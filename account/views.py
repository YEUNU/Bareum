from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied

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

def login_kakao(req):
    access_token = req.POST.get('access_token')
    user_info_url = "https://kapi.kakao.com/v2/user/me"
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = req.get(user_info_url, headers=headers)
    user_info = response.json()
    return JsonResponse({"result":"success","user_info":user_info})

def signup(req):
    ...