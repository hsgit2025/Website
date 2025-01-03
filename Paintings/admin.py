from django.contrib import admin
from .models import Painting
from .models import Offer
class PaintingsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
class OffersAdmin(admin.ModelAdmin):
    list_display = ('code', 'description','discount')

admin.site.register(Painting, PaintingsAdmin)
admin.site.register(Offer, OffersAdmin)

