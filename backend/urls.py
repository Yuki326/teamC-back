from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from backend import views

urlpatterns = [
    path('test',views.test),
    path('admin/', admin.site.urls),
]
urlpatterns = format_suffix_patterns(urlpatterns)
