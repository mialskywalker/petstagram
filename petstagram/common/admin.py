from django.contrib import admin
from petstagram.common.models import Comment, Like


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "date_time_of_publication", "to_photo")


class LikeAdmin(admin.ModelAdmin):
    list_display = ("to_photo",)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
