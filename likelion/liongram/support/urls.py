from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('', views.FaqListView.as_view() ,name='index'), 
    path('edit/<int:pk>', views.FaqEditView.as_view() ,name='edit'), 
    path('create/', views.FaqCreateView.as_view() ,name='create'), 
    path('detail/<int:pk>', views.FaqDetailView.as_view() ,name='detail'), 

]

