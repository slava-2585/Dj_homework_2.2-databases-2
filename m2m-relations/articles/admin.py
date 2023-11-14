from django.contrib import admin

from .models import Article, Tag, Scope


class TagInline(admin.TabularInline):
    model = Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagInline]


