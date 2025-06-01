from django.contrib import admin
from .models import Project, ProjectImage, About, ContactMessage

# Inline admin to show ProjectImage inside Project admin
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of extra empty forms to show

# Admin for Project model including inline images
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Columns to show in admin list page
    inlines = [ProjectImageInline]

# Admin for ContactMessage model
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('submitted_at',)

# Register the models with their respective admin classes
admin.site.register(Project, ProjectAdmin)
admin.site.register(About)
admin.site.register(ContactMessage, ContactMessageAdmin)
