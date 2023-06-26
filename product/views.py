from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from rest_framework.views import APIView

# Create your views here.

class ProductDetailView(APIView):
    
    def get(self,request,nutra_id):
        ...
        