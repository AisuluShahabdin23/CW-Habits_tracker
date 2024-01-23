import os
from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_notification():
    time_now = timezone.now() + timedelta(hours=3)
    habits_users = Habit.objects.filter(user__telegram_id__isnull=False).prefetch_related('user')
    token = os.getenv('TELEGRAM_TOKEN')

    for habit in habits_users:
        if habit.time >= time_now - timedelta(seconds=1):
            message = f"Напоминаю о привычке {habit.action}\n" \
                      f"Завершив, можно: {habit.habits if habit.habits else habit.reward}"
            send_telegram_message(token=token,
                                  chat_id=habit.user.chat_id,
                                  message=message)
