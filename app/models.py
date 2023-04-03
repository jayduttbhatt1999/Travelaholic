from django.db import models
import uuid
from django.contrib.auth.models import User


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
    package_price = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    extras = models.ManyToManyField(Extras)
    date = models.DateField(null=False)
    url = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return "%s %s" % (self.package_name, self.package_price)


class Contact(BaseModel):
    name = models.CharField(max_length=100, blank=True)
    email_id = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return "Complaint from %s " % self.name



class Booking(BaseModel):
    STATUS = [
        (1, 'male'),
        (2, 'female'),
        (3, 'other'),
    ]
    name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=75, blank=True)
    people = models.CharField(max_length=80, blank=True)
    telephone = models.CharField(max_length=10, blank=True)
    hotel_name = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Packbook(BaseModel):
    name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=8, blank=True)
    email = models.CharField(max_length=50, blank=True)
    people = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=10, blank=True)
    select_package_name = models.ForeignKey(Package, related_name='ispackage_name', on_delete=models.CASCADE)

    def __str__(self):
        return "Package for %s " % self.name