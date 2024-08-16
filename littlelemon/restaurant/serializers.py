from .models import MenuItem, BookingTable
from rest_framework import serializers

        
class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = ['name','no_of_guests','bookingdate']