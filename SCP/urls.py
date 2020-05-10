"""SCP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from SCPapp import views as s
from MockSchedularApp import views as m
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getData/', s.getData.as_view()),
    path('postData/', s.postData.as_view()),
    path('deleteData/<id>', s.deleteData),
    path('patchData/<int:id>/', s.patchData.as_view()),
    re_path(r'^api/students/$', m.students_list),
    re_path(r'^api/students/([0-9]+)$', m.students_detail),
    re_path(r'^api/students/sendmail/([0-9]+)$', m.sendmail),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
