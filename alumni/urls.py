from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.opening_page, name='greeting'),
    url(r'^loginform', views.login_form, name='login_form'),

    url(r'^registration', views.registration, name='register_form'),
    url(r'^register', views.register, name='register'),

    url(r'^attempt_logout', views.attempt_logout, name='attempt_logout'),

    url(r'^chorus_index', views.chorus_index, name='chorus_index'),
    url(r'^chorus_detail/(?P<chorus_pk>[0-9]+)', views.chorus_detail, name='chorus_detail'),
    url(r'^alumni_index', views.alumni_index, name='alumni_index'),
    url(r'^alumni_detail/(?P<alumni_pk>[0-9]+)', views.alumni_detail, name='alumni_detail'),

    #ajax choruses
    url(r'get_choruses', views.getChoruses, name='get_choruses'),
    url(r'delete_chorus', views.deleteChorus, name='delete_chorus'),
    url(r'edit_chorus', views.editChorus, name='edit_chorus'),

    #ajax members
    url(r'get_members', views.getMembers, name='get_member'),
    url(r'delete_member', views.deleteMember, name='delete_member'),
    url(r'edit_member', views.editMember, name='edit_member'),
    url(r'approve_member', views.approveMember, name='approve_member'),
    url(r'get_unapproved_members', views.getUnApprovedMembers, name='get_unapproved_members'),
]

