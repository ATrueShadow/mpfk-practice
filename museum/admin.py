from django.contrib import admin

# Register your models here.

from .models import Tour, Ticket, Exhibition, Item


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', )


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
    list_display = ('tour', 'visitor')


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', )