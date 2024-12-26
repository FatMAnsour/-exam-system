from django.contrib import admin
from .models import *

admin.site.register(Exam)
admin.site.register(Question)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'grade']
    list_per_page = 10
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__istartswith', 'user__last_name__istartswith']

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

admin.site.register(Student, StudentAdmin)
