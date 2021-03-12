class UserManagementSerializerHelper:
    def __init__(self,app_id,first_name,last_name,
                user_name,email,mobile,password,
                user_meta_data,user_personal_details,verification_details,
                profile_pic,basic_address,username,middle_name=None):
        self.app_id=app_id
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.user_name=user_name
        self.email=email
        self.mobile=mobile
        self.password=password
        self.user_meta_data=user_meta_data
        self.user_personal_details=user_personal_details
        self.verification_details=verification_details
        self.profile_pic=profile_pic
        self.basic_address=basic_address
        self.username=username

