from django.contrib import admin
from .models import *
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Finorder)
admin.site.register(Payment)
admin.site.register(Review)
admin.site.register(Shipment)
admin.site.register(Discount)

admin.site.register(Product)
# Register your models here.
