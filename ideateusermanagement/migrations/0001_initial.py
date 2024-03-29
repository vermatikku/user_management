# Generated by Django 3.1.7 on 2021-03-11 19:59

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ideateusermanagement.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('is_primary', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
                ('address_line_1', models.TextField(blank=True)),
                ('address_line_2', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('district', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('a_state', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('pincode', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('country', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IdeateApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to=ideateusermanagement.models.profile_pic_path)),
            ],
        ),
        migrations.CreateModel(
            name='UserBasicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_name', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('mobile_number', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('user_name', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('dob', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VerificationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_verified', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
                ('mail_verified', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
                ('profile_verified', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='UserMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date_time', models.DateTimeField(default=datetime.datetime.now)),
                ('active', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserAllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.ideateapp')),
                ('basic_address', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.basicaddress')),
                ('profile_pic', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.profilepic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_basic_details', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.userbasicdetails')),
                ('user_meta_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.usermetadata')),
                ('user_personal_details', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.userpersonaldetails')),
                ('verification_details', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ideateusermanagement.verificationdetails')),
            ],
        ),
    ]
