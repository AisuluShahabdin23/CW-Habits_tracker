from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """ Класс погинации вывода списка привычек с выводом по 5 привычек на страницу"""
    page_size = 5
