"""djproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from home.views import home_view,contact,about,deletestudent,editstudent,createstudent
from acc.views import home_view,user_login,register,user_logout

from home import views 
from account import views
urlpatterns = [
    path('',views.home_view),
    path('home/',include('home.urls')),
    path('admin/',admin.site.urls),
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
   # path('delete-student/<id>',deletestudent),
   # path('edit-student/<id>',editstudent),
   # path('admin/', admin.site.urls),
   # path('contact/',contact),
   # path('about/',about),
   # path('create-student/',createstudent),
]
