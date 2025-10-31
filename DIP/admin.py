from django.contrib import admin
from .models import DIP_work
# Register your models here.

@admin.register(DIP_work)
class DIPWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'tech_stack', 'created_at', 'in_progress')
    search_fields = ('title', 'tech_stack')
    list_filter = ('in_progress', 'created_at')