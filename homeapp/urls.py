
from django.urls import path
from homeapp import views

urlpatterns = [
    path('',views.registration,name="registration"),
    path('login',views.login_page,name="login"),   
    path('home/',views.home_page,name="home"),
    path('signout',views.signout,name="signout"),

    path('index/',views.index,name="index"),
    path('insert',views.insertData,name="insertData"), # name="" is used for html page url {{urls }}
    path('update/<id>',views.updateData,name="updateData"),
    path('delete/<id>',views.deleteData,name="deleteData"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('logoutpage',views.logoutpage,name="logoutpage"),
]

