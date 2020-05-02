
from django.shortcuts import render
import json


def get_context(type: str, rank: str) -> dict:

    with open('..\\data\\%s\\%s.json' % (type.upper(), rank.upper()), 'r', encoding='utf-8') as f:
        data_json = json.load(f)
        context = data_json.get('divisions')[0]

    return context
def index(request):

    if request.GET.get("type") and request.GET.get('rank'):

        type = request.GET.get("type")
        rank = request.GET.get('rank')
        context = get_context(type=type,rank=rank)
        return render(request, 'leaders.html', context=context)

    return render(request, 'index.html')
def comingsoon(request):

    return render(request, 'comingsoon.html')