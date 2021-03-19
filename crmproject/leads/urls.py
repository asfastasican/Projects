from django.urls import path
from . import views
from .views import LeadCreate

urlpatterns = [
    path('list/', views.lead_list,name='lead-list'),
    path('detail/<int:pk>/',views.lead_detail),
    path('create/',LeadCreate.as_view(),name='create'),
    path('update/<int:id>',views.lead_update),
    path('delete/<int:id>',views.lead_delete),
]
