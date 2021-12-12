from django.contrib import admin
from management_discount_cards.models import Card
from management_products.models import Product, Purchase


class PurchaseInline(admin.TabularInline):
    model = Purchase
    extra = 0


class CardAdmin(admin.ModelAdmin):
    model = Card
    inlines = [PurchaseInline]
    list_display = (
        'id',
        'series',
        'number',
        'create_date',
        'end_of_activity',
        'date_of_use',
        'total_sum',
        'status',
    )
    search_fields = (
        'id',
        'series',
        'number',
        'create_date',
        'end_of_activity',
        'date_of_use',
        'total_sum',
        'status',
    )


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'id',
        'title',
        'price',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Card, CardAdmin)

