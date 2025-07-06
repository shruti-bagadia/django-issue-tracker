from django.contrib import admin
from .models import Project, Issue, Comment, Tag

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'created_at')
    search_fields = ('name',)
    filter_horizontal = ('members',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'assignee', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority', 'project', 'assignee')
    autocomplete_fields = ['project', 'assignee', 'created_by', 'tags']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'issue', 'created_at')
    search_fields = ('content',)
    autocomplete_fields = ['author', 'issue']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
