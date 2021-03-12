from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import exceptions
from ideateusermanagement.models import *
from ideateusermanagement.helper import UserManagementSerializerHelper

class UserAltSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username'
        ]
        read_only_fields = ('id','username')

class UserSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # first_name = serializers.CharField()
    # last_name = serializers.CharField()
    # email = serializers.CharField()
    # username = serializers.CharField(required=False)
    # password = serializers.CharField(write_only=True, editable=False)
    # def create():
    #         raise serializers.ValidationError("finish must occur after start")
    #     pass

    # def validate():
    #     pass
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True,}}
        # read_only_fields = ('id')#,'username')
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data.pop('password'))
        user.save()
        return user
        # def update(self, instance, validated_data):
        #     print('mera naam')
        #     # instance = super(self).update(instance,validated_data)
        #     # if(password = validated_data.pop('password')):
        #         #rise error password can't update
        #     instance.first_name = validated_data.get('first_name', instance.first_name)
        #     instance.last_name = validated_data.get('last_name', instance.last_name)
        #     instance.email = validated_data.get('email', instance.email)        
        #     instance.username = validated_data.get('username', instance.username)
        #     # instance = super(ProduitUpdateSerializer,self).update(instance, validated_data)
        #     # instance.email = validated_data.get('email', instance.email)
        #     # instance.content = validated_data.get('content', instance.content)
        #     # instance.created = validated_data.get('created', instance.created)
        #     instance.save()
        #     print(instance)
        #     print('hello world')
        #     return instance
        
####block password update
class UserBasicDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBasicDetails
        fields = [
            'middle_name',
            'mobile_number',
            'user_name'
        ]
        read_only_fields = ('id',)

class UserMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMetaData
        fields = [
            'created_by',
            'creation_date_time',
            'active'
        ]
        read_only_fields = ('id',)

class UserPersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersonalDetails
        fields = [
            'gender',
            'dob'
        ]
        read_only_fields = ('id',)

class VerificationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationDetails
        fields = [
            'mobile_verified',
            'mail_verified',
            'profile_verified'
        ]
        read_only_fields = ('id',)

class ProfilePicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePic
        fields = [
            'profile_pic'
        ]
        read_only_fields = ('id',)

class BasicAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicAddress
        fields = [
            'name',
            'mobile_number',
            'is_primary',
            'address_line_1',
            'address_line_2',
            'city',
            'district',
            'a_state',
            'pincode',
            'country'
        ]
        read_only_fields = ('id',)

class PasswordUpdateSerializer(serializers.Serializer):
    pass

class UserManagementSerializer(serializers.Serializer):
    app_id = serializers.IntegerField(required=True)
    first_name = serializers.CharField(max_length=50)
    middle_name = serializers.CharField(max_length=50,required=False)
    last_name = serializers.CharField(max_length=50,required=False)
    user_name = serializers.CharField(max_length=50)
    username = serializers.CharField(read_only=True)
    email = serializers.CharField(max_length=50)
    mobile = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50,write_only=True)
    user_meta_data = UserMetaDataSerializer()
    user_personal_details = UserPersonalDetailsSerializer(required=False)
    verification_details = VerificationDetailsSerializer()
    profile_pic = ProfilePicSerializer(required=True)
    basic_address = BasicAddressSerializer(required=True)
    
    def validate(self,data):
        try:
            IdeateApp.objects.get(pk = data['app_id'])
        except IdeateApp.DoesNotExist:
            raise serializers.ValidationError("Invalid app id")
        return data

    def create(self, validated_data):
        app_id = validated_data.get('app_id')
        first_name = validated_data.get('first_name')
        middle_name = validated_data.get('middle_name')
        last_name = validated_data.get('last_name')
        user_name = validated_data.get('user_name')
        email = validated_data.get('email')
        mobile = validated_data.get('mobile')
        password = validated_data.get('password')
        username = user_name + str(app_id)
        validated_data.__setitem__('username',username)
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password = password
        user.save()
        user_basic_details = UserBasicDetails.objects.create(
            middle_name=middle_name,
            mobile_number=mobile,
            user_name=user_name
        )
        user_meta_data_data = validated_data.get('user_meta_data')
        user_meta_data = UserMetaData.objects.create(**user_meta_data_data)
        user_personal_details_data = validated_data.get('user_personal_details')
        # print(user_personal_details_data)
        user_personal_details = UserPersonalDetails.objects.create(**user_personal_details_data)
        verification_details_data = validated_data.get('verification_details')
        verification_details = VerificationDetails.objects.create(**verification_details_data)
        profile_pic_data = validated_data.get('profile_pic')
        profile_pic = ProfilePic.objects.create(**profile_pic_data)
        basic_address_data = validated_data.get('basic_address')
        basic_address = BasicAddress.objects.create(**basic_address_data)
        # print(basic_address_data)
        app = IdeateApp.objects.get(pk=app_id)
        user_all_data = UserAllData.objects.create(
            user = user,
            user_meta_data=user_meta_data,
            user_basic_details=user_basic_details,
            user_personal_details=user_personal_details,
            verification_details=verification_details,
            profile_pic=profile_pic,
            basic_address=basic_address,
            app=app
        )
        return UserManagementSerializerHelper(**validated_data)

    # class Meta:
    #     model = UserAllData
    #     fields = '__all__'
    #     # []
    #     read_only_fields = ('id',)
