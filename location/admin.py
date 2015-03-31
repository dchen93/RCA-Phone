from django.contrib import admin

from location.models import Phone, Center

# Register your models here.

class CenterInLine(admin.TabularInline):
	model = Center
	extra = 3


class PhoneAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,				{'fields': ['phone_name']}),
		('Last Updated',	{'fields': ['updated_time']}),
	]
	inlines = [CenterInLine]
	list_display = ('phone_name','updated_time')
	search_fields = ['phone_name']


admin.site.register(Phone, PhoneAdmin)