from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import views
from . import tests

admin.site.site_header = "TKD Main Admin"
admin.site.site_title = "TKD Main Admin"
admin.site.index_title = "Welcome to TKD"

urlpatterns = [
    path('password/', views.passwordjson.as_view()),
    path('password/<int:lenght>', views.custompassword.as_view()),
    path('exracturl/', views.exracturl.as_view()),
    path('instagram/', views.instagramurl.as_view()),
]