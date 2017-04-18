from django.shortcuts import render, redirect, HttpResponse
def index(request):
    return render(request, "index/index.html")

def progress(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    req = request.session
    req['name']= request.POST['name']
    req['location']= request.POST['location']
    req['language']= request.POST['language']
    req['comment'] =request.POST['comment']
    request.session['count'] += 1
    print request.session['count']
    return render(request, 'index/result.html')

# Create your views here.
