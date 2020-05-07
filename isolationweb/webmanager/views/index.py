from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, "index.html", {})
