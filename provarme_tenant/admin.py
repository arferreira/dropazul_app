from django.contrib import admin

from provarme_tenant.models import Client, Plan, Purchase


# Custom django admin
admin.site.site_header = "provarme_core"
admin.site.site_title = "provarme_core - [Administração]"
admin.site.index_title = "provarme_core - [Administração]"


# Custom itens
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name', 'name_fantasy',)
    list_display = ('name', 'name_fantasy', 'is_active',)
    list_filter = ('is_active',)

class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ('client',)
    list_display = ('client', 'plan', 'active_url', 'modified_on', 'created_on', 'validate_on', 'status',)
    list_filter = ('created_on', 'validate_on',)

class PlanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'amount', 'is_active',)
    list_filter = ('created_on',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Purchase, PurchaseAdmin)