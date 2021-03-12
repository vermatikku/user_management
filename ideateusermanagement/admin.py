from django.contrib import admin
from .models import IdeateApp,UserMetaData,UserBasicDetails
from .models import UserPersonalDetails,VerificationDetails,ProfilePic,BasicAddress,UserAllData
# Register your models here.
admin.site.register(IdeateApp)
admin.site.register(UserMetaData)
admin.site.register(UserBasicDetails)
admin.site.register(UserPersonalDetails)
admin.site.register(VerificationDetails)
admin.site.register(ProfilePic)
admin.site.register(BasicAddress)
admin.site.register(UserAllData)