from django.urls import path
from receipts.views import receipt_list
from accounts.views import user_login

urlpatterns = [
    path("", receipt_list, name="home"),
    path("login/", user_login, name="login"),
]
