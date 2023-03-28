from django.contrib import admin
from django.db import models
from .models import Amenities, Hotel, Package, Extras, Client, Contact, Booking, Packbook

# Register your models here.


# Register your models here.
admin.site.register(Amenities)
admin.site.register(Hotel)
admin.site.register(Extras)
admin.site.register(Package)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(Booking)
admin.site.register(Packbook)
