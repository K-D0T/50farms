from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .forms import *
import os
from django.shortcuts import render, get_object_or_404, redirect

#password: BradAmos2020



def cowsguest(request):
	qs = SubmitModel.objects.all()
	fuck = SubmitModel.objects.all()
	cows = fuck.filter(sex__icontains='Cow')

	tagsearch = request.GET.get('tagsearch')

	if tagsearch != '' and tagsearch is not None:
		qs = qs.filter(tagnum__icontains=tagsearch)



	context = {
		'queryset': qs,
		'cow': cows,


	}


	return render(request, 'cowsguest.html', context)










def bullsguest(request):

	qs = SubmitModel.objects.all()
	tagsearch = request.GET.get('tagsearch')
	fuck = SubmitModel.objects.all()
	if tagsearch != '' and tagsearch is not None:
		tagnum = qs.filter(tagnum__icontains=tagsearch)


	bulls = fuck.filter(sex__icontains='Bull')
	context = {
		'queryset': qs,
		'bull': bulls,
	}

	return render(request, 'bullsguest.html', context)













def calvesguest(request):

	qs = SubmitModel.objects.all()
	tagsearch = request.GET.get('tagsearch')
	fuck = SubmitModel.objects.all()
	if tagsearch != '' and tagsearch is not None:
		qs = qs.filter(tagnum__icontains=tagsearch)


	calves = fuck.filter(sex__icontains='Calf')

	context = {
		'queryset': qs,
		'calf': calves,

	}

	return render(request, 'calvesguest.html', context)






def heifersguest(request):

	qs = SubmitModel.objects.all()
	tagsearch = request.GET.get('tagsearch')
	fuck = SubmitModel.objects.all()
	if tagsearch != '' and tagsearch is not None:
		qs = qs.filter(tagnum__icontains=tagsearch)

	heifers = fuck.filter(sex__icontains='Heifer')
	context = {
		'queryset': qs,
		'heifer': heifers,
	}

	return render(request, 'heifersguest.html', context)







def guest(request):
	qs = SubmitModel.objects.all()

	tagsearch = request.GET.get('tagsearch')

	if tagsearch != '' and tagsearch is not None:
		qs = qs.filter(tagnum__icontains=tagsearch)


	context = {
		'queryset': qs,

	}


	return render(request, 'guest.html', context)

def login_request(request):

	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)

		if user is not None:

			login(request, user)
			return HttpResponseRedirect(reverse("home"))
	else:
		print("invalid pass")

	form = AuthenticationForm()
	return render(request = request,
					template_name = "login.html",
					context={"form":form})



def logout_request(request):
	logout(request)


def all(request):
	if request.user.is_authenticated:
		form = MainForm(request.POST, request.FILES)
		data = list(SubmitModel.objects.values())
		
		try:
			
			owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
			owner_id = owner_id[0]['owner_id']

			pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
			pasture_id = pasture_id[0]['pasture_id']

			owner = list(OWNER.objects.filter(id=owner_id).values())
			pasture = list(PASTURE.objects.filter(id=pasture_id).values())
			data = list(SubmitModel.objects.values())


			return render(request, 'all.html', {'form': form, 'data': data, 'owner': owner, 'pasture': pasture})
		except:
			return render(request, 'all.html', {'form': form, 'data': data})

def HeadInPastures(request):
	if request.user.is_authenticated:
		qs = SubmitModel.objects.all()

		BentonCounty = qs.filter(pasture__icontains='Benton County')
		BentonCountyCount = len(BentonCounty)


		FeedMill = qs.filter(pasture__icontains='Feed Mill')
		FeedMillCount = len(FeedMill)

		Maysville = qs.filter(pasture__icontains='Maysville')
		MaysvilleCount = len(Maysville)

		Caswell = qs.filter(pasture__icontains='Caswell')
		CaswellCount = len(Caswell)

		Obrian = qs.filter(pasture__icontains='Obrian')
		ObrianCount = len(Obrian)

		NoPlace = qs.filter(pasture__icontains='No Place')
		NoPlaceCount = len(NoPlace)



		context = {
			'BC': BentonCountyCount,
			'FM': FeedMillCount,
			'MV': MaysvilleCount,
			'CW': CaswellCount,
			'OB': ObrianCount,
			'NP': NoPlaceCount,




		}

		return render(request, 'HeadInPastures.html', context)

def home(request):
	if request.user.is_authenticated:
		form = MainForm(request.POST, request.FILES)
		data = list(SubmitModel.objects.values())
		dlist = []
		for i in data:
			if i['sex_id'] == 2:
				dlist.append(i)

		
		try:

			owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
			owner_id = owner_id[0]['owner_id']

			pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
			pasture_id = pasture_id[0]['pasture_id']

			owner = list(OWNER.objects.filter(id=owner_id).values())
			pasture = list(PASTURE.objects.filter(id=pasture_id).values())
			data = list(SubmitModel.objects.values())
			dlist = []
			for i in data:
				if i['sex_id'] == 2:
					dlist.append(i)

			return render(request, 'home.html', {'form': form, 'data': dlist, 'owner': owner, 'pasture': pasture})
		except:
			return render(request, 'home.html', {'form': form, 'data': dlist})




def search(request):
	return render(request, 'search.html', {})


def DeletePost(request):


	if request.user.is_authenticated:
		if request.method != 'POST':
			return HttpResponseRedirect(reverse("all"))

		if request.method=='POST' and 'btnform1' in request.POST:
			tagnum=request.POST.get("tagnum")

			sex=request.POST.get("sex")
			age=request.POST.get("age")
			comments=request.POST.get("comments")
			color=request.POST.get("color")
			owner=request.POST.get("owner")
			pasture=request.POST.get("pasture")



			setup1= SubmitModel.objects.filter(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture)
			setup2 = SubmitModel.objects.get(tagnum=tagnum).id
			setup3 = SubmitModel.objects.filter(id=setup2).values()
			values = setup3[0]

			pic_name = values.get("pic")
			os.remove("/home/kdot/Environment/50farms/cattle/media/" + pic_name)

			setup1.delete()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

		if request.method=='POST' and 'btnform2' in request.POST:

			tagnum=request.POST.get("tagnum")

			setup1=SubmitModel.objects.filter(tagnum=tagnum)
			setup1.delete()




			pic=request.POST.get("pic")
			tagnum=request.POST.get("tagnum")
			sex=request.POST.get("sex")
			age=request.POST.get("age")
			comments=request.POST.get("comments")
			color=request.POST.get("color")
			sire=request.POST.get("sire")
			dam=request.POST.get("dam")
			owner=request.POST.get("owner")
			pasture=request.POST.get("pasture")



			setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, sire=sire, dam=dam, color=color, owner=owner, pasture=pasture, pic=pic)
			setup1.save()
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def EditPost(request, id):

	if request.user.is_authenticated:
		data = list(SubmitModel.objects.filter(pk=id).values())

		owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
		owner_id = owner_id[0]['owner_id']

		pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
		pasture_id = pasture_id[0]['pasture_id']

		owner = list(OWNER.objects.filter(id=owner_id).values())
		pasture = list(PASTURE.objects.filter(id=pasture_id).values())

		if request.method != 'POST':
			editform = EditForm(request.POST, request.FILES)
			return render(request, 'edit.html', {'editform': editform, 'data': data, 'owner': owner, 'pasture': pasture})
		else:
			a = SubmitModel.objects.get(pk=id)
			editform = EditForm(request.POST, request.FILES, instance=a)
			
			if editform.is_valid():
				post = editform.save(commit=False)
				post.author = request.user
				post.save()
				return HttpResponseRedirect(reverse("home"))
			else:
				print(editform.errors)
				print("form is invalid")
				return render(request, 'edit.html', {'editform': editform, 'data': data, 'owner': owner, 'pasture': pasture})

			
	


def SignUp_saveCows(request):

	if request.user.is_authenticated:
		if request.method != 'POST':
			return HttpResponseRedirect(reverse("home"))
		else:
			form = MainForm(request.POST, request.FILES)
			print(form['sire'])
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return HttpResponseRedirect(reverse('home'))
			else:
				print("Form is invalid")
				return HttpResponseRedirect(reverse('home'))


def SignUp_saveBulls(request):
	if request.user.is_authenticated:
		if request.method != 'POST':
			return HttpResponseRedirect(reverse("bulls"))
		else:
			form = MainForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return HttpResponseRedirect(reverse('bulls'))
			else:
				print("Form is invalid")
				return HttpResponseRedirect(reverse('bulls'))





def SignUp_saveCalves(request):
	if request.user.is_authenticated:
		if request.method != 'POST':
			return HttpResponseRedirect(reverse("calves"))
		else:
			form = MainForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return HttpResponseRedirect(reverse('calves'))
			else:
				print("Form is invalid")
				return HttpResponseRedirect(reverse('calves'))



def SignUp_saveHeifers(request):
	if request.user.is_authenticated:
		if request.method != 'POST':
			return HttpResponseRedirect(reverse("heifers"))
		else:
			form = MainForm(request.POST, request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.save()
				return HttpResponseRedirect(reverse('heifers'))
			else:
				print("Form is invalid")
				return HttpResponseRedirect(reverse('heifers'))





def bulls(request):
	if request.user.is_authenticated:
		form = MainForm(request.POST, request.FILES)
		data = list(SubmitModel.objects.values())
		dlist = []
		for i in data:
			if i['sex_id'] == 3:
				dlist.append(i)

		try:
			owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
			owner_id = owner_id[0]['owner_id']

			pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
			pasture_id = pasture_id[0]['pasture_id']
			
			owner = list(OWNER.objects.filter(id=owner_id).values())
			pasture = list(PASTURE.objects.filter(id=pasture_id).values())
			data = list(SubmitModel.objects.values())
			dlist = []
			for i in data:
				if i['sex_id'] == 3:
					dlist.append(i)
				
			

			return render(request, 'bulls.html', {'form': form, 'data': dlist, 'owner': owner, 'pasture': pasture})
		except:
			return render(request, 'bulls.html', {'form': form, 'data': dlist})







def calves(request):
	if request.user.is_authenticated:
		form = MainForm(request.POST, request.FILES)
		data = list(SubmitModel.objects.values())
		dlist = []
		for i in data:
			if i['sex_id'] == 0 or 1:
				dlist.append(i)

		
		try:

			owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
			owner_id = owner_id[0]['owner_id']

			pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
			pasture_id = pasture_id[0]['pasture_id']

			owner = list(OWNER.objects.filter(id=owner_id).values())
			pasture = list(PASTURE.objects.filter(id=pasture_id).values())
			data = list(SubmitModel.objects.values())
			dlist = []
			for i in data:
				if i['sex_id'] == 0 or 1:
					dlist.append(i)

			return render(request, 'calves.html', {'form': form, 'data': dlist, 'owner': owner, 'pasture': pasture})
		except:
			return render(request, 'calves.html', {'form': form, 'data': dlist})






def heifers(request):
	if request.user.is_authenticated:
		form = MainForm(request.POST, request.FILES)
		data = list(SubmitModel.objects.values())
		dlist = []
		for i in data:
			if i['sex_id'] == 4:
				dlist.append(i)

		
		try:

			owner_id = list(SubmitModel.objects.filter(pk=id).values('owner_id'))
			owner_id = owner_id[0]['owner_id']

			pasture_id = list(SubmitModel.objects.filter(pk=id).values('pasture_id'))
			pasture_id = pasture_id[0]['pasture_id']

			owner = list(OWNER.objects.filter(id=owner_id).values())
			pasture = list(PASTURE.objects.filter(id=pasture_id).values())
			data = list(SubmitModel.objects.values())
			dlist = []
			for i in data:
				if i['sex_id'] == 4:
					dlist.append(i)

			return render(request, 'heifers.html', {'form': form, 'data': dlist, 'owner': owner, 'pasture': pasture})
		except:
			return render(request, 'heifers.html', {'form': form, 'data': dlist})