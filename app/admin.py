from django.contrib import admin
from django.db import models
from .models import Amenities, Hotel, HotelImage, HotelBooking, Client

# Register your models here.


# Register your models here.
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(HotelBooking)
admin.site.register(Client)
