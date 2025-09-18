from .models import Logo

def menu_items(request):
    user_menu = [
        {'title': 'О себе', 'url_name': 'about', 'anchor': '', 'icon': 'bi bi-person'},
        {'title': 'Стоимость', 'url_name': 'home', 'anchor': 'services', 'icon': 'bi bi-cash'},
        {'title': 'Контакты', 'url_name': 'contacts', 'anchor': '', 'icon': 'bi bi-phone'},
        {'title': 'Отзывы', 'url_name': 'reviews', 'anchor': '', 'icon': 'bi bi-award'},
        {'title': 'Расписание', 'url_name': 'schedule', 'anchor': '', 'icon': 'bi bi-calendar-week'},
    ]

    admin_menu = []
    if request.user.is_authenticated and request.user.is_staff:
        admin_menu.append({'title': 'Заявки', 'url': 'requests', 'icon': 'bi bi-view-list'})
        admin_menu.append({'title': 'Админка', 'url': 'admin:index', 'icon': 'bi bi-shield-lock'})

    return {
        'user_menu': user_menu,
        'admin_menu': admin_menu,
    }

def logo_context(request):
    return {
        'logo': Logo.objects.first()
    }