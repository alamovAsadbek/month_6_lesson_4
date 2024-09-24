from django.shortcuts import render


# home page
def home_page_view(request):
    return render(request, 'index.html')


# about page
def about_page_view(request):
    return render(request, 'about.html')
