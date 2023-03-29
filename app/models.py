from django.db import models
import uuid
from django.contrib.auth.models import User
from form import form


# Create your models here.


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


class Extras(BaseModel):
    extra_amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.extra_amenity_name


class Client(User):
    user_name = models.CharField(max_length=100, null=True, blank=False)
    email_id = models.CharField(max_length=100, null=True, blank=False)
    pass_word = models.CharField(max_length=100, null=True, blank=False)


class Hotel(BaseModel):
    hotel_name = models.CharField(max_length=100, blank=True)
    hotel_city = models.CharField(max_length=100, blank=True)
    hotel_provinvce = models.CharField(max_length=100, blank=True)
    hotel_price = models.IntegerField()
    description = models.TextField()
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)
    url = models.URLField(blank=True, null=True)
    STATUS = [
        (1, 'Ok - 1 star'),
        (2, 'Average - 2 star'),
        (3, 'Fine - 3 star'),
        (4, 'Good - 4 star'),
        (5, 'Excellent - 5 star')
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)

    def __str__(self) -> str:
        return self.hotel_name


class Package(BaseModel):
    package_name = models.CharField(max_length=100, blank=True)
    package_city = models.CharField(max_length=100, blank=True)
    package_province = models.CharField(max_length=100, blank=True)
    package_duration = models.CharField(max_length=200, blank=True)
    package_airport = models.CharField(max_length=100, blank=True)
    package_price = models.IntegerField()
    description = models.TextField()
    extras = models.ManyToManyField(Extras)
    date = models.DateField(null=False)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.package_name


# class HotelBooking(BaseModel):
#     hotel = models.ForeignKey(Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name="user_booking", on_delete=models.CASCADE)
#     booking_type = models.CharField(choices=(('pre paid', 'pre paid'), ('post paid', 'post paid')), max_length=100)


class Contact(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=1000, blank=True, null=True)


class Booking(BaseModel):
    STATUS = [
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    ]
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    telephone = models.CharField(max_length=10,blank=True)
    email = models.CharField(max_length=100, blank=True)
    people = models.CharField(max_length=100, blank=True)
    ishotel_name = models.ForeignKey(Hotel, related_name="ishotel_name", on_delete=models.CASCADE, null=True)

    # startdate = models.CharField(max_length=10, default=None)
    # enddate = models.CharField(max_length=10, default=None)


class Packbook(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    telephone = models.CharField(max_length=10,blank=True)
    email = models.CharField(max_length=100, blank=True)
    people = models.CharField(max_length=100, blank=True)
    ispackage_name = models.ForeignKey(Package, related_name='ispackage_name', on_delete=models.CASCADE, null=True)


# class Detailed_description(BaseModel):
#     dest_id = models.AutoField(primary_key=True)
#     city = models.CharField(max_length=20)
#     province = models.CharField(max_length=30)
#     days = models.IntegerField(default=5)
#     price = models.IntegerField(default=500)
#     rating = models.IntegerField(default=5)
#     dest_name = models.CharField(max_length=35)
#     img1 = models.ImageField(upload_to='gallery')
#     img2 = models.ImageField(upload_to='gallery')
#     description = models.TextField(max_length=500)
