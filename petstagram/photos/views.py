from django.shortcuts import render, redirect
from petstagram.photos.forms import PhotoCreateForm
from petstagram.photos.models import Photo

# Create your views here.


def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    context = {"form": form}

    return render(request, template_name='photos/photo-add-page.html', context=context)


def photo_details(request, pk):
    return render(request, 'photos/photo-details-page.html')


def photo_edit(request, pk):
    return render(request, 'photos/photo-edit-page.html')
