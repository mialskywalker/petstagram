from django.shortcuts import render, redirect
from petstagram.photos.models import Photo
from petstagram.common.models import Like


# Create your views here.


def show_home_page(request):
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos
    }

    return render(request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')
