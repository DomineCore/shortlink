from django.http.response import JsonResponse
from short_link.models import Links

def build_links(request):
    url = request.GET.get('targeturl')
    if not url:
        return JsonResponse({
            "result":False,
            "message":"不可为空"
        })
    success, link = Links.objects.build_link(url)
    return JsonResponse({
        "result":success,
        "data":link
    })
