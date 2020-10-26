"""library URL Configuration

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
from django.urls import path, include
from lib import views as lib_views
from users import views as user_views
from Transactions import views as transactions_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     path('', lib_views.welcome,name='library-welcome'),
#     path('admin/', admin.site.urls),
#     path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
#     path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout'),
#     path('home/',lib_views.home,name='home'),
#     path('manage-books/',lib_views.manage_books,name='manage-books'),
#     path('manage-users/',user_views.manage_users,name='manage-users'),
#     path('add-books/',lib_views.add_books,name='add-books'),
#     path('view-books/',lib_views.view_books,name='view-books'),
#     path('delete-books/<str:par1>/',lib_views.delete_books,name='delete-books'),
#     path('update-books/<str:par1>/',lib_views.update_books,name='update-books'),
#     path('add-users/',user_views.add_users,name='add-users'),
#     path('view-users/',user_views.view_users,name='view-users'),
#     path('delete-users/<int:id>/',user_views.delete_users,name='delete-users'),
#     path('update-users/<int:id>/',user_views.update_users,name='update-users'),
#     path('unauthorized',lib_views.unauthorized_access, name='unauthorized-access'),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', lib_views.welcome,name='library-welcome'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'),name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name = 'logout'),
    path('home/',lib_views.home,name='home'),
    path('books/',include('lib.urls')),
    path('users/',include('users.urls')),
    path('transactions/',include('Transactions.urls')),
    path('fines/',include('Fine.urls')),
    path('unauthorized',lib_views.unauthorized_access, name='unauthorized-access'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
