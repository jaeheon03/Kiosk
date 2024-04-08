from django.contrib import admin
from cafes.models import *

# Register your models here.
@admin.register(Menu)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class PostAdmin(admin.ModelAdmin):
    pass
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    pass
@admin.register(Temperature)
class TemperatureAdmin(admin.ModelAdmin):
    pass
@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass