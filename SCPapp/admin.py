from django.contrib import admin

from .models import File, Interview, Login, CommentsPYQ, CommentsExp, emailVerify

admin.site.register(File)
admin.site.register(Interview)
admin.site.register(Login)
admin.site.register(CommentsPYQ)
admin.site.register(CommentsExp)
admin.site.register(emailVerify)

# Register your models here.
