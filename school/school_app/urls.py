from django.urls import path
from .views import *
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index,name="index"),
    path('test',test_view,name="test"),
    path('gallery',gallery,name="gallery"),
    path('admission',admission,name="admission"),
    path('teachers',teachers,name="teachers"),
    path('fee_structure',fee_structure,name="fee_structure"),
    path('tc_certi',tc_certi,name="tc_certi"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('admission_form',admission_form,name="admission_form"),
    path('infrastructure',infrastructure,name="infrastructure"),
    path('mandatory_disclosure',mandatory_disclosure,name="mandatory_disclosure"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   