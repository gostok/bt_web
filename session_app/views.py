import asyncio
import aiohttp
from asgiref.sync import async_to_sync
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from home_app.models import SidebarNews
from .models import *
from .forms import *
from datetime import datetime


BOT_TOKEN = "7247051447:AAEh7VTA9zJ88n6A8Y75I1CNjw8mW0nXZpY"  # Токен бота тест
CHAT_ID = "1393180508"  # ID Anton
# BOT_TOKEN = "5383497492:AAHxd-yAXqGURMm_ISNCJb08l0RXCHjfdPg" # Токен бота BjusTattoo
# CHAT_ID = "-1002124714510" # ID чата сотрудников


async def send_to_tg(
    tg_session_name, tg_session_date, tg_session_time, tg_session_contact
):
    message = (
        f"Новая запись:\n\n"
        f"Имя: {tg_session_name}\n"
        f"Дата: {tg_session_date}\n"
        f"Время: {tg_session_time}\n"
        f"Контакт: {tg_session_contact}"
    )

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": message},
        ) as resp:
            if resp.status != 200:
                print(f"Error: {resp.status}, Message: {await resp.text()}")


class BookSessionView(View):
    @method_decorator(csrf_exempt)
    def get(self, request):
        print("GET запрос к BookSessionView")

        sidebar_news = SidebarNews.objects.all()
        form = SessionForm()
        available_dates = AvailableDate.objects.prefetch_related(
            "available_times"
        ).all()

        selected_date = request.GET.get("date", "")
        selected_time = request.GET.get("time", "")
        context = {
            "sidebar_news": sidebar_news,
            "form": form,
            "available_dates": available_dates,
            "selected_date": selected_date,
            "selected_time": selected_time,
        }
        return render(request, "session.html", context)

    def post(self, request):
        print("POST запрос к BookSessionView")
        form = SessionForm(request.POST)
        if form.is_valid():
            print("Форма валидна")
            tg_session = form.save()
            print("Запись успешно сохранена:")
            print(
                f"Имя: {tg_session.name}, Дата: {tg_session.date}, Время: {tg_session.time}, Контакт: {tg_session.contact_info}"
            )

            try:
                async_to_sync(send_to_tg)(
                    tg_session.name,  # Передайте имя
                    tg_session.date,
                    tg_session.time,
                    tg_session.contact_info,
                )
            except Exception as e:
                print(f"Ошибка при отправке сообщения в Telegram: {e}")
                return JsonResponse(
                    {
                        "success": False,
                        "error": "Не удалось отправить сообщение в Telegram.",
                    },
                    status=500,
                )

            return JsonResponse({"success": True})

        else:
            print(form.errors)
            return JsonResponse({"success": False, "errors": form.errors}, status=400)


@require_GET
def get_times(request):
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        date = request.GET.get("date")
        if not date:
            return JsonResponse({"error": "Дата не предоставлена."}, status=400)

        available_date = AvailableDate.objects.filter(date=date).first()

        if not available_date:
            return JsonResponse({"error": "Дата не найдена."}, status=404)

        available_times = available_date.available_times.values_list("time", flat=True)

        return JsonResponse(list(available_times), safe=False)

    return JsonResponse({"error": "Это не AJAX-запрос!"}, status=400)
