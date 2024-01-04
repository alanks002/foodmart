
from django.urls import path
from frontend import views

urlpatterns=[
    path('home_view/',views.home_view,name="home_view"),
    path('home_shop/<catname>/',views.home_shop,name="home_shop"),
    path('home_about/',views.home_about,name="home_about"),
    path('home_blog/',views.home_blog,name="home_blog"),
    path('home_contact/',views.home_contact,name="home_contact"),
    path('contact_post/',views.contact_post,name="contact_post"),
    path('product_single/<int:s_id>/',views.product_single,name="product_single"),

    path('user_login/',views.user_login,name="user_login"),
    path('user_sigin_in_post/',views.user_sigin_in_post,name="user_sigin_in_post"),
    path('user_sigin_up/',views.user_sigin_up,name="user_sigin_up"),
    path('userlogout', views.userlogout, name="userlogout"),

    path('cart_post/', views.cart_post, name="cart_post"),
    path('cart_view/',views.cart_view,name="cart_view"),

    path('Checkout_view/',views.Checkout_view,name="Checkout_view"),
    path('CheckoutDBsave/',views.CheckoutDBsave,name="CheckoutDBsave"),






]
