from django.urls import path
from testapp import views

urlpatterns=[
    path('', views.home,name='home'),
    path('cart/', views.cart,name='cart'),
    path('checkout/', views.checkout,name='checkout'),
    path('logout/', views.logoutpage,name='logout'),
    path('login/', views.loginpage,name='login'),
    path('view/<int:id>', views.product_view,name='productView'),
    path('addtocart/<int:id>', views.addtocart,name='addtocart'),
    path('about/', views.about,name='about'),
    path('addProduct/', views.add_product,name='add_product'),
    path('delete_orderitem/<int:id>', views.delete_orderitem,name='delete_orderitem'),
    ]
