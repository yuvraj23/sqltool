"""Easy_Sql_Tool URL Configuration

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
from django.urls import path, re_path
from sqltoolapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('select_form/',views.show_select_form,name='select_form'),
    path('update_form/',views.show_update_form,name='update_form'),
    path('delete_form/',views.show_delete_form,name='delete_form'),

    re_path('selectq/<str:query_type>/$', views.SELECT_QUERY_GENERATOR,name='selectq'),
    re_path('updateq/<str:query_type>/$', views.UPDATE_QUERY_GENERATOR,name='updateq'),
    re_path('deleteq/<str:query_type>/$', views.DELETE_QUERY_GENERATOR,name='deleteq'),


]
