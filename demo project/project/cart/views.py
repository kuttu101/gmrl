from django.shortcuts import render, redirect
from .models import Product, CartItem, Feedback
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def product_list(request):
	products = Product.objects.all()
	return render(request, 'index.html', {'products': products})

def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def search(request):
    if request.method == 'POST':
        s=request.POST.get('search')
        if Product.objects.filter(name=s).exists():
           a = Product.objects.get(name=s)
           return render(request,'newadd1.html',{'products':a})
        else:
            return redirect(shop)
    else:
         return redirect(product_list)


def remove_from_cart(request, item_id):
	cart_item = CartItem.objects.get(id=item_id)
	cart_item.delete()
	return redirect(view_cart)



def shop(request):
	p=Product.objects.all()
	return render(request,'shop.html',{'products':p})

def whye(request):
    return render(request,'why.html')

def contactt(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message = request.POST.get('message')
        feedback = Feedback.objects.create(name=name,email=email,phone=phone,message=message)
        feedback.save()
    return render(request,'contact.html')

def testimonials(request):
    return render(request,'testimonial.html')


def feedback(request):
    f=Feedback.objects.all()
    return render(request,'feedback.html',{'feedback':f})



def signup(request):
    if request.method=='POST':
        username=request.POST.get('Name')
        email=request.POST.get('Email')
        password=request.POST.get('Password')
        confirmPassword=request.POST.get('ConfirmPassword')
        if password==confirmPassword:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username alreadt exists!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password)
                new_user.save()
                return redirect(user_logine)
        else:
            print('wrong password')
    return render(request,'signup.html')

def user_logine(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect(product_list)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_logine)
    return render(request,'login.html')  

def logoute(request):
    logout(request)
    return redirect(product_list)


def newadd(request,products_id):
	prod = Product.objects.get(id=products_id)
	return render(request,'newadd.html',{'products':prod})

def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect(view_cart)