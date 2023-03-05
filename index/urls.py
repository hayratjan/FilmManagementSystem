from django.urls import path, include
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/<int:pIndex>', views.index, name='index_page'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('star', views.star, name='star'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('password_update/', views.password_update, name='password_update'),
]
