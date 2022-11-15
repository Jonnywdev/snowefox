from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_clubs, name='clubs'),
    path('<club_id>', views.club_detail, name='club_page'),
]
