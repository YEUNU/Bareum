from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
import requests
import json
from django.views import View

# Create your views here.

def login(req):
    login_id = req.GET.get('userLoginid')
    password = req.GET.get('password')
    # 로그인 실패 조건을 확인하고, 실패한 경우 PermissionDenied 예외를 발생시킵니다.
    # if 로그인_실패_조건:
        # raise PermissionDenied("Login failed")
    
    # 로그인 성공 처리
    # ...
    
    return HttpResponse("Login successful")

def signup(req):
    login_id = req.POST.get('userLoginid')
    password = req.POST.get('password')
    user_name = req.POST.get('userName')
    
    #회원가입 로직
    
    #가입후에 정보 다시 리턴
    return ...
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
@method_decorator(csrf_exempt, name='dispatch')
class KakaoLogin(View):

    def dispatch(self, request, *args, **kwargs):
        return super(KakaoLogin, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        try:
            data = json.loads(request.body)
        except:
            ...
        access_token = data['access_token']
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        response = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
        user_data = response.json()
        print(user_data)
        # 이미 가입한 회원인지 확인후
        # 기존사용자가 아니면 새 사용자로 생성하고
        # 로그인로직실행 하면될듯
        return JsonResponse({"message": "success"})