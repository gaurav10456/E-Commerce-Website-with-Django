from django.contrib import admin


# Register your models here.
from .models import Blogpost
from .models import Contact


admin.site.register(Blogpost)
admin.site.register(Contact)
