def menu_items(request):
    user_menu = [
        {'title': 'О себе', 'url': 'about', 'icon': 'bi bi-person'},
        {'title': 'Услуги', 'url': 'services', 'icon': 'bi bi-card-checklist'},
        {'title': 'Контакты', 'url': 'contacts', 'icon': 'bi bi-phone'},
        {'title': 'Отзывы', 'url': 'reviews', 'icon': 'bi bi-award'},
        {'title': 'Расписание', 'url': 'schedule', 'icon': 'bi bi-calendar-week'},
    ]

    admin_menu = []
    if request.user.is_authenticated and request.user.is_staff:
        admin_menu.append({'title': 'Заявки', 'url': 'requests', 'icon': 'bi bi-view-list'})
        admin_menu.append({'title': 'Админка', 'url': 'admin:index', 'icon': 'bi bi-shield-lock'})

    return {
        'user_menu': user_menu,
        'admin_menu': admin_menu,
    }