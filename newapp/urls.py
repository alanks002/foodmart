from django.urls import path
from newapp import views

urlpatterns = [
    path('main_view/',views.main_view,name="main_view"),


    path('second_view/',views.second_view,name="second_view"),
    path('post_sec/',views.post_sec,name="post_sec"),
    path('food_table/',views.food_table,name="food_table"),
    path('food_edit/<int:f_id>',views.food_edit,name="food_edit"),
    path('food_delete/<int:f_id>',views.food_delete,name="food_delete"),
    path('food_update/<int:f_id>',views.food_update,name="food_update"),




    path('product_view/',views.product_view,name="product_view"),
    path('product_post/',views.product_post,name="product_post"),
    path('product_table/',views.product_table,name="product_table"),
    path('product_edit/<int:n_id>',views.product_edit,name="product_edit"),
    path('product_delete/<int:n_id>',views.product_delete,name="product_delete"),
    path('product_update/<int:n_id>',views.product_update,name="product_update"),

    path('login_view/',views.login_view,name="login_view"),
    path('login_post/',views.login_post,name="login_post"),
    path('logout_view/',views.logout_view,name="logout_view"),


    path('new_contact/',views.new_contact,name="new_contact"),

    path('sigin_up_table',views.sigin_up_table,name="sigin_up_table"),
    path('sigin_up_delete/<int:d_id>',views.sigin_up_delete,name="sigin_up_delete"),
    path('sigin_up_delete/',views.sigin_up_delete,name="sigin_up_delete"),




]