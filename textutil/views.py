#created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyzeText(request):
    punctution = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    text = request.POST.get('text','')
    cb1 = request.POST.get('cb1', 'off')
    if len(text) == 0:
        return render(request, 'error.html')

    rlt = " "
    if cb1 == "on":
        for char in text:
            if char not in punctution:
                rlt = rlt + char
    if cb1 == "on":
        text = rlt

    cb2 = request.POST.get('cb2', 'off')
    if cb2 == "on":
        text = text.upper()

    cb3 = request.POST.get('cb3', 'off')
    if cb3 == "on":
        text = text.replace('\r', ' ')
        text = text.replace('\n', ' ')

    cb4 = request.POST.get('cb4', 'off')
    if cb4 == "on":
        text = " ".join(text.split())

    ans = {"result": text}
    return render(request,'p.html',ans)

