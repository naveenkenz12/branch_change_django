from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf 

from django.contrib import messages
from django.template import RequestContext

from branch_change.forms import userpostform
from django.contrib.auth.forms import UserCreationForm
from branch_change.models import userpost

from branch_change.models import branch_stats
from branch_change.models import allocated_branch

import csv
import os
# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response
# from rest_framework.views import APIView

def get_allocation(request):
	if not request.user.is_staff:
		raise PermissionDenied
	import subprocess
	#os.system("python3 ./export.csv ./input_programmes")
	subprocess.call("pwd",shell=True)
	subprocess.call("./main.sh",shell=True)
	subprocess.call("cd ..",shell=True)
	subprocess.call("pwd",shell=True)
	data = []
	with open('./branch_change/output.csv','r') as csvfile :
		reader = csv.reader(csvfile,delimiter = ',')
		for line in reader:
			input_data = allocated_branch()
			input_data.roll_number = line[0]
			input_data.name = line[1]
			input_data.initial_branch = line[2]
			input_data.alloted_branch = line[3]
			input_data.save()
	with open('./branch_change/output_stats.csv') as csvfile:
		reader = csv.reader(csvfile,delimiter = ',')
		for line in reader:
			input_data = branch_stats()
			input_data.branch_name = line[0]
			input_data.cutoff = line[1]
			input_data.sanctioned_st = line[2]
			input_data.original_st = line[3]
			input_data.final_st = line[4]
			input_data.save()
	return HttpResponseRedirect('/admin')


# def get_allocation(request):
# 	data = '<html><body><h1>Hello, world</h1></body></html>'
# 	return Response(data)

def save_csv(request):
	if not request.user.is_staff:
		raise PermissionDenied
	data = []
	with open('./branch_change/input_options.csv','r') as csvfile :
		reader = csv.reader(csvfile,delimiter = ',')
		for line in reader:
			input_data = userpost()
			input_data.user_name = '@'+line[0]+'__'
			input_data.roll_number = line[0]
			input_data.name = line[1]
			input_data.present_branch = line[2] 
			input_data.category = line[4]
			input_data.cpi = line[3]
			input_data.pref1 = line[5]
			input_data.pref2 = line[6]
			input_data.pref3 = line[7]
			input_data.pref4 = line[8]
			input_data.pref5 = line[9]
			input_data.pref6 = line[10]
			input_data.pref7 = line[11]
			input_data.pref8 = line[12]
			input_data.pref9 = line[13]
			input_data.pref10 = line[14]
			input_data.pref11= line[15]
			input_data.pref12 = line[16]
			input_data.pref13 = line[17]
			input_data.pref14 = line[18]
			input_data.pref15 = line[19]
			input_data.save()
	return HttpResponseRedirect('/admin')


def download_csv(request):
    if not request.user.is_staff:
        raise PermissionDenied
    queryset =userpost.objects.all()
    opts = queryset.model._meta
    model = queryset.model
    response = HttpResponse(content_type='text/csv')
    # force download.
    response['Content-Disposition'] = 'attachment;filename=export.csv'
    # the csv writer
    writer = csv.writer(response)
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])
    return response
#download_csv.short_description = "Download selected as csv"

'''
def login(request):
	log={}
	log.update(csrf(request))
	return render_to_response('branch_change_form.html',log , context_instance = RequestContext(request))

'''		

'''
def branch_change_form(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	else:
		if request.method == 'POST':
			form = userpostform(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/naveen')
			else:
				print(form.errors)
		return render(request, 'branch_change_form.html', {'branch_change_form': userpostform() })
'''		
	



def branch_change_form(request):
   
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    try:
        queryset =userpost.objects.get(user_name = request.user.username)
    except:
        queryset = None

    if request.method == 'POST':
        form = userpostform(request.POST, instance = queryset)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/naveen')
        else:
            print(form.errors)
    else:
        try:
        	form = userpostform(initial = {'user_name':queryset.user_name,'roll_number' : queryset.roll_number , 'name' : queryset.name, 'cpi': queryset.cpi, 'present_branch' : queryset.present_branch, 'category': queryset.category, 'pref1': queryset.pref1, 'pref2': queryset.pref2, 'pref3': queryset.pref3, 'pref4': queryset.pref4, 'pref5': queryset.pref5, 'pref6': queryset.pref6, 'pref7': queryset.pref7, 'pref8': queryset.pref8, 'pref9': queryset.pref9, 'pref10': queryset.pref10, 'pref11': queryset.pref11, 'pref12': queryset.pref12, 'pref13': queryset.pref13, 'pref14': queryset.pref14, 'pref15': queryset.pref15 })
        except:
        	form = userpostform(initial = {'user_name':request.user.username })
    context = {
     'branch_change_form' :form,
     'queryset' :queryset

    }
    return render(request, 'branch_change_form.html', context)
    #return render(request, 'user.html', context)


def login(request):
	if not request.user.is_authenticated():
		log={}
		log.update(csrf(request))
		return render_to_response('branch_change_form.html',log , context_instance = RequestContext(request))
	else:
		return HttpResponseRedirect('/branch_change_form')


def logout(request):
	auth.logout(request)
	render_to_response('branch_change_form.html',{})
	return HttpResponseRedirect('/login')

def authorized_view(request):
	username = request.POST.get('username','')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password =password )

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/branch_change_form')
	else:
		messages.error(request, 'username or password is not valid')
		return HttpResponseRedirect('/login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/branch_change_form")
    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()

    return render_to_response('registration.html',args)

def naveen(request):
	try:
		queryset =userpost.objects.get(user_name = request.user.username)
	except:
		queryset = None
	context = {
    	'queryset' :queryset
    }
	return render(request, 'user.html', context)

def see_allocation(request):
	if not request.user.is_staff:
		raise PermissionDenied
	try:
		queryset = allocated_branch.objects.all()
	except:
		queryset = None
	context = {
		'queryset' :queryset
		}
	return render(request, 'get_allocation.html' , context)


def see_stats(request):
	if not request.user.is_staff:
		raise PermissionDenied
	try:
		queryset = branch_stats.objects.all()
	except:
		queryset = None
	context = {
		'queryset' :queryset
		}
	return render(request, 'get_stats.html' , context)
