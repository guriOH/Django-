from django.contrib import admin

# Register your models here.
from .models import Fcuser

# Register your models here.
class  UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(Fcuser,UserAdmin)