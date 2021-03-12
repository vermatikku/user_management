from django.db import models
from django.contrib.auth.models import User
from ideateusermanagement.enums import YesNo
from datetime import datetime
import uuid

# # Create your models here.
class IdeateApp(models.Model):
    app_name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.app_name

class UserMetaData(models.Model):
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    creation_date_time = models.DateTimeField(default=datetime.now)
    active = models.CharField(max_length=2, choices=YesNo.choices(), default='N')

class UserBasicDetails(models.Model):
    middle_name = models.CharField(max_length=50,default=None,blank=True,null=True)
    mobile_number = models.CharField(max_length=20,default=None,blank=True,null=True)
    user_name = models.CharField(max_length=100,default=None,blank=True,null=True)

class UserPersonalDetails(models.Model):
    gender = models.CharField(max_length=20,default=None,blank=True,null=True)
    dob = models.DateField(default=None,blank=True,null=True)

class VerificationDetails(models.Model):
    mobile_verified = models.CharField(max_length=2, choices=YesNo.choices(), default='N')
    mail_verified = models.CharField(max_length=2, choices=YesNo.choices(), default='N')
    profile_verified = models.CharField(max_length=2, choices=YesNo.choices(), default='N')

def profile_pic_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    filename.replace('-','_')
    return "profile_pic_{}".format(filename)
    
class ProfilePic(models.Model):
    profile_pic = models.ImageField(upload_to = profile_pic_path)

class BasicAddress(models.Model):
    name = models.CharField(max_length=100,default=None,blank=True,null=True)
    mobile_number = models.CharField(max_length=20,default=None,blank=True,null=True)
    is_primary = models.CharField(max_length=2, choices=YesNo.choices(), default='N')
    address_line_1 = models.TextField(blank=True)
    address_line_2 = models.TextField(blank=True)
    city = models.CharField(max_length=20,default=None,blank=True,null=True)
    district = models.CharField(max_length=20,default=None,blank=True,null=True)
    a_state = models.CharField(max_length=20,default=None,blank=True,null=True)
    pincode = models.CharField(max_length=20,default=None,blank=True,null=True)
    country = models.CharField(max_length=20,default=None,blank=True,null=True)

class UserAllData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    user_meta_data = models.ForeignKey(UserMetaData,on_delete=models.CASCADE)
    user_basic_details = models.ForeignKey(UserBasicDetails,on_delete=models.CASCADE,default=None,blank=True,null=True)
    user_personal_details = models.ForeignKey(UserPersonalDetails,on_delete=models.CASCADE,default=None,blank=True,null=True)
    verification_details = models.ForeignKey(VerificationDetails,on_delete=models.CASCADE,default=None,blank=True,null=True)
    profile_pic = models.ForeignKey(ProfilePic,on_delete=models.CASCADE,default=None,blank=True,null=True)
    basic_address = models.ForeignKey(BasicAddress,on_delete=models.CASCADE,default=None,blank=True,null=True)
    app = models.ForeignKey(IdeateApp,on_delete=models.CASCADE,default=None,blank=True,null=True)