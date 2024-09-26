from django.shortcuts import render

from servicing.models import ServiceModel


# home page
def home_page_view(request):
    context = {
        'servicing': ServiceModel.objects.all()
    }
    return render(request, 'index.html')


# about page
def about_page_view(request):
    return render(request, 'about.html')


# contact page
def contact_page_view(request):
    return render(request, 'contact.html')


# services page
def service_page_view(request):
    context = {
        'content': ServiceModel.objects.all()
    }
    return render(request, 'service.html', context)


# booking page
def booking_page_view(request):
    return render(request, 'booking.html')


# team page
def team_page_view(request):
    return render(request, 'team.html')


# testimonial page
def testimonial_page_view(request):
    return render(request, 'testimonial.html')


# 404 error page
def error_404_view(request, exception):
    return render(request, '404.html', status=404)
