from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('terms/', views.condition, name='conditions'),
	path('policy/', views.policy, name='policy'),
	path('print/', views.print, name='print'),
	path('job/', views.job, name='job'),
	path('preview/<int:pk>/', views.preview, name='preview'),
	path('update/<int:pk>/', views.updateDocument, name='update'),
	path('total/<int:pk>/', views.total, name='total'),
	path('done/', views.done, name='done'),
]