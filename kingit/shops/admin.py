from django.contrib import admin
from .models import Tenant, TC, Rent, Worker, Pavilion


class TCAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'count_pavilions', 'cost', 'city', 'storeys')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('status',)


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'password', 'role', 'phone')
    list_display_links = ('id', 'full_name',)
    search_fields = ('role',)


class PavilionAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_pavilion', 'title_TC', 'floor', 'status', 'area',)
    list_display_links = ('id', 'number_pavilion')
    search_fields = ('status',)


class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_phone', 'phone', 'address')
    list_display_links = ('id',)


class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_TC', 'number_pavilion', 'status', 'start_rent', 'finish_rent')
    list_display_links = ('id',)
    search_fields = ('status',)


admin.site.register(TC, TCAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Pavilion, PavilionAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Rent, RentAdmin)
