from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request, Review
from .telegram import send_telegram_message

@receiver(post_save, sender=Request)
def notify_new_request(sender, instance, created, **kwargs):
    if created:
        text = (
            f"*У тебя новая заявка!*\n"
            f"*№ заявки:* {instance.id}\n"
            f"*Имя клиента:* {instance.client_name}\n"
            f"*E-mail:* {instance.email}\n"
            f"*Телефон:* {instance.phone_number or 'Не указан'}\n"
            f"*Сообщение:* {instance.message or 'Нет'}\n"
            f"*Дата создания заявки:* {instance.created_at.strftime('%d.%m.%Y %H:%M')}"
        )
        send_telegram_message(text)

@receiver(post_save, sender=Review)
def notify_new_review(sender, instance, created, **kwargs):
    if created:
        text = (
            f"*У тебя новый отзыв!*\n"
            f"*Имя клиента:* {instance.client_name or 'Аноним'}\n"
            f"*Текст отзыва:* {instance.text}\n"
            f"*Оценка:* {instance.rating}/5\n"
            f"*Опубликован:* {'Да' if instance.is_published else 'Нет'}"
        )
        send_telegram_message(text)
