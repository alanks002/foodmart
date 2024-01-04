from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from newapp.models import fooddb, prodb
from frontend.models import contactdb,singinupdb

from django.contrib import messages


# Create your views here.
def main_view(request):
    return render(request,'index.html')
def second_view(request):

    return render(request,'intro.html')



def post_sec(request):
    if request.method=="POST":
        a=request.POST.get("Name")
        b = request.POST.get("Description")
        c = request.FILES["Profile"]
        obj=fooddb(Name=a,Description=b,Profile=c)
        obj.save()
        messages.success(request,"category saved successfully")
        return redirect(second_view)

def food_table(request):
    data=fooddb.objects.all()
    return render(request,'food_table.html',{"data":data})

def food_edit(request,f_id):

   fdata=fooddb.objects.get(id=f_id)
   return render(request,'food_edit.html',{"fdata":fdata})

def food_delete(request, f_id):
    data = fooddb.objects.filter(id=f_id)
    data.delete()
    return redirect(food_table)

def food_update(request, f_id):
    if request.method == "POST":
        a = request.POST.get("Name")
        b = request.POST.get("Description")

        try:
            img = request.FILES["Profile"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = fooddb.objects.get(id=f_id).Profile
        fooddb.objects.filter(id=f_id).update(Name=a,Description=b,Profile=file)
        return redirect(food_table)




def product_view(request):
    data = fooddb.objects.all()
    return render(request,'product.html',{"data":data})

def product_post(request):
    if request.method=="POST":
        a=request.POST.get("Product_Name")
        b = request.POST.get("Product_Category")
        c = request.POST.get("Price")
        d = request.POST.get("Description")
        e = request.FILES["Profile"]
        obj=prodb(Product_Name=a,Product_Category=b,Price=c,Description=d,Profile=e)
        obj.save()
        return redirect(product_view)

def product_table(request):
    data=prodb.objects.all()
    return render(request,'product_table.html',{"data":data})

def product_edit(request,n_id):
   data = fooddb.objects.all()
   pdata=prodb.objects.get(id=n_id)
   return render(request,'product_edit.html',{"pdata":pdata,"data":data})

def product_delete(request, n_id):
    pdata = prodb.objects.filter(id=n_id)
    pdata.delete()
    return redirect(product_table)

def product_update(request,n_id):
    if request.method == "POST":
        a = request.POST.get("Product_Name")
        b = request.POST.get("Product_Category")
        c = request.POST.get("Price")
        d = request.POST.get("Description")
        try:
            img = request.FILES["Profile"]
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = prodb.objects.get(id=n_id).Profile
        prodb.objects.filter(id=n_id).update(Product_Name=a, Product_Category=b,Price=c,Description=d,Profile=file)
        return redirect(product_table)


def login_view(request):
    return render(request,'login.html')

def login_post(request):
    if request.method=="POST":
        a=request.POST.get("username")
        b=request.POST.get("password")
        if User.objects.filter(username__contains=a).exists():
            x = authenticate(username=a, password=b)
            if x is not None:
                login(request, x)
                request.session['username'] = a
                request.session['password'] = b
                return redirect(main_view)
            else:
                return redirect(login_view)
        else:
            return redirect(login_view)


def logout_view(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_view)


def new_contact(request):
    data=contactdb.objects.all()
    return render(request,'new_page_contact.html',{"data":data})



def sigin_up_table(request):
    tdata=singinupdb.objects.all()
    return render(request,'sigin_up_table.html',{"tdata":tdata})

def sigin_up_delete(request, d_id):
    ddata = singinupdb.objects.filter(id=d_id)
    ddata.delete()
    return redirect(sigin_up_table)








