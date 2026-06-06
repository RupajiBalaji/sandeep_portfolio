from django.contrib import admin
from .models import Skill, Project, Experience, Education, Certification, ContactMessage


# Customize admin site
admin.site.site_header = "Shalem Sandeep - Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Your Portfolio Management"


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']
    list_editable = ['proficiency', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'detailed_description')
        }),
        ('Media & Links', {
            'fields': ('image', 'live_link', 'github_link')
        }),
        ('Technical Details', {
            'fields': ('technologies',)
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'employment_type', 'is_current', 'start_date']
    list_filter = ['employment_type', 'is_current', 'start_date']
    search_fields = ['position', 'company']
    ordering = ['-is_current', '-start_date']
    list_editable = ['is_current']
    fieldsets = (
        ('Position Details', {
            'fields': ('position', 'company', 'employment_type')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'is_current')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']
    list_filter = ['start_date']
    search_fields = ['degree', 'institution']
    fieldsets = (
        ('Education Details', {
            'fields': ('degree', 'institution', 'field_of_study')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'date']
    list_filter = ['date']
    search_fields = ['title', 'issuer']
    fieldsets = (
        ('Certification Details', {
            'fields': ('title', 'issuer')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Information', {
            'fields': ('date', 'certificate_link')
        }),
        ('Display', {
            'fields': ('order',)
        }),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
        ('Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return False  # Prevent manual creation of messages
