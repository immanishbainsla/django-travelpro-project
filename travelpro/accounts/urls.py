from . import views
from django.urls import path
from travelpro import views as travelpro_views

app_name = 'accounts'

urlpatterns = [
    path('', travelpro_views.IndexView.as_view(), name='index'),
]
