from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('rockpaperscissors/', views.rockpaperscissors_view, name='rockpaperscissors'),
    path('', views.index_view, name='index'),
    path('user/<int:id>/', views.user_view, name='user'),
    path('ranking/', views.ranking_view, name='ranking'),
]