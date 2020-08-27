from django.contrib import admin

from .models import File,Interview,Login,CommentsPYQ,CommentsExp

admin.site.register(File)
admin.site.register(Interview)
admin.site.register(Login)
admin.site.register(CommentsPYQ)
admin.site.register(CommentsExp)

# Register your models here.
