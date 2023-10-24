from django.urls import path
from home import views

urlpatterns = [
    path("", views.home, name="homePage"),
    path("login", views.signin, name="loginPage"),
    path("signup", views.signup, name="signupPage"),
    path("signout", views.signout, name="signout"),
    path("cart", views.view_cart, name="viewCart"),
    path("add-to-cart/<int:pid>", views.add_to_cart, name="addToCart"),
    path("delelete-cart-item/<int:id>", views.delete_cart_item, name="deleteCartItem"),
    path("order", views.order, name="order"),
]