from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms

from .models import Article, Tag, Scope


class ScopeInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            #ismain = form.cleaned_data['ismain']
            print(form.cleaned_data['is_main'])
            if form.cleaned_data['is_main']:
                count += 1
            if count > 1:
                raise forms.ValidationError('Выберите один основной тег')
        if count == 0:
            raise forms.ValidationError('Выберите основной тег')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 1



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


admin.site.register(Tag)

