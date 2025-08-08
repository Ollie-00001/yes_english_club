from django.shortcuts import render

def about(request):
    return render(request, 'core/about.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def order_details(request):
    return render(request, 'core/order_details.html')

def orders(request):
    return render(request, 'core/orders.html')

def reviews(request):
    return render(request, 'core/reviews.html')

def services(request):
    return render(request, 'core/services.html')
