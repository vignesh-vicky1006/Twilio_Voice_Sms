from django.urls import path
from .views import  make_call,send_sms

urlpatterns = [
    # path("", index, name="index"),
    path("make_call/", make_call, name="make_call"),
    path('send_sms/', send_sms, name='send_sms'),
]
