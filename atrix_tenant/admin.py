from django.contrib import admin

from atrix_tenant.models import Client, Plan, Purchase


# Custom django admin
admin.site.site_header = "atrixmob"
admin.site.site_title = "atrixmob - [Administração]"
admin.site.index_title = "atrixmob - [Administração]"


# Custom itens
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name', 'name_fantasy', 'plan',)
    list_display = ('name', 'name_fantasy', 'plan', 'is_active',)
    list_filter = ('is_active',)

admin.site.register(Client, ClientAdmin)
admin.site.register(Plan)
admin.site.register(Purchase)