from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
import requests
import json
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.http import HttpResponse
from .models import User, ProfileImage, Address
from .serializer import ProfileSerializer, UserAddInfoSerializer, AddressSerializer
from django.core.exceptions import ObjectDoesNotExist
import logging
import traceback

class UserAddInfoView(APIView):

    def put(self, request, member_id):
        data = json.loads(request.body)
        try:
            user = User.objects.get(pk=member_id)
            user.nickname = data['nickname']
            user.birthday = data['birthday']
            user.height = data['height']
            user.weight = data['weight']
            user.gender = data['gender']
            user.save()
            return Response({'message': 'User updated successfully'}, status=200)
        except ObjectDoesNotExist:
            return Response({'message': 'User does not exist'}, status=404)
        except KeyError:
            return Response({'message': 'Invalid parameters'}, status=400)
        except Exception as e:
            print(traceback.format_exc())  # 예외 정보를 추적 및 출력합니다.
            return Response({'message': 'Something went wrong'}, status=500)
    def get(self, request, member_id):
        try:
            user = User.objects.get(pk=member_id)
            user_data = {
                'nickname': user.nickname,
                'birthday': user.birthday,
                'height': user.height,
                'weight': user.weight,
                'gender': user.gender
            }
            return Response(user_data, status=200)
        except ObjectDoesNotExist:
            return Response({'message': 'User does not exist'}, status=404)
        except:
            return Response({'message': 'Something went wrong'}, status=500)
        
    
# Create your views here.

@csrf_exempt
def login_user(req):
    if req.method == 'POST':
        data = json.loads(req.body)
        login_id = data.get('userLoginid')
        password = data.get('password')
        print(login_id, password)
        
        #사용자 인증
        user = authenticate(login_id=login_id, password=password)
        print(user)
        if user is not None:
            login(req, user)
            csrf_token = get_token(req)
            img_url = ProfileSerializer.get_profile_image_url(user=user)
            
            response = JsonResponse({'success': '로그인이 완료되었습니다.',
                                     'login_id': login_id, 
                                     'username': user.user_name,
                                     'member_id': user.member_id,
                                     'profile_img_url':img_url
                                     })
            response["Token"] = csrf_token
            return response
        else:
            return JsonResponse({'error': '로그인에 실패했습니다.'}, status=400)
        
    else:
        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    
def logout_user(req):
    logout(req)
    return JsonResponse({'success': '로그아웃이 완료되었습니다.'})

@csrf_exempt
def signup(req):

    if req.method == 'POST':

        data = json.loads(req.body.decode('utf-8'))

        login_id = data.get('userLoginid')

        password = data.get('password')

        user_name = data.get('userName')

        print(login_id, password, user_name)

       

        if models.User.objects.filter(login_id = login_id).exists():

            return JsonResponse({'result':'fail'})

       

        user = models.User.objects.create_user(login_id = login_id,

                                               password = password,

                                               user_name = user_name)

       

        return JsonResponse({'login id':login_id, 'user_nickname':user_name,

                             'result': 'success',

                             'message': '회원가입이 완료되었습니다.'})

    else:

        return JsonResponse({'error': '잘못된 요청입니다.'}, status=400)
    
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
        user_id = str(user_data['id'])
        email = user_data['kakao_account']['email']
        name = user_data['properties']['nickname']
        if models.User.objects.filter(login_id = email).exists():
            user = authenticate(login_id=email, password=user_id)
            login(request, user)
        else:
            user = models.User.objects.create_user(login_id = email,
                                       password = user_id,
                                       user_name = name,
                                       email=email)
            user = authenticate(login_id=email, password=user_id)
            login(request, user)
            
        response = JsonResponse({'success': '로그인이 완료되었습니다.',
                     'login id': email, 
                     'username': user.user_name,
                     'member_id': user.member_id
                     })
            
        return response

@login_required
def check_session(request):
    print(request)
    #로그인 안되있으면 302 리턴
    return JsonResponse({"logged_in": True})

class UserProfileImageView(APIView):
    def post(self, request, member_id):
        try:
            user = User.objects.get(pk=member_id)
            if len(request.FILES) > 0:
                image_file = request.FILES['image']
                # 프로필 이미지가 이미 존재하는 경우에는 해당 이미지를 먼저 삭제
                try:
                    existing_image = ProfileImage.objects.get(user=user)
                    default_storage.delete(existing_image.image.path)
                    image = existing_image
                except ProfileImage.DoesNotExist:
                    image = ProfileImage()
                image.image = default_storage.save(
                    "profile_images/%s" % (image_file.name,),
                    image_file
                )
                image.user = user
                image.save()

        except User.DoesNotExist:
            return Response({"error": "회원이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        return Response({}, status=status.HTTP_201_CREATED)
    
    
    
    


class UserAddressView(View):
    def get(self, request, member_id):
        user = User.objects.get(pk=member_id)
        if user.is_authenticated:
            try:
                address = Address.objects.get(user=user)
                serializer = AddressSerializer(address)
                return JsonResponse(serializer.data, safe=False)
            except Address.DoesNotExist:
                return JsonResponse({
                    "postcode": "",
                    "address": "",
                    "extra_address": "",
                    "detailed_address": ""
                }, safe=False)
        else:
            return JsonResponse({"error": "Not authenticated"}, status=401)
        
    def post(self, request, member_id):
        user = User.objects.get(pk=member_id)
        if user.is_authenticated:
            data = JSONParser().parse(request)
            data["user"] = user.pk

            try:
                # 해당 사용자가 이미 주소를 가지고 있다면 기존 주소를 업데이트 합니다.
                existing_address = Address.objects.get(user=user)
                serializer = AddressSerializer(existing_address, data=data)
            except Address.DoesNotExist:
                # 해당 사용자의 주소가 없다면 새로운 주소를 생성합니다.
                serializer = AddressSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"success": True})
            else:
                return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse({"error": "Not authenticated"}, status=401)
        
        
def user_remove(request, member_id):
    # 삭제하고자 하는 유저 정보를 가져온다.
    user = get_object_or_404(User, pk=member_id)

    # 유저 프로필 이미지를 삭제한다.
    try:
        profile = get_object_or_404(ProfileImage, user=user)
        default_storage.delete(profile.image.path)
        profile.delete()
    except ProfileImage.DoesNotExist:
        pass

    # 유저 주소 정보를 삭제한다.
    try:
        address = get_object_or_404(Address, user=user)
        address.delete()
    except Address.DoesNotExist:
        pass

    # 유저를 삭제한다.
    user.delete()

    # 삭제 후 결과를 리턴한다.
    return HttpResponse("User has been removed")