from django.urls import path
from . import views

app_name = 'uploads'
urlpatterns = [
    path('/<int:dataset_id>/', views.prepocessing, name='prepocessing'),
    # path('hasil-test/', views.logic_predict, name='logic_predict'),
]