
from django.contrib import admin
from django.urls import path
from Calculator import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.showCalculator),
    path('services/', views.showServices),
    path('form-data/', views.showForm),
    path('save-form/', views.saveForm, name='save_data')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
