"""CapstoneProject URL Configuration

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
# from django.contrib import admin
from django.urls import path

from hrp.views.hr_views import CreateCompany, ShowCompanies, GetFile, ShowPositions, CreatePosition, ShowResumes, \
    DeleteCompany, DeletePosition

# HR 的路由表
urlpatterns = [
    #    path('admin/', admin.site.urls),
    path('company/create/', CreateCompany.as_view()),
    path('company/show/', ShowCompanies.as_view()),
    path('company/delete/', DeleteCompany.as_view()),

    path('company/position/create/', CreatePosition.as_view()),
    path('company/position/show/', ShowPositions.as_view()),
    path('company/position/delete/', DeletePosition.as_view()),

    path('company/position/resume/show/', ShowResumes.as_view()),
    path('company/position/resume/delete/', ShowResumes.as_view()),

    path('get_file/', GetFile.as_view()),

]
