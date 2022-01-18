from django.urls import re_path
from basics import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^student/$', views.StudentApi),
    re_path(r'^student/([0-9]+)$',views.StudentApi),
]