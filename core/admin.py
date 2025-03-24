from django.contrib import admin

# Register your models here.
from .models import Place, CodeType, Code, Comment

admin.site.register(Place)
admin.site.register(CodeType)
admin.site.register(Code)
admin.site.register(Comment)
