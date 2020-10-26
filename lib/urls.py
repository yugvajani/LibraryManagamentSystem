from django.contrib import admin
from django.urls import path, include
from lib import views as lib_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lib_views.manage_books,name='manage-books'),
    path('add/', lib_views.add_books,name='add-books'),
    path('view/', lib_views.view_books,name='view-books'),
    path('delete/<int:id>/',lib_views.delete_books,name='delete-books'),
    path('update/<int:id>/',lib_views.update_books,name='update-books'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)