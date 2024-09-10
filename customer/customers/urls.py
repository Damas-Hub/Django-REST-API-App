from django.urls import path
from . import views

urlpatterns = [
    path('', views.customers_List),
    path('<int:pk>', views.customer_details)

]
