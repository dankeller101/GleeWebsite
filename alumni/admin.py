from django.contrib import admin

# Register your models here.


from .models import Member, unapprovedMember, Chorus, Conductor, City, AuthorizationToken

admin.site.register(Member)

admin.site.register(Chorus)
admin.site.register(Conductor)
admin.site.register(City)

def approveMember(modeladmin, request, queryset):
    for newMember in queryset:
        member = Member()
        member.first_name = newMember.first_name
        member.last_name = newMember.last_name
        member.type = newMember.type
        try:
            #TODO: ideally, make these atomic
            member.save()
            newMember.delete()
        except:
            continue
        else:
            #TODO: send email to email address informing them that their request has been granted
            continue
approveMember.short_description = "Approve selected member requests"

def unapproveMember(modeladmin, request, queryset):
    for member in queryset:
        #TODO:  Send an email to email address informing them that their request has been denied
        member.delete()
unapproveMember.short_description = "Unapprove selected member requests"

class unapprovedMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'type')
    exclude = ['user']
    readonly_fields = ['first_name', 'last_name', 'type']
    # readonly_fields = ['first_name', 'last_name', 'city', 'type']
    actions = [approveMember, unapproveMember]

class AuthorizationTokenAdmin(admin.ModelAdmin):
    list_display = ('name', 'authorization_code', 'delete_date')
    readonly_fields = ['delete_date']

admin.site.register(AuthorizationToken, AuthorizationTokenAdmin)
admin.site.register(unapprovedMember, unapprovedMemberAdmin)