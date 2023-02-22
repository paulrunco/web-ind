from django.contrib import admin

from quoting.models import Quote, Customer, Line

class QuoteAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Customer)
admin.site.register(Quote)
admin.site.register(Line)

