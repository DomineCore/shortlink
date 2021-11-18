from django.http.response import HttpResponse
from django.shortcuts import redirect
from short_link.models import Links

def redirect_link(request,link):
    if link is None:
        return redirect(request,'/')
    success, msg = Links.objects.get_url(link)
    if not success:
        return HttpResponse(msg)
    return redirect(msg)
