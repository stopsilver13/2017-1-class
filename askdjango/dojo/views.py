from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import json

# Create your views here.
def json_response(request) :
    data = {
        'message' : '안녕, 파이썬, 장고',
        'items' : ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
    }
    # 방법1
    #json_string = json.dumps(data, ensure_ascii=False)
    #return HttpResponse(json_string, content_type='application/json')
    # 방법2
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False}) # ensure_ascii가 참이면 유니코드 값으로 보임

def image_download(request) :
    filepath = os.path.join(settings.BASE_DIR, 'yagudjango_team.jpg')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='img/png')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

def image_download_write_title(request) :
    filepath = os.path.join(settings.BASE_DIR, 'yagudjango_team.jpg')
    filename = os.path.basename(filepath)

    img = Image.open(filepath)
    draw = ImageDraw.Draw(img)
    fontpath = os.path.join(settings.BASE_DIR, 'a고딕13.ttf')
    font = ImageFont.truetype(fontpath, 30)
    draw.text((10, 10), filename, (255,255,255), font=font)

    new_filepath = os.path.join(settings.BASE_DIR, '{}_edit.jpg'.format(filename))
    img.save(new_filepath)

    with open(new_filepath, 'rb') as f:
        response = HttpResponse(f, content_type='img/png')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

def mysum(request, x) :
    x = x.split('/')
    mysum = 0

    for num in x :
        if num != '':
            mysum += int(num)

    return HttpResponse(mysum)


def hello(request, name, age) :
    return HttpResponse('안녕하세요. {}. {}살이시네요.'.format(name, age))