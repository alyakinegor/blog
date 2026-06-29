from django.shortcuts import render

def post_lists(request):
    return render(request, 'home.html')