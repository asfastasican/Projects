from django.urls import path
from . import views
from .views import AgentListView,AgentCreateView,AgentDetailView

urlpatterns = [
    path('Agentlist/', AgentListView.as_view(),name='agentlist'),
    path('CreateAgent/',AgentCreateView.as_view(),name='createagent'),
    path('AgentDetail/<int:pk>',AgentDetailView.as_view(),name='Agent-Detail'),
    #path('Agentupdate/<int:id>',views.lead_update),
    #path('Agentdelete/<int:id>',views.lead_delete),
]
