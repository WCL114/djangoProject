from django.urls import path
from . import views

app_name = 'userapp'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('accounts/center/<int:pk>/', views.user_center, name='user_center'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),

]
