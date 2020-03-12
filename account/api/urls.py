from django.urls import path
from account.api.views import Register, Login, ListAccounts

urlpatterns = [
    path('', ListAccounts.as_view(), name='list_accounts'),
    path('register', Register.as_view(), name='register'),  # Creates account and sends back token
    path('login', Login.as_view(), name='login')
]
