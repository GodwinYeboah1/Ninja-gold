from django.conf.urls import url,include
from .  import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^process_money$', views.proccess_money)
]
