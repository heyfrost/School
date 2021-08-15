from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
# Create your models here.


def content_file_name(instance,filename):
	ext="png"
	filename= str(instance.caption)+"."+str(ext)
	return os.path.join('images/',filename)

def student_im(instance,filename):
    ext="png"
    filename= str(instance.g_phone1)+"."+str(ext)
    return os.path.join('admission_form/',filename)

def content_tc(instance,filename):
	ext="png"
	filename= str(instance.caption)+"."+str(ext)
	return os.path.join('TC/',filename)

def content_file_name1(instance,filename):
	ext="png"
	filename= str(instance.name)+"."+str(ext)
	return os.path.join('images/',filename)

class Faculties(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField(default="")
    url_Facebook = models.URLField(default="")
    image = models.ImageField(upload_to=content_file_name1)
    # TODO
    # AUTOGENERATE DATETIME
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    def get_cname(self):
        class_name = "Faculty"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'faculties'
        verbose_name_plural = 'Faculties'


class Messages(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'messages'
        verbose_name_plural = 'Messages'
    def __self__(self):
        return self.name

class Notices(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'notices'
        verbose_name_plural = 'Notices'
    def __self__(self):
        return self.title

class TC_certi(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to=content_tc)
    # TODO
    # AUTOGENERATE DATETIME
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.caption

    def get_cname(self):
        class_name = "TC_certi"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'TC'
        verbose_name_plural = 'TC_Certificates'

class Fee_detail(models.Model):
    clas=models.CharField(max_length=10)
    add_fee = models.IntegerField(default=0)
    tution_fee = models.IntegerField(default=0)
    science_fee = models.IntegerField(default=0)
    comp_fee = models.IntegerField(default=0)
    dev_fee = models.IntegerField(default=0)
    smart_fee = models.IntegerField(default=0)
    exam_fee = models.IntegerField(default=0)
    total_fee = models.IntegerField(default=0)

    class Meta:
            managed = True
            db_table = 'Fee_detail'
            verbose_name_plural = 'Fee_details'

    def __str__(self):
            return self.clas

class Fee_detail_quarterly(models.Model):
    clas=models.CharField(max_length=5)
    first_quarter = models.IntegerField(default=0)
    second_quarter = models.IntegerField(default=0)
    third_quarter = models.IntegerField(default=0)
    fourth_quarter = models.IntegerField(default=0)
    total = models.IntegerField(default=0)


    class Meta:
        managed = True
        db_table = 'Fee_detail_quarterly'
        verbose_name_plural = 'Fee_details_quarterly'

    def __str__(self):
        return self.clas


class ImgCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name



class Pictures(models.Model):
    category = models.ForeignKey(
        ImgCategory, on_delete=models.SET_NULL, null=True, blank=True)
    caption = models.CharField(max_length=100)

    image = models.ImageField(upload_to=content_file_name)
    # TODO
    # AUTOGENERATE DATETIME
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.caption

    def get_cname(self):
        class_name = "Picture"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'pictures'
        verbose_name_plural = 'Pictures'



class Admission_form(models.Model):
    SEX = (
        ("M","Male"),
        ("F","Female")
    )
    BLOOD = (
        ("A","A"),
        ("B","B"),
        ("AB","AB"),
        ("O","O")
    )
    RELIGION = (
        ("Hindu","Hindu"),
        ("Muslim","Muslim"),
        ("Sikhs","Sikhs"),
        ("Christiian","Christiian")
    )
    CASTE = (
        ("ST","ST"),
        ("SC","SC"),
        ("OBC","OBC"),
        ("General","General")
    )
    serial_no = models.IntegerField(blank=True, null = True)
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100,choices = SEX)
    blood = models.CharField(max_length=100, choices = BLOOD)
    religion = models.CharField(max_length=100,choices = RELIGION )
    caste = models.CharField(max_length=100,choices = CASTE)
    g_phone1 = models.CharField(max_length=12)
    g_phone2 = models.CharField(max_length=12)
    g_name = models.CharField(max_length=100)
    g_email = models.EmailField(max_length=100,null = True,blank=True)
    g_profession = models.CharField(max_length=100)
    g_religion = models.CharField(max_length=100,choices = RELIGION)
    g_rel_with_guardion = models.CharField(max_length=100)
    g_caddress = models.TextField(max_length=100)
    g_paddress = models.TextField(max_length=100)
    c_email = models.EmailField(max_length=100,null = True,blank=True)
    c_phone = models.CharField(max_length=12)
    c_address = models.TextField(max_length=100)
    acad_class = models.CharField(max_length=100)
    aad_prev_school = models.CharField(max_length=100)
    acad_prev_class = models.CharField(max_length=100)
    student_image = models.ImageField(upload_to = student_im, null=True, blank=True)
    f_phone = models.CharField(max_length=12)
    f_name = models.CharField(max_length=100)
    f_email = models.EmailField(max_length=100,null = True,blank=True)
    f_profession = models.CharField(max_length=100)
    m_phone = models.CharField(max_length=12)
    m_name = models.CharField(max_length=100)
    m_email = models.EmailField(max_length=100,null = True,blank=True)
    m_profession = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class DocCategory(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name



class Disclosure(models.Model):
    category = models.ForeignKey(
        DocCategory, on_delete=models.SET_NULL, null=True, blank=True)
    caption = models.CharField(max_length=100)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    # TODO
    # AUTOGENERATE DATETIME


    def __str__(self):
        return self.caption

    def get_cname(self):
        class_name = "Disclosure"
        return class_name

    class Meta:
        managed = True
        ordering = ['-created_at']
        db_table = 'Disclosure'
        verbose_name_plural = 'Disclosures'


class General_Disclosure(models.Model):
    info = models.CharField(max_length=100, null=False)
    detail = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.info
