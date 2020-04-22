"""usersystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
""" 
from django.contrib import admin
from django.urls import path
from . import views


app_name='usersystem'

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', views.add_user, name='add_user'),
   # path('manage_user/', views.manage_user, name="manage_user"),
   # path('edit_user/<int:user_id>', views.edit_user, name="edit_user"),
    path('', views.index, name='index'),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('register/', views.register, name="register"),
    path('register_user/', views.register_user, name="register_user"),
    path('all_users/', views.all_users, name="all_users"),
    path('delete_user/<int:myid>', views.delete_user, name="delete_user"),
    path('get_user/<int:myid>', views.get_user, name="get_user"),
    path('update_user/<int:myid>', views.update_user, name="update_user"),
    path('approve_user/<int:myid>', views.approve_user, name="approve_user"),
    path('login_user/', views.login_user, name="login_user"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('logout_admin/', views.logout_admin, name="logout_admin"),
    
    
    

]  
