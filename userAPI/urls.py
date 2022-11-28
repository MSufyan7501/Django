from django.urls import path
from userAPI.views import TextView
from rest_framework_simplejwt.views import token_refresh,token_verify

urlpatterns = [
    path('test', TextView.as_view()),
]
