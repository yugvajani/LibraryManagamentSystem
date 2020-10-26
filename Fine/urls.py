from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views as fine_views

urlpatterns = [
    # path('/', fine_views.check_fines,name='view-fines'),
    # path('', fine_views.manage_fines,name='manage-fines'),
    path('view/', fine_views.check_fines,name='view-fines'),
    path('pay/<int:id>/', fine_views.pay_fine,name='pay-fine'), #only librarian
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)