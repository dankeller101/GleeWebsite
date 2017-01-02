from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404, HttpResponseBadRequest
from .models import Chorus, Member, unapprovedMember
import json
import alumni.utils

# Create your views here.

def opening_page(request):
    if not request.user.id:
        return HttpResponseRedirect(reverse('alumni:login_form'))
    else:
        return render(request, 'alumni/homepage.html', {
            'user': request.user,
        })

def login_form(request):
    if request.method == "GET":
        template = loader.get_template('alumni/login.html')
        context = {}
        return HttpResponse(template.render(context, request))
    elif request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if not user:
            return render(request, 'predictor/error.html', {
                'error_message': "Failed to log you in.",
            })

        login(request, user)
        return HttpResponseRedirect(reverse('alumni:greeting'))
    else:
        return HttpResponseBadRequest("Invalid method.")

def attempt_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('alumni:greeting'))

def chorus_index(request):
    #TODO: look at how to get all
    return render(request, 'alumni/chorus_index.html', [])
    try:
        choruses = Chorus.objects.all()
    except:
        return HttpResponseBadRequest("Database Error")
    else:
        context = {}
        context['choruses'] = choruses
        return render(request, 'alumni/chorus_index.html', context)

def chorus_detail(request, chorus_pk):
    return render(request, 'alumni/chorus_detail.html', [])
    try:
        chorus = Chorus.objects.get(pk=chorus_pk)
    except:
        context = {}
        context['error_message'] = "The Chorus you tried to access does not exist."
        return render(request, 'alumni/error_page.html', context)
    else:
        context = {}
        context['chorus'] = chorus
        return render(request, 'alumni/chorus_detail.html', context)

def alumni_index(request):
    return render(request, 'alumni/alumni_index.html', [])
    try:
        alumni = Member.objects.filter(type='alumni')
    except:
        return HttpResponseBadRequest("Database Error")
    else:
        context = {}
        context['alumni'] = alumni
        return render(request, 'alumni/alumni_index.html', context)

def alumni_detail(request, alumni_pk):
    return render(request, 'alumni/alumni_detail.html', [])
    try:
        alumnus = Member.objects.get(pk=alumni_pk)
    except:
        context = {}
        context['error_message'] = "The Alumni you tried to access does not exist."
        return render(request, 'alumni/error_page.html', context)
    else:
        context = {}
        context['alumnus'] = alumnus
        return render(request, 'alumni/alumni_detail.html', context)


def admin_page(request):
    return render(request, 'alumni/admin_page.html', [])

#FOR AJAX ADMIN SECTION

#choruses!
#get choruses for Chorus Index
def getChoruses(request):
    try:
        choruses = Chorus.objects.all()
    except:
        return alumni.utils.returnFailure()
    else:
        return json.dumps(choruses)

#edit an existing Chorus
def editChorus(request):
    try:
        chorus = Chorus.objects.get(pk=request.POST['primary_key'])
    except Chorus.DoesNotExist:
        return alumni.utils.returnFailure()
    else:
        chorus.conductor = request.POST['conductor'] if request.POST['conductor'] else chorus.conductor
        chorus.save()
        return json.dumps(chorus)

#delete a chorus!
def deleteChorus(request):
    try:
        chorus = Chorus.objects.get(pk=request.POST['primary_key']).delete()
    except:
        return alumni.utils.returnFailure()
    else:
        return alumni.utils.returnSuccess()

#get Members for index
def getMembers(request):
    try:
        members = Member.objects.all()
    except:
        return alumni.utils.returnFailure()
    else:
        return json.dumps(members)

#edit an existing Member
def editMember(request):
    try:
        member = Member.objects.get(pk=request.POST['primary_key'])
    except Member.DoesNotExist:
        return alumni.utils.returnFailure()
    else:
        member.first_name = request.POST['first_name'] if request.POST['first_name'] else member.conductor
        member.save()
        return json.dumps(member)

#delete an existing Member
def deleteMember(request):
    try:
        member = Member.objects.get(pk=request.POST['primary_key']).delete()
    except:
        return alumni.utils.returnFailure()
    else:
        return alumni.utils.returnSuccess()

#improve a pending member
def approveMember(request):
    try:
        newMember = unapprovedMember.objects.get(pk=request.POST['primary_key'])
    except:
        return alumni.utils.returnFailure()
    else:
        member = Member()
        member.first_name = newMember.first_name
        member.last_name = newMember.last_name
        member.type = newMember.type
        try:
            #TODO: ideally, make these atomic
            member.save()
            newMember.delete()
        except:
            return alumni.utils.returnFailure()
        else:
            return alumni.utils.returnSuccess()

#get a list of pending members
def getUnApprovedMembers(request):
    try:
        unapprovedMembers = unapprovedMember.objects.all()
    except:
        return alumni.utils.returnFailure()
    else:
        return json.dumps(unapprovedMembers)
