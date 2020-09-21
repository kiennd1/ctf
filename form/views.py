from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from .models import Info
from .filter import *
from .serializers import *
import os
from .AES import *

def index(request):
    id = request.GET.get('id', 0)

    if check_sqli(str(id)):
        return render(request, 'form/index.html', {'message': 'Do not try to hack meeee (づ￣ ³￣)づ'})

    try:
        query = 'SELECT * FROM form_info where id = ' + str(id)
        info_list = Info.objects.raw(query)
        if len(info_list) < 1:
            return render(request, 'form/index.html', {})

        for info in info_list:
            if info.location:
                info.location = encrypt(request, info.location)
        data = InfoSerializer(info_list, many=True).data
    except:
        return render(request, 'form/index.html', {})

    return JsonResponse(data, safe=False)

def key(request, path):
    if check_path(path):
        return render(request, 'form/index.html', {'message': 'Do not try to hack meeee (づ￣ ³￣)づ'})

    if os.path.isdir(path):
        data = os.listdir('./' + path)
        return JsonResponse(data, safe=False)
    elif os.path.isfile(path):
        if 'db.sqlite3' in path:
            return render(request, 'form/index.html', {'message': 'Not easy like this (づ￣ ³￣)づ'})
        return FileResponse(open(path, 'rb'))
    else:
        return render(request, 'form/index.html', {})

def git(request):
    data = os.listdir('.git')
    return JsonResponse(data, safe=False)
