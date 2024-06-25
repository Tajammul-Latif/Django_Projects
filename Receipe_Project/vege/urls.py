from django.urls import path
from vege.views import *

urlpatterns = [
    path('', receipes, name='receipes'),
    path('show-receipes/', showReceipes, name='show_receipes'),
    path('delete-receipe/<int:id>/', delete_receipe, name='delete_receipe'),
    path('update-receipe/<int:id>/', update_receipe, name='update_receipe'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('register/', registerPage, name='register_page')
]
