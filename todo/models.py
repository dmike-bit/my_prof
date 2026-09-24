from django.db import models
from django.contrib.auth.models import User

class  Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # Основные поля ФИО
    surname = models.CharField("Фамилия", max_length=30)
    name = models.CharField("Имя", max_length=15)
    patronymic = models.CharField("Отчество", max_length=30, blank=True)  # может быть пустым

    # Контактные данные
    email = models.EmailField("Email", unique=True)  # уникальный, не может повторяться

    # Автоматическая дата
    created_at = models.DateTimeField("Дата регистрации", auto_now_add=True)

    def __str__(self):
        # Возвращаем ФИО для отображения в админке
        return f"{self.surname} {self.name} {self.patronymic}".strip()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["surname", "name"]  # сортировка: сначала по фамилии, потом по имени