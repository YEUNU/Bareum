from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView
from .models import Nutraceuticals

# Create your views here.

class ProductDetailView(APIView):
    
    def get(self,request,nutra_id):
        product = Nutraceuticals.objects.get(pk=nutra_id)
        
        