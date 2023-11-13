from django.contrib import admin
from .models import UserConnection

@admin.register(UserConnection)
class UserConnectionAdmin(admin.ModelAdmin):
    list_display = ('current_user', 'connected_user', 'connection_status', 'created_at')
    search_fields = ['current_user__username', 'connected_user__username']
    list_filter = ['connection_status']
    readonly_fields = ['created_at']