from django.contrib import admin
from store.models import Customer,Product,Order,Orderitem
# Register your models here.


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Orderitem)
