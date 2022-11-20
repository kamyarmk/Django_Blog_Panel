from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.


@admin.action(description="Publish the Selected Posts")
def MakePublished(modeladmin, request, queryset):
    queryset.update(status='P')

class PostAdmin(admin.ModelAdmin):
    fields=(
        ('Title', 'Slug', 'Status'), 
        ('Category', 'Tags'), 
        ('Date', 'Author'), 
        ('Text', 'Featured_Image'),
        ('Meta_Keyword', 'Meta_Desc'))
    list_display = ['Title', 'Status']
    ordering = ['Title']
    actions = [MakePublished]
    change_list_template = 'admin/posts/posts_change_list.html'
    change_form_template = 'admin/posts/posts_change_form.html'
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['Title'].label = "Title of your Post :"
        return form

admin.site.register(Post, PostAdmin)



class CategoryAdmin(admin.ModelAdmin):
    fields=(
        ('Name', 'Slug'), 
        ('Parent', 'Date'),
        ('Meta_Keyword', 'Meta_Desc'))
    list_display = ['Name', 'Parent']
    ordering = ['Parent']

admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    fields=(
        ('Name', 'Slug'), 
        'Date',
        ('Meta_Keyword', 'Meta_Desc'))
    list_display = ['Name', 'Date']
    ordering = ['Date']

admin.site.register(Tag, TagAdmin)