from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):
    # Other configurations for your model admin
    
    # Change the display name in the admin interface
    verbose_name = "Superuser"

# Register the model with the custom admin
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)