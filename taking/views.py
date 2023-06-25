from django.http import JsonResponse
from product.models import Nutraceuticals

def prSearch(request):
    search_query = request.GET.get('search', '')
    results = Nutraceuticals.objects.filter(nutraceuticals_name__icontains=search_query)
    response_data = []
    for result in results:
        response_data.append({
            'id': result.nutraceuticals_id,
            'nutraceuticals_name': result.nutraceuticals_name,
            # 여기에 필요한 나머지 필드를 추가하십시오.
        })
    return JsonResponse(response_data, safe=False)