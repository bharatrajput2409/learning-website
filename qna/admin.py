from django.contrib import admin
from .models import materials
from .models import comments
from .models import mat_solutions


# Register your models here.
admin.site.register(materials)
admin.site.register(comments)
admin.site.register(mat_solutions)
