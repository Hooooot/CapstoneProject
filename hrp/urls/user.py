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

from hrp.views.user_views import Home, Myself, GetNewestPosition, Job, Search

# User 的路由表  /user/
urlpatterns = [
    path('home/load/', Home.Load.as_view()),
    path('sign_in/', Home.SignIn.as_view()),
    path('submit_name/', Home.ChangeName.as_view()),

    path('home/intent/change/', Home.ChangeIntent.as_view()),
    path('home/intent/show/', Home.ShowIntent.as_view()),

    path('newest/show/', GetNewestPosition.as_view()),

    path('myself/resume/create/', Myself.CreateResume.as_view()),
    path('myself/resume/show/', Myself.ShowResume.as_view()),
    path('myself/resume/delete/', Myself.DeleteResume.as_view()),
    path('myself/delivery_history/', Myself.DeliveryHistory.as_view()),
    path('myself/show_history/', Myself.ShowHistory.as_view()),

    path('job/detail/', Job.ShowDetail.as_view()),
    path('job/is_favor/', Job.IsFavor.as_view()),
    path('job/set_favor/', Job.SetFavor.as_view()),
    path('job/show_favor/', Job.ShowFavor.as_view()),
    path('job/cancel_favor/', Job.CancelFavor.as_view()),

    path('job/is_delivery/', Job.IsDeliveryResume.as_view()),

    path('job/delivery/', Job.DeliveryResume.as_view()),

    path('search/', Search.as_view())
]
