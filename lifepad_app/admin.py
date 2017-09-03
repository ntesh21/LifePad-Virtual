from django.contrib import admin
from .models import Landlord,Tenant,Internet_Connection,Standard_Pad_Amenities,Pad_Specific_Amenities,Standard_Room_Amenities,Room_Specific_Amenities,Society_Amenities,Room,Pad

#PadAdmin
class pad_admin(admin.ModelAdmin):
	radio_fields = {'pad_for':admin.HORIZONTAL,'property_type':admin.HORIZONTAL,'flooring_type':admin.HORIZONTAL}
	#formfield_overrides = {map_fields.AddressField:{'widget':map_widgets.GoogleMapsAddressWidget},}

#RoomAdmin
class room_admin(admin.ModelAdmin):
	radio_fields = {'room_sharing':admin.HORIZONTAL}

#Hiding the user restricted model
class hidden_model_admin(admin.ModelAdmin):
	def get_model_perms(self,request):
		return {}
# Register your models here.
admin.site.register(Landlord)
admin.site.register(Tenant)
admin.site.register(Internet_Connection)
admin.site.register(Pad,pad_admin)
admin.site.register(Room,room_admin)
admin.site.register(Standard_Pad_Amenities)
admin.site.register(Pad_Specific_Amenities)
admin.site.register(Standard_Room_Amenities)
admin.site.register(Room_Specific_Amenities)
admin.site.register(Society_Amenities)