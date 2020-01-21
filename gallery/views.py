from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Gallery
from .forms import AddImageForm


def add(request):
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect(reverse('gallery:success'))
    else:
        form = AddImageForm()
    return render(request, 'gallery/add.html', {
        'form': form,
    })


def success(request):
    return HttpResponse('success uploaded')
