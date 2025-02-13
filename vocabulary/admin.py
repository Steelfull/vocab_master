from django.contrib import admin
from django.contrib import admin
from .models import GermanWord, Declination, Article, Pronoun, Conjunction

class DeclinationInline(admin.TabularInline):
    model = Declination
    extra = 4  # 4 Kasus pro Wort

@admin.register(GermanWord)
class GermanWordAdmin(admin.ModelAdmin):
    list_display = ('base_form', 'word_class', 'user')
    inlines = [DeclinationInline]
    search_fields = ('base_form',)
    



@admin.register(Declination)
class DeclinationAdmin(admin.ModelAdmin):
    list_display = ('word', 'case', 'singular', 'plural')
    list_filter = ('case',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_type', 'case', 'gender', 'singular', 'plural')
    list_filter = ('article_type', 'case', 'gender')

@admin.register(Pronoun)
class PronounAdmin(admin.ModelAdmin):
    list_display = ('pronoun_type', 'case', 'gender', 'singular', 'plural')
    list_filter = ('pronoun_type', 'case', 'gender')

@admin.register(Conjunction)
class ConjunctionAdmin(admin.ModelAdmin):
    list_display = ('conjunction_type', 'case_governed', 'word')
    list_filter = ('conjunction_type', 'case_governed')