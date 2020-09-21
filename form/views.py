from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
import json
from .models import Info
from .filter import *
import base64
from .serializers import *

def index(request):
    id = request.GET.get('id', 0)

    if check_sqli(str(id)):
        return render(request, 'form/index.html', {'message': 'Do not try to hack meeee (づ￣ ³￣)づ'})

    query = 'SELECT * FROM form_info where id = ' + str(id)
    try:
        info_list = Info.objects.raw(query)
        tmp = len(info_list)
    except:
        return render(request, 'form/index.html', {})

    if len(info_list) < 1:
        return render(request, 'form/index.html', {})

    for info in info_list:
        if info.location:
            info.location = base64.b64encode(bytes(info.location, encoding='utf-8'))

    data = InfoSerializer(info_list, many=True).data
    return JsonResponse(data, safe=False)

def key(request):
    return render(request, 'form/key.html', {})
