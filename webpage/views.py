from django.shortcuts import render
from rest_framework.views import APIView
from django.template import loader

class Main(APIView):
    def get(self, request):
        return render(request, 'index.html', {})

