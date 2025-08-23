def menu_items(request):
    menu = [
        {'title': 'О себе', 'url': 'about'},
        {'title': 'Услуги', 'url': 'services'},
        {'title': 'Контакты', 'url': 'contacts'},
        {'title': 'Отзывы', 'url': 'reviews'},
    ]

    if request.user.is_authenticated and request.user.is_staff:
        menu.append({'title': 'Заявки', 'url': 'requests'})
        menu.append({'title': 'Админка', 'url': 'admin:index'})

    return {'menu_items': menu}