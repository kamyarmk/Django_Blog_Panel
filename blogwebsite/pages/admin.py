from django.contrib import admin
from .models import Page

# Register your models here.

@admin.action(description="Publish the Selected Posts")
def MakePublished(modeladmin, request, queryset):
    queryset.update(status='P')
    

class PageAdmin(admin.ModelAdmin):
    fields=(('Title', 'Status'), ('Date', 'OwnerId'), 'Content')
    list_display = ['Title', 'Status']
    ordering = ['Title']
    actions = [MakePublished]

admin.site.register(Page, PageAdmin)