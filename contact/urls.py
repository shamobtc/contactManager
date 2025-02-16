from django.urls import path
from . import views
app_name = 'contact'

urlpatterns = [

	path('add/', views.add, name='add_contact'), 
	path('<int:pk>/', views.edit, name='edit_contact'),
	path('<int:pk>/delete/', views.delete, name='delete_contact'),

]