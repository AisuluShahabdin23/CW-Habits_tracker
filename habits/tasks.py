import os
from datetime import timedelta
from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from habits.services import send_message
from users.models import User


@shared_task
def send_notification():
    time_now = timezone.now()
    habits = Habit.objects.all()
    users = User.objects.objects.all()
    token = os.getenv('TELEGRAM_TOKEN')
    for habit in habits:
        for user in users:
            if habit.time >= time_now - timedelta(minutes=15):
                message = f"Напоминаю о привычке {habit.action}\n" \
                          f"Завершив, можно:\n \
    {habit.habits if habit.habits else habit.reward}"
                send_message(token=token,
                             chat_id=user.chat_id,
                             message=message)