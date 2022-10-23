from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from thekoushikdurgas import views
urlpatterns = [
    path('',include('thekoushikdurgas.urls')),
    path('admin/', admin.site.urls),
]
