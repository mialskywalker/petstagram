from django.shortcuts import render, redirect
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.pets.models import Pet


# Create your views here.

def pet_add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)
    context = {'form': form}
    return render(request, template_name='pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def pet_edit(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_slug)
    context = {'form': form}

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def pet_delete(request, username, pet_slug):
    pet = Pet.objects.get(slug=pet_slug)
    if request.method == 'POST':
        pet.delete()
        return redirect('profile-details', pk=1)
    form = PetDeleteForm(initial=pet.__dict__)
    context = {'form': form}

    return render(request, template_name='pets/pet-delete-page.html', context=context)
