from .views import Index , signup, login, logout
from django.urls import path

urlpatterns = [
    path('',Index.as_view(), name='homepage'),
    path('signup', signup),
    path('login', login.as_view(), name='login'),
    path('logout',logout, name='logout')

]
