from django.contrib import admin

# Register your models here.


from .models import Member, unapprovedMember, Chorus, Conductor, City

admin.site.register(Member)
admin.site.register(unapprovedMember)
admin.site.register(Chorus)
admin.site.register(Conductor)
admin.site.register(City)

class unapprovedMember(admin.ModelAdmin):
    change_list_template = ""
    list_display = ('first_name', 'last_name', 'city', 'type')
    exclude = ['user']
    readonly_fields = ['first_name', 'last_name', 'city', 'type']

