from django.shortcuts import render, redirect

from frontend.models import contactdb, singinupdb, cartdb, CheckoutDB
from newapp.models import fooddb, prodb
from django.contrib import messages


# Create your views here.
def home_view(request):
    pro=prodb.objects.all()
    product=fooddb.objects.all()
    return render(request,'homepage.html',{"product":product,"pro":pro})


def home_shop(request, catname):
    product = fooddb.objects.all()
    x=prodb.objects.filter(Product_Category=catname)
    return render(request,'shop.html',{"x":x,"product":product})

def home_about(request):
    product=fooddb.objects.all()
    return render(request,'about.html',{"product":product})

def home_blog(request):
    product=fooddb.objects.all()
    return render(request,'blog.html',{"product":product})

def home_contact(request):
    product=fooddb.objects.all()
    return render(request,'contact.html',{"product":product})


def product_single(request, s_id):
    data = prodb.objects.get(id=s_id)
    return render(request,'product_single.html',{"data":data})

def contact_post(request):
    if request.method=="POST":
        a=request.POST.get("Name")
        b=request.POST.get("Email")
        c=request.POST.get("Subject")
        d=request.POST.get("Messege")
        obj=contactdb(Name=a,Email=b,Subject=c,Messege=d)
        obj.save()
        return redirect(home_contact)

def user_login(request):
    return render(request,'user_login_page.html')

def user_sigin_in_post(request):
    if request.method=="POST":
        a=request.POST.get("Username")
        b=request.POST.get("Email")
        c=request.POST.get("Password")
        obj=singinupdb(Username=a,Email=b,Password=c)
        obj.save()
        return redirect(user_login)

def user_sigin_up(request):
    if request.method=="POST":
        un=request.POST.get("name")
        pwd=request.POST.get("password")
        if singinupdb.objects.filter(Username=un,Password=pwd).exists():
            request.session["Username"]=un
            request.session["Password"]=pwd
            messages.success(request,"loged in sucessucfully")
            return redirect(home_view)
        else:
            messages.error(request, "wrong username or password ")
            return redirect(user_login)
    else:
        return redirect(user_login)

def userlogout(request):
    del request.session["Username"]
    del request.session["Password"]
    return redirect(user_login)

def cart_post(request):
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("product_name")
        c=request.POST.get("Quantity")
        d=request.POST.get("Price")
        e=request.POST.get("Total")
        obj=cartdb(name=a,product_Name=b,Quantity=c,Price=d,Total=e)
        obj.save()
        return redirect(home_view)

def cart_view(request):
    data=cartdb.objects.filter(name=request.session["Username"])
    return render(request,'cart.html',{"data":data})




def Checkout_view(request):
    categories = fooddb.objects.all()
    cart = cartdb.objects.filter(name=request.session["Username"])
    total_price = 0
    for i in cart:
        total_price = total_price + i.Total
    return render(request, 'Checkout.html', {'cart':cart, 'total_price':total_price, 'categories':categories})


def CheckoutDBsave(request):
    if request.method == "POST":
        nmfirst = request.POST.get('firstname')
        nmlast = request.POST.get('lastname')
        countr = request.POST.get('country')
        addr = request.POST.get('address')
        city1 = request.POST.get('city')
        pncode = request.POST.get('pincode')
        mob = request.POST.get('mobile')
        Em = request.POST.get('email')
        obj = CheckoutDB(firstnm=nmfirst, lastnm=nmlast, country=countr, address=addr, city=city1, pincode=pncode,
                         phone=mob, email=Em)
        obj.save()
        messages.success(request, "Order Placed Successfully")
        return redirect(Checkout_view)





