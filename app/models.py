from django.db import models
import uuid
from django.contrib.auth.models import User


# import PIL
# Create your models here.

# username: admin, password: riversfront
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name


class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name


class HotelImage(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="Image", on_delete=models.CASCADE)
    # images = models.ImageField(upload_to="hotel", blank=True)


class HotelBooking(BaseModel):
    hotel = models.ForeignKey(Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()
    booking_type = models.CharField(choices=(('pre paid', 'pre paid'), ('post paid', 'post paid')), max_length=100)
