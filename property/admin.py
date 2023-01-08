from django.contrib import admin

from .models import Flat, Complaint, Owner


class FlatOwnersInline(admin.TabularInline):
    model = Flat.owners.through
    raw_id_fields = ('owner', 'flat')


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'id')
    readonly_fields = ('created_at',)
    raw_id_fields = ('liked_by',)

    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year',
        'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    inlines = [FlatOwnersInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'address')

    list_display = ('author', 'address')


class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    raw_id_fields = ('apartments',)

    list_display = ('name', 'phonenumber', 'pure_phonenumber')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)
