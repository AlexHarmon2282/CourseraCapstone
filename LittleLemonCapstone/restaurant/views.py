from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
=======
>>>>>>> parent of 79bea59 (Setup serializers on the menu API, possibly unsuccessfully?)
from . import models
from . import serializers
from rest_framework.decorators import api_view

def index(request):
 return render(request, 'index.html', {})

class BookingViewSet(ModelViewSet):
    def get(self, request):
        items = models.booking.objects.all()
        serializer_class = serializers.BookingSerializer(items, many = True)
        return Response(serializer_class.data)
    
<<<<<<< HEAD

class MenuItemView(ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer

=======
class menuView(APIView):
>>>>>>> parent of 79bea59 (Setup serializers on the menu API, possibly unsuccessfully?)
    def post(self, request):
        serializer = serializers.MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
<<<<<<< HEAD
            return Response({"status":"success", "data": serializer.data})
        
    def get(self, request):
        pass            #FIX LATER

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuItemSerializer
    
    def get(self, request):
        pass
    def put(self, request):
        pass
    def delete(self, request):
        pass
=======
            return Response({"status":"success", "data": serializer.data})
>>>>>>> parent of 79bea59 (Setup serializers on the menu API, possibly unsuccessfully?)
