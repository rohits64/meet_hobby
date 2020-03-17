from django.urls import path
from .views import signup
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', signup, name='signup'),
    # path('', views.post_list, name='post_list'),
]
