from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('profile/', views.index,name='index'),
    path('showgroup/', views.show_joined_group, name='show_joined_group'),
    path('newgroup/', views.show_new_group, name='show_new_group'),
    path('newgroup/<int:id>', views.join_group, name='join_group')
]
