from .models import Customer
from .serializers import CustomerSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

def customer_List(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(serializer.data)