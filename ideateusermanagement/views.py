from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from ideateusermanagement.models import *
from ideateusermanagement.serializers import *
from .helper import UserManagementSerializerHelper
from rest_framework.decorators import action

# from ideateusermanagement.tests import UserManagementSerializer
# UserAltSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'PUT' or self.request.method == 'PATCH' :
            serializer_class = UserAltSerializer
        return serializer_class

class UserBasicDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserBasicDetails.objects.all()
    serializer_class = UserBasicDetailsSerializer

class UserMetaDataViewSet(viewsets.ModelViewSet):
    queryset = UserMetaData.objects.all()
    serializer_class = UserMetaDataSerializer

class UserPersonalDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserPersonalDetails.objects.all()
    serializer_class = UserPersonalDetailsSerializer

class VerificationDetailsViewSet(viewsets.ModelViewSet):
    queryset = VerificationDetails.objects.all()
    serializer_class = VerificationDetailsSerializer

class ProfilePicViewSet(viewsets.ModelViewSet):
    queryset = ProfilePic.objects.all()
    serializer_class = ProfilePicSerializer

class BasicAddressViewSet(viewsets.ModelViewSet):
    queryset = BasicAddress.objects.all()
    serializer_class = BasicAddressSerializer


# class UserViewSet(viewsets.ViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

#     def list(self, request):
#         # queryset = User.objects.all()
#         # serializer = UserSerializer(queryset, many=True)
#         return Response(self.serializer_class.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def create(self, request):
#         data = request.data
#         serializer = UserSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors , status=400)

#     def update(self, request, pk=None):
#         serializer = UserSerializer(queryset, many=True)

#     def partial_update(self, request, pk=None):
#         serializer = UserSerializer(queryset, many=True)

#     def destroy(self, request, pk=None):
#         instance = self.get_object(pk)
#         instance.delete()
#         return HttpResponse(status=204)



# class UserManagementViewSet(viewsets.ViewSet):

#     def list(self, request):
#         queryset = User.objects.all()
#         serializer = UserManagementSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = UserManagementSerializer(user)
#         return Response(serializer.data)

#     def create(self, request):
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         pass

#     def partial_update(self, request, pk=None):
#         pass

#     def destroy(self, request, pk=None):
#         pass


    # def get(self, request, id=None):
    #         if id:
    #             return self.retrieve(request, id)
    #         else:
    #             return self.list(request)

# app_id = serializers.IntegerField(required=True)
# first_name = serializers.CharField(max_length=50)
# middle_name = serializers.CharField(max_length=50,required=False)
# last_name = serializers.CharField(max_length=50,required=False)
# user_name = serializers.CharField(max_length=50)
# email = serializers.CharField(max_length=50)
# mobile = serializers.CharField(max_length=50)
# password = serializers.CharField(max_length=50)
# user_meta_data = UserMetaDataSerializer()
# user_personal_details = UserPersonalDetailsSerializer(required=False)
# verification_details = VerificationDetailsSerializer()
# profile_pic = ProfilePicSerializer(required=True)
# basic_address = BasicAddressSerializer(required=True)
# class user_all_data(object):
#     def __init__(self,**kwargs):
#         pass

class UserManagementViewSet(viewsets.ViewSet):
    serializer_class = UserManagementSerializer
    lookup_field = 'id'

    @action(detail=True, methods=["GET"])
    def users(self,request,id=None):
        return Response('List', status=200)

    def user_details(self,request,*args, **kwargs):
        user_id = int(kwargs['id'])
        target_id = int(kwargs['target_id'])
        return Response('Details', status=200)

    def user_details_patch():
        pass

    def user_details_put():
        pass
    
    
    # get_user_details
    # user_personal_details
    # verification_details
    # profile_pic
    # basic_address
    
    # @action(detail=True, methods=["GET"])
    def get_user_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_meta_data').get(pk=id)
        umd = user_all.user_meta_data
        sld = UserMetaDataSerializer(umd)
        return Response(sld.data, status=200)

    # @action(detail=True, methods=["PUT"])
    def put_user_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_meta_data').get(pk=id)
        umdpk = user_all.user_meta_data.pk
        umd = UserMetaData.objects.get(pk=umdpk)
        serializer = UserMetaDataSerializer(umd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["PATCH"])
    def patch_user_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_meta_data').get(pk=id)
        umdpk = user_all.user_meta_data.pk
        umd = UserMetaData.objects.get(pk=umdpk)
        serializer = UserMetaDataSerializer(umd, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CodeByAlok===============================================================================
      
   # @action(detail=True, methods=["GET"])
    def get_user_personal_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_personal_details').get(pk=id)
        umd = user_all.user_personal_details
        sld = UserPersonalDetailsSerializer(umd)
        return Response(sld.data, status=200)

     # @action(detail=True, methods=["PUT"])
    def put_user_personal_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_personal_details').get(pk=id)
        umdpk = user_all.user_personal_details.pk
        umd = UserPersonalDetails.objects.get(pk=umdpk)
        serializer = UserPersonalDetailsSerializer(umd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["PATCH"])
    def patch_user_personal_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('user_personal_details').get(pk=id)
        umdpk = user_all.user_personal_details.pk
        umd = UserPersonalDetails.objects.get(pk=umdpk)
        serializer = UserPersonalDetailsSerializer(umd, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#==========================================================================================

   # @action(detail=True, methods=["GET"])
    def get_verification_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('verification_details').get(pk=id)
        umd = user_all.verification_details
        sld = VerificationDetailsSerializer(umd)
        return Response(sld.data, status=200)

    # @action(detail=True, methods=["PUT"])
    def put_verification_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('verification_details').get(pk=id)
        umdpk = user_all.verification_details.pk
        umd = VerificationDetails.objects.get(pk=umdpk)
        serializer = VerificationDetailsSerializer(umd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["PATCH"])
    def patch_verification_details(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('verification_details').get(pk=id)
        umdpk = user_all.verification_details.pk
        umd = VerificationDetails.objects.get(pk=umdpk)
        serializer = VerificationDetailsSerializer(umd, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#==========================================================================================

   # @action(detail=True, methods=["GET"])
    def get_profile_pic(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('profile_pic').get(pk=id)
        umd = user_all.profile_pic
        sld = ProfilePicSerializer(umd)
        return Response(sld.data,status=200)

    # @action(detail=True, methods=["PUT"])
    def put_profile_pic(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('profile_pic').get(pk=id)
        umdpk = user_all.profile_pic.pk
        umd = ProfilePic.objects.get(pk=umdpk)
        serializer = ProfilePicSerializer(umd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["PATCH"])
    def patch_profile_pic(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('profile_pic').get(pk=id)
        umdpk = user_all.profile_pic.pk
        umd = ProfilePic.objects.get(pk=umdpk)
        serializer = ProfilePicSerializer(umd, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#==========================================================================================

   # @action(detail=True, methods=["GET"])
    def get_basic_address(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('basic_address').get(pk=id)
        umd = user_all.basic_address
        sld = BasicAddressSerializer(umd)
        return Response(sld.data,status=200)

    # @action(detail=True, methods=["PUT"])
    def put_basic_address(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('basic_address').get(pk=id)
        umdpk = user_all.basic_address.pk
        umd = BasicAddress.objects.get(pk=umdpk)
        serializer = BasicAddressSerializer(umd, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=["PATCH"])
    def patch_basic_address(self,request,*args, **kwargs):
        id = int(kwargs['id'])
        user_all = UserAllData.objects.select_related('basic_address').get(pk=id)
        umdpk = user_all.basic_address.pk
        umd = BasicAddress.objects.get(pk=umdpk)
        serializer = BasicAddressSerializer(umd, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#======================END=================END================END=========================

    def list(self, request):
        user_all = UserAllData.objects.all().select_related()
        user_all_data = []
        for user_data in user_all:
            app_id = user_data.app.pk
            first_name = user_data.user.first_name
            middle_name = user_data.user_basic_details.middle_name
            last_name = user_data.user.last_name
            username = user_data.user.username
            user_name = user_data.user_basic_details.user_name
            email = user_data.user.email
            mobile = user_data.user_basic_details.mobile_number
            password = user_data.user.password
            user_meta_data = user_data.user_meta_data
            user_personal_details = user_data.user_personal_details
            verification_details = user_data.verification_details
            profile_pic = user_data.profile_pic
            basic_address = user_data.basic_address
            user_all_data.append(UserManagementSerializerHelper(app_id=app_id,first_name=first_name,middle_name=middle_name,
                last_name=last_name,username=username,user_name=user_name,email=email,mobile=mobile,
                password=password,user_meta_data=user_meta_data,user_personal_details=user_personal_details,
                verification_details=verification_details,profile_pic=profile_pic,basic_address=basic_address))
        serializer = UserManagementSerializer(user_all_data, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserManagementSerializer(data=request.data,)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.save())
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, id=None):
        # print('some one called me ')
        user_all = UserAllData.objects.all().select_related()
        user_data = get_object_or_404(user_all,user__id=id)
        app_id = user_data.app.pk
        first_name = user_data.user.first_name
        middle_name = user_data.user_basic_details.middle_name
        last_name = user_data.user.last_name
        username = user_data.user.username
        user_name = user_data.user_basic_details.user_name
        email = user_data.user.email
        mobile = user_data.user_basic_details.mobile_number
        password = user_data.user.password
        user_meta_data = user_data.user_meta_data
        user_personal_details = user_data.user_personal_details
        verification_details = user_data.verification_details
        profile_pic = user_data.profile_pic
        basic_address = user_data.basic_address
        user_data_s = UserManagementSerializerHelper(app_id=app_id,first_name=first_name,middle_name=middle_name,
                last_name=last_name,username=username,user_name=user_name,email=email,mobile=mobile,
                password=password,user_meta_data=user_meta_data,user_personal_details=user_personal_details,
                verification_details=verification_details,profile_pic=profile_pic,basic_address=basic_address)
        serializer = UserManagementSerializer(user_data_s)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass
