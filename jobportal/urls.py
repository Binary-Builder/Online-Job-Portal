"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from job.views import *
from django.conf  import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_login',user_login,name="user_login"),
    path('recruiter_login',recruiter_login,name="recruiter_login"),
    path('user_signup',user_signup,name="user_signup"),
    path('user_home',user_home,name="user_home"),
    path('recruiter_signup', recruiter_signup, name="recruiter_signup"),
    path('recruiter_home', recruiter_home, name="recruiter_home"),
    path('admin_home', admin_home, name="admin_home"),
    path('Logout',Logout,name="Logout"),
    path('view_users', view_users, name="view_users"),
    path('recruiter_pending', recruiter_pending, name="recruiter_pending"),
    path('recruiter_accepted', recruiter_accepted, name="recruiter_accepted"),
    path('recruiter_rejected', recruiter_rejected, name="recruiter_rejected"),
    path('recruiter_all', recruiter_all, name="recruiter_all"),
    path('delete_user/<int:pid>', delete_user, name="delete_user"),
    path('add_job', add_job, name="add_job"),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
