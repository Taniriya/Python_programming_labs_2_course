# blog/admin.py
from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_date', 'approved_comment']
    list_filter = ['approved_comment', 'created_date']
    search_fields = ['author__username', 'text']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)
        self.message_user(request, f'{queryset.count()} комментариев одобрено.')
    approve_comments.short_description = 'Одобрить выбранные комментарии'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_date', 'published_date', 'category']
    list_filter = ['created_date', 'published_date', 'category']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_date'

    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'author', 'category')
        }),
        ('Даты', {
            'fields': ('created_date', 'published_date')
        }),
        ('Медиа', {
            'fields': ('image',)
        }),
    )