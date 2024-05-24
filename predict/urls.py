from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'predict'
urlpatterns = [
    path('/<int:dataset_id>/', views.save_model, name='save_model'),
    # path('hasil-test/', views.logic_predict, name='logic_predict'),
    path('hasil/', views.logic_predict, name='predict'),
    path('/predict/hasil/', views.logic_predict, name='logic_predict'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)