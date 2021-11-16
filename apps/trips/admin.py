from django.contrib import admin


from .models import Trip


class TripAdmin(admin.ModelAdmin):
    fields = (
        'id', 'address', 'status',
        'driver', 'rider', 'comment',
        'created_at', 'updated_at',
        'price', 'payment_type'
    )
    list_display = (
        'id', 'address', 'status',
        'driver', 'rider', 'comment',
        'created_at', 'updated_at',
        'price', 'payment_type'
    )
    list_filter = (
        'status',
    )
    readonly_fields = (
        'id', 'created_at', 'updated_at',
    )
    search_fields = (
        'id',
    )


admin.site.register(Trip, TripAdmin)
