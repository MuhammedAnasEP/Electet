from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from home.models import Products, Cart, Orders
# import joblib

# from Cython.Build import cythonize


# Create your views here.

def home(request):
    if request.user.is_authenticated:

        new_product = Products.objects.all().order_by('-id')[:10]
        all_product = Products.objects.all()
        cart = Cart.objects.filter(user_id = request.user.id)
        cart_count = len(cart)
        # recommended_products = generate_product_recommendations(request.user)
        # print(recommended_products)
        context = {
            'new_product' : new_product,
            'all_product' : all_product,
            'cart_count' : cart_count,
            # 'recommantaion' : recommended_products,
        }
        return render(request, 'home.html', context)
    else:
        return redirect(signin)

def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
        
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        
        if password == confirm_password:
            if User.objects.filter(username = user_name).exists():
                messages.info(request,"Username already exisst!")
                return redirect(signup)

            if User.objects.filter(email = email).exists():
                messages.info(request,"Email already exists!")
                return redirect(signup)

            user = User.objects.create_user(first_name = first_name, last_name = last_name, username = user_name, email = email, password = password)
            user.save()
            return redirect(home)

        messages.info(request, "Password is not matching!")

    return render(request, "signup.html")

def signin(request):
    if request.user.is_authenticated:
        return redirect(home)
        
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        print(user_name,password)
        user = auth.authenticate(username=user_name, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            messages.info(request, "Invalid Credentials!")
            return redirect(signin)
    else:
        return render(request, "login.html")

def signout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect(home)

def add_to_cart(request, pid):
    user = User.objects.get(id = request.user.id)
    product = Products.objects.get(id = pid)
    cart_item = Cart.objects.create(user = user, product = product)
    return redirect(home)

def view_cart(request):
    cart_items = Cart.objects.filter(user_id = request.user.id)
    cart_count = len(cart_items)
    total_price = 0
    for items in cart_items:
        total_price += items.product.price
    context = {
        'cart_items' : cart_items,
        'cart_count' : cart_count,
        'total' : total_price,
    }

    return render(request, 'cart.html', context)

def delete_cart_item(request, id):
    item = Cart.objects.get(id = id)
    item.delete()
    return redirect(view_cart)

def order(request):
    if request.method == "POST":
        items = Cart.objects.filter(user_id = request.user.id)
        name = request.POST['name']
        address = request.POST['address']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        phone = request.POST['phone']
        orders = []
        for item in items:
            order = Orders(
                name=name,
                address=address,
                city=city,
                district=district,
                state=state,
                pincode=pincode,
                phone=phone,
                user=request.user,
                product=item.product,
                price=item.product.price,
                pname=item.product.name,
            )
            orders.append(order)
        Orders.objects.bulk_create(orders)
        for item in items:
            item.product.stock -= 1
            item.product.save()

        items.delete()

        messages.info(request, "Your Items Prchased succesfully")
        return redirect(home)

# def generate_product_recommendations(user):

#     model = joblib.load('products_recommendation_model.joblib')
#     user_interaction_history = user.products_recommendations.all()
#     recommended_products = model.predict(user_interaction_history)

#     return recommended_products
