from django.shortcuts import render

def get_index_page(request):
    return render(request, "social_network/index.html")
