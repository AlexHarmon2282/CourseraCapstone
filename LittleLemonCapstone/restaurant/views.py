from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from . import models
from . import serializers
from rest_framework.decorators import api_view

def index(request):
 return render(request, 'index.html', {})

class bookingView(APIView):
    def get(self, request):
        items = models.booking.objects.all()
        serializer = serializers.BookingSerializer(items, many = True)
        return Response(serializer.data)
    

class MenuItemView(ListCreateAPIView):
    #queryset = models.Menu.objects.all()
    #serializer_class = serializers.MenuItemSerializer

    def post(self, request):
        serializer = serializers.MenuItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data": serializer.data})
        
    def get(self, request):
        pass            #FIX LATER

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    #queryset = models.Menu.objects.all()
    #serializer_class = serializers.MenuItemSerializer
    
    def get(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass