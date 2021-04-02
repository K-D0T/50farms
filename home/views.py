from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import SubmitModel
# Create your views here.


'''
for editing just have them re enter the same tag and have it delete the old one
'''

def all(request):
	qs = SubmitModel.objects.all()

	tagsearch = request.GET.get('tagsearch')

	if tagsearch != '' and tagsearch is not None:
		qs = qs.filter(tagnum__icontains=tagsearch)


	context = {
		'queryset': qs,

 

	}
	

	return render(request, 'all.html', context)	

def HeadInPastures(request):
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
	
	print(qs)
	return render(request, 'home.html', context)




def search(request):
	return render(request, 'search.html', {})


def DeletePost(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("all"))	
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")

		print("shit")
		setup1=SubmitModel.objects.filter(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture)
		#setup1.delete()
		return HttpResponseRedirect(reverse('all'))


def EditPost(request):

	if request.method != 'GET':
		return HttpResponseRedirect(reverse("all"))	
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")
		print("FUCK YES")
		

		setup1=SubmitModel.objects.filter(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture)
		#setup1.delete()
		return HttpResponseRedirect(reverse('all'))










def SignUp_saveCows(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("home"))
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture, pic=pic)
		setup1.save()
		return HttpResponseRedirect(reverse('home'))




def SignUp_saveBulls(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("bulls"))
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture, pic=pic)
		setup1.save()
		return HttpResponseRedirect(reverse('bulls'))





def SignUp_saveCalves(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("calves"))
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		sire=request.POST.get("sire")
		dam=request.POST.get("dam")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, sire=sire, dam=dam, owner=owner, pasture=pasture, pic=pic)
		setup1.save()
		return HttpResponseRedirect(reverse('calves'))



def SignUp_saveHeifers(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("heifers"))
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		owner=request.POST.get("owner")
		pasture=request.POST.get("pasture")
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, owner=owner, pasture=pasture, pic=pic)
		setup1.save()
		return HttpResponseRedirect(reverse('heifers'))





def bulls(request):
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
	
	return render(request, 'bulls.html', context)







def calves(request):
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
	
	return render(request, 'calves.html', context)







def heifers(request):
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
	
	return render(request, 'heifers.html', context)	
