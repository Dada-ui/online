from django.contrib import admin
from test1.models import *

# Register your models here.

class exam_model_admin(admin.ModelAdmin):
    list_display = ["id","select_user","questions","inputs"]

admin.site.register(exam_model,exam_model_admin)