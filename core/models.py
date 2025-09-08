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
    education = models.TextField(verbose_name='Образование')
    experience = models.CharField(max_length=100, verbose_name='Опыт работы')
    email = models.EmailField(verbose_name='Email')
    photo = models.ImageField(upload_to='teacher_photos/', verbose_name='Фото')

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
    title = models.CharField(max_length=200, verbose_name="Название видео")
    url = models.URLField(verbose_name="Ссылка на видео")

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title

    def embed_url(self):
        # --- YouTube ---
        if "youtube.com/watch" in self.url:
            video_id = re.search(r"v=([^&]+)", self.url).group(1)
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in self.url:
            video_id = self.url.split("/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"

        # --- VK ---
        elif "vk.com/video" in self.url and "video_ext.php" not in self.url:
            match = re.search(r"video(-?\d+)_(\d+)", self.url)
            if match:
                owner_id, video_id = match.groups()
                try:
                    r = requests.get("https://vk.com/video_ext.php", params={
                        "oid": owner_id,
                        "id": video_id
                    })
                    if r.status_code == 200:
                        return f"https://vk.com/video_ext.php?oid={owner_id}&id={video_id}"
                except:
                    return None
        return self.url