from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
#from django_google_maps import fields as map_fields
from geoposition.fields import GeopositionField
from django.utils import timezone
# Create your models here.

#Model - Landlord
class Landlord(models.Model):
	name = models.CharField('Name', max_length=200)
	address = models.CharField('Address', max_length=200)
	pan_number = models.CharField('PAN Number', max_length=200, unique=True)
	phone_no = models.IntegerField('Phone Number',unique=True)
	email = models.EmailField('Email', max_length=200)
	def __str__(self):
		return self.name
#Model - Tenant
class Tenant(models.Model):
	name = models.CharField('Name', max_length=200)
	address = models.CharField('Address', max_length=200)
	pan_number = models.CharField('PAN Number', max_length=200, unique=True)
	phone_no = models.IntegerField('Phone Number',unique=True)
	email = models.EmailField('Email', max_length=200)
	def __str__(self):
		return self.name
#Model - Standard Pad Amenities
class Standard_Pad_Amenities(models.Model):
	standard_pad_amenity_name = models.CharField('Standard Pad Amenity Name', max_length=200)
	def __str__(self):
		return self.standard_pad_amenity_name
#Model - Standard Room Amenities
class Standard_Room_Amenities(models.Model):
	standard_room_amenity_name = models.CharField('Standard Room Amenity Name', max_length=200)
	def __str__(self):
		return self.standard_room_amenity_name
#Model - Room Specific Amenities
class Room_Specific_Amenities(models.Model):
	room_specific_amenity_name = models.CharField('Rom Specific Amenity Name', max_length=200)
	def __str__(self):
		return self.room_specific_amenity_name
#Model - Society Amenities
class Society_Amenities(models.Model):
	society_amenity_name = models.CharField('Society Amenity Name', max_length=200)
	def __str__(self):
		return self.society_amenity_name
#Model - Room
class Room(models.Model):
	room_name = models.CharField('Room Name', max_length=200)
	room_sharing_choices = (('single','single'),('double','double'))
	room_sharing = models.CharField('Room Sharing Type', max_length=200,choices=room_sharing_choices, default='double')
	room_rent = models.DecimalField('Room Rent(INR)', max_digits=5, decimal_places=0)
	room_specific_amenities = models.ManyToManyField(Room_Specific_Amenities)
	def __str__(self):
		return self.room_name
#Model - Pad Specific Amenities
class Pad_Specific_Amenities(models.Model):
	pad_specific_amenity_name = models.CharField('Pad Specific Amenity Name', max_length=200)
	def __str__(self):
		return self.pad_specific_amenity_name
#Model - Internet Connection
class Internet_Connection(models.Model):
	service_provider = models.CharField('Internet Service Provider', max_length=200)
	address = models.CharField('Address(optional)', max_length=200, default='This Field Is Optional')
	def __str__(self):
		return self.service_provider
#Model - Pad
class Pad(models.Model):
#defining a function to group the pads city wise and to assign the corresponding compound ID
	def count_auto(self):
		count = Pad.objects.filter(city = self.city).count() + 1
		return (self.city + '%d')%count
	def  save(self, *args, **kwargs):
		#if not self.pad_id:
		self.pad_id = self.count_auto()
		super(Pad,self).save(*args, **kwargs)

	pad_id = models.CharField(max_length = 200, null = True, blank = True)  
	landlord = models.ForeignKey(Landlord, on_delete = models.CASCADE, null = True)
	pad_for_choices = (('boys','boys'),('girls','girls'),('family','family'),('all','all'))
	pad_for = models.CharField('Pad For', max_length=200,choices=pad_for_choices,default='all')
	available_from = models.DateField('Available From')
	address_line1 = models.CharField('House No./Apartment Name/Block Name', max_length=200, default = 'Enter valid details...')
	floor = models.CharField('Floor', max_length=200)
	locality = models.CharField('Locality', max_length=200,default='Enter Sector/Area Name')
	landmark = models.CharField('Landmark',max_length=200,default='Near...')
	city_choices = (('Noida','Noida'),('Gurgaon','Gurgaon'),('Delhi','Delhi'))
	city = models.CharField('City',max_length=200,choices=city_choices,default='Noida')
	pincode = models.IntegerField('Pincode')
	property_type_choices = (('flat','flat'),('house','house'))
	property_type = models.CharField('Property Type', max_length=200, choices=property_type_choices,default='house')
	pad_rent_to_owner = models.DecimalField('Rent To Owner',max_digits=8,decimal_places=2,default=0)
	pad_rent_from_tenant = models.DecimalField('Rent From Tenant',max_digits=8,decimal_places=2,default=0)
	area = models.DecimalField('Area(in sqft)', max_digits=8,decimal_places=2)
	bedroom_count = models.IntegerField('Number of Bedrooms')
	bathroom_count = models.IntegerField('Number of Bathrooms')
	balcony_count = models.IntegerField('Number of Balconies')
	room = models.ManyToManyField(Room)
	flooring_choices = (('mosaic','mosaic'),('marble','marble'),('granite','granite'),('tiles','tiles'))
	flooring_type = models.CharField('Flooring Type', max_length=200, choices=flooring_choices,default='tiles')
	pad_specific_amenities = models.ManyToManyField(Pad_Specific_Amenities)
	society_amenities = models.ManyToManyField(Society_Amenities)
	internet_connection = models.ManyToManyField(Internet_Connection)
	electric_meter_num = models.CharField('Electricity Meter Number', max_length=200,unique=True)
	#google_address = map_fields.AddressField(max_length=100,null=True)
	#geolocation = map_fields.GeoLocationField(max_length=100,null=True)
	google_position = GeopositionField(null=True)
	def __str__(self):
		return (self.pad_id +"," +self.landlord.name + ","+self.pad_for)