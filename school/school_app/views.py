from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, redirect,get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    faculties=Faculties.objects.all()
    notices=Notices.objects.all()
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'notices': notices, 'faculties': faculties, 'form':form}
    return render(request, 'index.html', args)

def admission(request):
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admission')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form}
    return render(request, 'admission.html', args)


def teachers(request):
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('teachers')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form}
    return render(request, 'teachers.html', args)

def infrastructure(request):
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('infrastructure')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form}
    return render(request, 'infrastructure.html', args)


def fee_structure(request):
    fees = Fee_detail.objects.all()
    fqq = Fee_detail_quarterly.objects.all()
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('fee_structure')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form,'fees':fees,'fqq':fqq}
    return render(request, 'fee_structure.html', args)



def tc_certi(request):
    pictures= TC_certi.objects.all()
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('tc_certi')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form,'pictures':pictures}
    return render(request, 'tc_certi.html', args)
def about(request):
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('about')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form}
    return render(request, 'about.html', args)

def contact(request):
    form = Messageform(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'form':form}
    return render(request, 'contact.html', args)

def gallery(request):
    category = request.GET.get('category')
    if category == None:
        pictures = Pictures.objects.all()
    else:
        pictures = Pictures.objects.filter(category__name = category)
    form = Messageform(request.POST or None)
    categories = ImgCategory.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('gallery')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'pictures': pictures,'form':form,'categories':categories }
    return render(request, 'gallery.html', args)

def admission_form(request):

    aform = AdmissionForm(request.POST or None, request.FILES or None,)
    if request.method == 'POST':
        if aform.is_valid():
            aform.save()
            return redirect('admission_form')
        else:
            return HttpResponse("Invalid Credentials")
    args = {'aform':aform,}
    return render(request,'admission_form.html',args)

def mandatory_disclosure(request):
    category = DocCategory.objects.all()
    dict=[]
    for cat in category:
        item=Disclosure.objects.filter(category=cat)
        dict.append((cat,item))
    generalDis = General_Disclosure.objects.all()
    args = {'dict':dict,'gd':generalDis}
    return render(request,'mandatory_disclosure.html',args)
