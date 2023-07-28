from django.contrib import admin
from .models import Labour_data,Labour_type
# Register your models here.
@admin.register(Labour_data)

class Labour_data_admin(admin.ModelAdmin):
    list_display=['user','type','name','no_of_w','salary','contact','location','other_type']
    
@admin.register(Labour_type)

class Labour_type_admin(admin.ModelAdmin):
    list_display=['user','reg_type'] 