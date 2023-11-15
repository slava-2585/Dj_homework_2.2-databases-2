from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms

from .models import Article, Tag, Scope


class ScopeInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            ismain = form.cleaned_data['ismain']
            # if is_main:
            #     count += 1
            if count > 1:
                raise forms.ValidationError('Выберите один основной тег')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


admin.site.register(Tag)

