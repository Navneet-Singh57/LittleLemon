from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from .models import MenuItem, BookingTable
from .serializers import MenuItemSerializers, BookingSerializer
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here. 

def index(request):
    return render(request, 'index.html', {})


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializers
    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    