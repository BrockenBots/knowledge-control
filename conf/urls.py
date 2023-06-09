"""
URL configuration for knowledge_control project.

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

from main.views import AllUserTestAPIView, AuthorizationUserAPIView, TestAPIView, CheckResultAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/auth', AuthorizationUserAPIView.as_view()),
    path('api/v1/test/test_cat/', AllUserTestAPIView.as_view()),
    path('api/v1/test/test_cat/id/', TestAPIView.as_view()),
    path('api/v1/test/test_cat/id/result/', CheckResultAPIView.as_view()),
    # path('api/vq/test/test_cat/id/result/check', CheckResultAPIView.as_view()),
]
