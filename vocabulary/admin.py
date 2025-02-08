from django.contrib import admin
from .models import GermanWord, Declination

class DeclinationInline(admin.TabularInline):
    model = Declination
    extra = 4  # 4 Kasus pro Wort

@admin.register(GermanWord)
class GermanWordAdmin(admin.ModelAdmin):
    list_display = ('base_form', 'word_class', 'user')
    inlines = [DeclinationInline]
    search_fields = ('base_form',)