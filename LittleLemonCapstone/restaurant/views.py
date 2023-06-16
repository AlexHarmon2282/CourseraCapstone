from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers

def index(request):
 return render(request, 'index.html', {})

class bookingView(APIView):
    def get(self, request):
        items = models.booking.objects.all()
        serializer = serializers.BookingSerializer(items, many = True)
        return Response(serializer.data)
    
class menuView(APIView):
    def post(self, request):
        serializer = serializers.MenuSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data": serializer.data})
        
    def get(self, request):
        items = models.Menu.objects.all()
        serializer = serializers.MenuSerializer(items, many = True)
        return Response(serializer.data)