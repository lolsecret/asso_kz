from django.contrib import admin


from .models import Trip


class TripAdmin(admin.ModelAdmin):
    fields = (
        'id', 'pick_up_address', 'drop_off_address', 'status',
        'driver', 'rider',
        'created_at', 'updated_at',
    )
    list_display = (
        'id', 'pick_up_address', 'drop_off_address', 'status',
        'driver', 'rider',
        'created_at', 'updated_at',
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id', 'created_at', 'updated_at',
    )



admin.site.register(Trip, TripAdmin)
