from django.contrib import admin

from provarme_tenant.models import Client, Plan, Purchase


# Custom django admin
admin.site.site_header = "Drop Azul - Gestão Online"
admin.site.site_title = "Drop Azul - [Administração]"
admin.site.index_title = "Drop Azul - [Administração]"


# Custom itens
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name', 'name_fantasy',)
    list_display = ('name', 'name_fantasy', 'is_active',)
    list_filter = ('is_active',)

class PurchaseAdmin(admin.ModelAdmin):
    search_fields = ('first_name',)
    list_display = ('first_name', 'purchase_date', 'prod_name', 'email', 'payment_type', 'status',)
    list_filter = ('purchase_date',)

class PlanAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'description', 'amount', 'is_active',)
    list_filter = ('created_on',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Purchase, PurchaseAdmin)