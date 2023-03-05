from django.contrib import admin

from index.models import *

# Register your models here.


admin.site.site_title = "电影"
admin.site.site_header = "电影"
admin.site.index_title = "电影"


class UsersManager(admin.ModelAdmin):
    # 列表页显示那些字段
    search_fields = ('name', 'email')
    list_display = ['id', 'name', 'password', 'email', 'time', 'is_active', 'admin_sample']


class FilmsManager(admin.ModelAdmin):
    # 列表页显示那些字段
    # search_fields = ('name')
    list_display = ['id', 'name', 'admin_sample', 'year', 'person']
    list_per_page = 12


class StartManager(admin.ModelAdmin):
    # 列表页显示那些字段
    # search_fields = ('name')
    list_display = ['id', 'name', 'admin_sample', 'time']
    list_per_page = 12


admin.site.register(Start, StartManager)
admin.site.register(Users, UsersManager)
admin.site.register(Films, FilmsManager)
