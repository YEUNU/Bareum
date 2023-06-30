from django.shortcuts import render
from rest_framework.views import APIView
from .models import ShoppingCart
from .serializers import CartSerializer
from rest_framework.response import Response
from rest_framework import status
from product.models import Nutraceuticals
import json
class CartView(APIView):
    
    def get(self,request):
        user = request.user
        try:
            cart = ShoppingCart.objects.filter(user=user)
            if not cart.exists(): # 만약 장바구니에 아이템이 없으면 None을 돌려줍니다.
                 return Response(None)
        except Exception as e:    
            return Response(e,status=status.HTTP_400_BAD_REQUEST)
        serializer = CartSerializer(cart,many=True)
        
        return Response(serializer.data,status=status.HTTP_200_OK)
        
    
    def post(self,request):
        user = request.user
        try:
            nutra = Nutraceuticals.objects.get(업체별_제품코드 = request.data['product_code'])
            cart = ShoppingCart(
                user = user,
                product = nutra,
                quantity = request.data['quantity'],
            )
            cart.save()
            return Response(status=status.HTTP_201_CREATED)
        except Nutraceuticals.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        try:
            cart = ShoppingCart.objects.get(pk=request.query_params['cartId'])
            cart.delete()
            return Response({"message": "장바구니에서 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT)
        except ShoppingCart.DoesNotExist:
            return Response({"error": "장바구니가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        try:
            data = json.loads(request.body)
            cartId = data.get('cartId')
            quantity = data.get('quantity')

            # 장바구니에 있는 상품을 가져옵니다.
            cart = ShoppingCart.objects.get(pk=int(cartId))

            # 상품 수량을 업데이트합니다.
            cart.quantity = int(quantity)
            cart.save()

            return Response({"message": "장바구니 상품 수량이 업데이트되었습니다."}, status=status.HTTP_200_OK)
        except ShoppingCart.DoesNotExist:
            return Response({"error": "장바구니가 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"장바구니 상품 수량 업데이트 중 오류가 발생했습니다. {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class paymentView(APIView):
    
    def post():
        ...