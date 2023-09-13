from django.contrib import admin
from .models import Projeto, Imagem

class ImagemInline(admin.TabularInline):
    model = Imagem
    extra = 4

class ProjetoAdmin(admin.ModelAdmin):
    inlines = [ImagemInline]

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Imagem)
