from django.contrib import admin, messages
from .models import Request, Review, Service, Teacher, Logo, Video, GalleryImage
from django.contrib.admin.actions import delete_selected as default_delete_selected
from adminsortable2.admin import SortableAdminMixin

def custom_delete_selected(modeladmin, request, queryset):
    count = queryset.count()
    queryset.delete()
    modeladmin.message_user(
        request,
        f'{count} отзыв(ов) успешно удалено',
        level=messages.SUCCESS
    )

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'email', 'phone_number', 'created_at']
    search_fields = ['client_name', 'email', 'phone_number']
    list_filter = ['created_at']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'text', 'rating', 'is_published']
    search_fields = ['client_name', 'text']
    actions = ['mark_as_published', 'mark_as_unpublished', 'custom_delete_selected']
    list_filter = ['is_published', 'rating']

    @admin.action(description='Опубликовать отзыв(ы)')
    def mark_as_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, f'{updated} отзыв(ов) опубликовано')

    @admin.action(description='Снять отзыв(ы) с публикации')
    def mark_as_unpublished(self, request, queryset):
        updated = queryset.update(is_published=False)
        self.message_user(request, f'{updated} отзыв(ов) снято с публикации')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            actions["delete_selected"] = (
                custom_delete_selected,
                'delete_selected',
                'Удалить выбранные отзывы'
            )
        return actions

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price']
    search_fields = ['title']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'education', 'experience', 'email')

@admin.register(GalleryImage)
class GalleryImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['__str__', 'image', 'order']

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "embed_url")
