from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Faculties)
class FacultyAdmin(admin.ModelAdmin):
    pass

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    pass

@admin.register(Notices)
class NoticeAdmin(admin.ModelAdmin):
    pass

@admin.register(Pictures)
class PictureAdmin(admin.ModelAdmin):
    pass

@admin.register(Fee_detail)
class Fee_detailAdmin(admin.ModelAdmin):
    pass

@admin.register(TC_certi)
class TC_certiAdmin(admin.ModelAdmin):
    pass

@admin.register(ImgCategory)
class ImgCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Fee_detail_quarterly)
class Fee_detail_quarterlyAdmin(admin.ModelAdmin):
    pass

@admin.register(Admission_form)
class Admission_formAdmin(admin.ModelAdmin):
    pass

@admin.register(DocCategory)
class DocCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Disclosure)
class DisclosureAdmin(admin.ModelAdmin):
    pass

@admin.register(General_Disclosure)
class General_DisclosureAdmin(admin.ModelAdmin):
    pass

@admin.register(Staff_Disclosure)
class Staff_DisclosureAdmin(admin.ModelAdmin):
    pass

@admin.register(School_Infra_Disclosure)
class School_Infra_DisclosureAdmin(admin.ModelAdmin):
    pass

@admin.register(MandatoryClassYear)
class MandatoryClassYearAdmin(admin.ModelAdmin):
    pass

@admin.register(MandatoryClassDetail)
class MandatoryClassDetailAdmin(admin.ModelAdmin):
    pass

@admin.register(IndexImage)
class IndexImageAdmin(admin.ModelAdmin):
    pass