from django.contrib import admin
from django.urls import path, include
# from lib import views as lib_views
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', user_views.manage_users,name='manage-users'),
    path('add/', user_views.add_users,name='add-users'),
    path('view/', user_views.view_users,name='view-users'),
    path('delete/<int:id>/',user_views.delete_users,name='delete-users'),
    path('update/<int:id>/',user_views.update_users,name='update-users'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)