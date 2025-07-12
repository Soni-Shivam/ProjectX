from django.contrib import admin
from .models import Swap

@admin.register(Swap)
class SwapAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_initiater',
        'user_reciever',
        'user_initiater_skill',
        'user_reciever_skill',
        'status',
        'date'
    )
    list_filter = ('status', 'date')
    search_fields = ('user_initiater__email', 'user_reciever__email', 'user_initiater_skill', 'user_reciever_skill')

