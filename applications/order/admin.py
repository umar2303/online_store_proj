from django.contrib import admin

from applications.order.models import OrderProduct, Order


class OrderProductInLine(admin.TabularInline):
    model = OrderProduct
    extra = 1
    fields = ('product', 'quantity', 'total_cost')


class OrderAdminDisplay(admin.ModelAdmin):
    inlines = [OrderProductInLine, ]


admin.site.register(Order, OrderAdminDisplay)

