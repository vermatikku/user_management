"""ideateuserapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path
from ideateusermanagement.views import *

router = DefaultRouter()
router.register('user', UserManagementViewSet,basename='user')
router.register('users', UserViewSet, basename='users')
router.register('basicdetails', UserBasicDetailsViewSet, basename='basicdetails')
router.register('metadata', UserMetaDataViewSet, basename='metadata')
router.register('personaldetails', UserPersonalDetailsViewSet, basename='personaldetails')
router.register('verificationdetails', VerificationDetailsViewSet, basename='verificationdetails')
router.register('profilepic', ProfilePicViewSet, basename='profilepic')
router.register('address', BasicAddressViewSet, basename='address')

urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
    path('user/<int:id>/users/<int:target_id>/', UserManagementViewSet.as_view({"get": "user_details"}))
    #reset password using mobile
    #reset password using mail
    #activate user by mobile otp
    #activate user by mail otp
    #verify mobile
    #verify mail
    #login 
    #logout
    #authentaton
    #
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

