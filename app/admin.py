from django.contrib import admin
from .models import *

# Register your models here.

class ImagesTublerinline(admin.TabularInline):
    model = Images

class TagTublerinline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines=[ImagesTublerinline,TagTublerinline]
    list_display = ['name','price']

class OrderItemsTublerinline(admin.TabularInline):
    model = OrderItems

class OrderAdmin(admin.ModelAdmin):
	inlines = [OrderItemsTublerinline]
	list_display = ['firstname','phone','email','payment_id','paid','date']
	search_fields = ['firstname','email','payment_id','phone']


admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images)
admin.site.register(Contact_us)
admin.site.register(Tag)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItems)
