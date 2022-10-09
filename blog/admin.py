from django.contrib import admin
from blog.models import Post, Category, Tag
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin


# Register your models here.
# admin.site.register(Post)
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'category', 'visit', 'status')
    search_fields = ('title',)
    list_filter = ('category',)
    ordering = ('status', 'created_at')
    date_hierarchy = 'created_at'
    list_editable = ('status',)

    fieldsets = [
        ('اطلاعات', {'fields': ['title', 'cover']}),
        ('تکمیل اطلاعات', {'fields': ['category', 'description', 'visit', 'status', 'author', 'updated_at']})
    ]

    @admin.display(description='تاریخ آپدیت', ordering='created_at')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y %H:%M:%S')


admin.site.site_header = 'پنل مدیریت بلاگ پای'
admin.site.site_title = 'پنل مدیریت بلاگ پای'
admin.site.index_title = 'بلاگ پای'
