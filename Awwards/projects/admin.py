from django.contrib import admin
from .models import Project,Profile,Comments,DesignRating,UsabilityRating,ContentRating
# Register your models here.

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(DesignRating)
admin.site.register(UsabilityRating)
admin.site.register(ContentRating)
