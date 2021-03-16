
from django.contrib import admin
from django.urls import path
from User_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='main'),
    path('Ajax_FileUpload/',views.Ajax_FileUpload,name='Ajax_FileUpload'),
    path('Search/',views.Search,name='Search'),
]
