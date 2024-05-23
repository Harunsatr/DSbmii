from django.urls import path
from . import views


app_name = 'predict'
urlpatterns = [
    path('/<int:dataset_id>/', views.save_model, name='save_model'),
    # path('hasil-test/', views.logic_predict, name='logic_predict'),
]