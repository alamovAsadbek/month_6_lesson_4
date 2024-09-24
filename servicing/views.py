from django.shortcuts import render


# home page
def home_page_view(request):
    return render(request, 'index.html')
