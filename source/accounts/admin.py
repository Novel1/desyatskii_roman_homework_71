from django.contrib import admin

from accounts.models import Accounts


class AccountsAdmin(admin.ModelAdmin):
    field = ['email', 'gender', 'password', 'password_confirm', 'first_name', 'last_name', 'inform', 'number', 'avatar']


admin.site.register(Accounts, AccountsAdmin)
