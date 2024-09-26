from django.urls import path

from servicing.views import home_page_view, about_page_view, contact_page_view, service_page_view, booking_page_view, \
    team_page_view, testimonial_page_view

urlpatterns = [
    path('', home_page_view, name='home_page'),
    path('about/', about_page_view, name='about_page'),
    path('contact/', contact_page_view, name='contact_page'),
    path('service/', service_page_view, name='service_page'),
    path('booking/', booking_page_view, name='booking_page'),
    path('team/', team_page_view, name='team_page'),
    path('testimonial/', testimonial_page_view, name='testimonial_page'),
    path('contact/', contact_page_view, name='contact_page')
]
