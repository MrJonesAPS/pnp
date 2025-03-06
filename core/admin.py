from django.contrib import admin

# Register your models here.
from .models import Place, PasswordType, Password, Comment

admin.site.register(Place)
admin.site.register(PasswordType)
admin.site.register(Password)
admin.site.register(Comment)
