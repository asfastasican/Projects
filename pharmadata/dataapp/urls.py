from django.urls import path
from dataapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("login/",views.login,name="login"),
    path("product/",views.product_details,name="product"),
    path("add_product/",views.addproduct,name="addproduct"),
    path("delete_product/<int:id>",views.deleteproduct,name="deleteproduct"),
    path("productinfo/<int:id>",views.productinfo,name="productinfo"),
    path('doctordetails/', views.doctor_details,name="doctordetails"),
    path('medicaldetails/', views.medical_details,name="medicaldetails"),
    path('orgdetails/', views.org_details,name="orgdetails"),
    path('adddoctor/', views.adddoctor,name="adddoctor"),
    path('addmedical/', views.addmedical,name="addmedical"),
    path('addorg/', views.addorg,name="addorg"),
    path('doctorinfo/<int:id>', views.doctor_info),
    path('medicalinfo/<int:id>', views.medical_info),
    path('orginfo/<int:id>', views.org_info),
    path('deletedoctor/<int:id>', views.deletedoctor),
    path('deletemedical/<int:id>', views.deletemedical),
    path('deleteorg/<int:id>', views.deleteorg),
    path('stocks/', views.stocks,name="stocks"),
    path('addstocks/', views.add_stock,name="add_stock"),

]
