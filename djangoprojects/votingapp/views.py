from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
arr = ['Java', 'Python', 'Cplusplus', 'C', 'DotNET', 'JavaScript', 'PHP', 'Swift', 'SQL', 'Ruby', 'Delphi', 'Objective-C', 'Go', 'Assemblylanguage', 'VisualBasic', 'D', 'R', 'Perl', 'MATLAB']
globalcnt = {}

def index(request):
    mydictionary = {
        "arr" : arr
    }
    return render(request,'index.html',context=mydictionary)

def getquery(request):
    q = request.GET['languages']
    globalcnt[q] = globalcnt[q]+1 if q in globalcnt else 1
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)

def sortdata(request):
    global globalcnt
    globalcnt = dict(sorted(globalcnt.items(),key=lambda x:x[1],reverse=True))
    mydictionary = {
        "arr" : arr,
        "globalcnt" : globalcnt
    }
    return render(request,'index.html',context=mydictionary)