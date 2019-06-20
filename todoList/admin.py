from django.contrib import admin
from .models import List

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    date_hierarchy = 'update_on'
    fields = ('title', 'desc','update_on')  # This will show fields on admin Panel Update/inert
    list_display = ('title','desc','update_on')
    list_filter = ['title','update_on']
    search_fields = ['title','desc']
    list_per_page = 3
    ordering = ['-update_on'] # '-' is used to display oject in descending order

admin.site.register(List,ListAdmin)