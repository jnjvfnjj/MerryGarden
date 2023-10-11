from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name="Название"
        )
    description = models.TextField(
        verbose_name="Описание"
    )
    login = models.ImageField(
        upload_to="logo_image/",
        verbose_name="логотип",
    )
    phone = models.CharField(
        max_length=200,
        verbose_name="телефонный номер"
    )
    class Meta:
        verbose_name = "Основные настройки"
        verbose_name_plural = "Основная настройка"

class Gallery(models.Model):
    best_photo = models.ImageField(
        upload_to="logo_image/",
        verbose_name="лучшиии фото"
    )
    photos = models.ImageField(
        upload_to='logo_image/',
        verbose_name="фото"
    )

    class Meta:
        verbose_name = "Настройки галереи",
        verbose_name_plural = "Настройка голорея"

class About(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="имя"
    )
    number = models.CharField(
        max_length=20,
        verbose_name="телефоннный номер"
    )
    info = models.TextField(
        verbose_name="информация"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Про нас",
        verbose_name_plural = "Про участника"

class Contact(models.Model):
    youtube = models.URLField(
        verbose_name="ютуб"
    )
    fasebook = models.URLField(
        verbose_name="фейсбук"
    )

    class Meta:
        verbose_name = "Контакты",
        verbose_name_plural = "Контакт"
class News(models.Model):
    last_news = models.TextField(
        verbose_name="Последние новости"
    )
    all_news = models.TextField(
        verbose_name="Все новости"
    )
    class Meta:
        verbose_name = "Новости",
        verbose_name_plural = "Новост"
class Post(models.Model):
    post = models.TextField(
        verbose_name="Посты"
    )

    class Meta:
        verbose_name = "Посты",
        verbose_name_plural = "Пост"
class Team(models.Model):
    person = models.CharField(
        max_length=30,
        verbose_name="Команда"
    )