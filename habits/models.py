from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    PERIOD_CHOICES = [
        ('daily', 'Ежедневно'),
        ('twice a week', 'Два раза в неделю'),
        ('three times a week', 'Три раза в неделю'),
        ('weekly', 'Раз в неделю')
    ]

    ACTION_CHOICES = [
        ('study', 'Изучать новое'),
        ('develop', 'Развивать личные и профессиональные навыки'),
        ('sport', 'Заниматься спортом'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='Место', **NULLABLE)
    time = models.DateTimeField(verbose_name='Время', **NULLABLE)
    action = models.CharField(max_length=200, choices=ACTION_CHOICES, verbose_name='Действие', **NULLABLE)
    is_nice = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    habits = models.ForeignKey('Habit', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES, verbose_name='Периодичность', **NULLABLE)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    lead_time = models.IntegerField(verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
