from django.contrib import admin

from .models import StudentModel

# admin.site.register(StudentModel)

@admin.register(StudentModel)
class Studentadmin(admin.ModelAdmin):
          list_display = ['name','city','marks']
# Register your models here.
