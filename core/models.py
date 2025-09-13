from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.html import format_html
import re
import requests

class Request(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    email = models.EmailField(verbose_name='Почта')
    phone_number = PhoneNumberField(region='RU', null=True, blank=False, verbose_name='Номер телефона')
    message = models.TextField(verbose_name='Сообщение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заявки')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

    def __str__(self):
        return f"{self.client_name} ({self.created_at.strftime('%d.%m %H:%M')})"
    
class Review(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    client_name = models.CharField(max_length=100, blank=True, verbose_name='Имя клиента')
    text = models.TextField(max_length=500, verbose_name='Текст отзыва')
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES, 
        verbose_name='Оценка',
        default=5
        )
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.client_name or 'Аноним'} - {self.rating}/5'

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Услуга')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title
    
class Teacher(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    education = models.TextField(verbose_name='Образование', blank=True)
    experience = models.CharField(max_length=100, verbose_name='Опыт работы', blank=True)
    email = models.EmailField(verbose_name='Email')
    photo = models.ImageField(upload_to='teacher_photos/', verbose_name='Фото', blank=True, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)

    def blank_description(self):
        if not self.description:
            return ""
        return self.description

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.name

class Logo(models.Model):
    image = models.ImageField(upload_to='logos/', verbose_name='Логотип')

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипы'

    def __str__(self):
        return f'Логотип {self.id}'

    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" height="50"/>', self.image.url)
        return "-"
    image_tag.short_description = 'Превью'

class Video(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    original_url = models.URLField(verbose_name="Ссылка на видео")
    embed_url = models.URLField(verbose_name="Встраиваемая ссылка (генерируется автоматически, вставлять ничего не нужно)", blank=True)

    def generate_vk_iframe(self, Autoplay=False, hd=3, use_vk_com_domain=True):

        pattern = re.compile(r'https://vkvideo\.ru/video(-[0-9]+)_([0-9]+)')

        match = pattern.search(self.original_url)
        
        if not match:
            print(f"Неверный формат URL для VK Video {self.original_url}")
            return None
        
        oid = match.group(1)
        video_id = match.group(2)

        domain = 'vk.com' if use_vk_com_domain else 'vkvideo.ru'

        autoplay_value = 1 if Autoplay else 0

        embed_url = f"https://{domain}/video_ext.php?oid={oid}&id={video_id}&hash=1&hd={hd}&autoplay={autoplay_value}"
        
        return embed_url
    
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def save(self, *args, **kwargs):
        self.embed_url = self.generate_vk_iframe(Autoplay=False)
        super().save(*args, **kwargs)