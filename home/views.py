from django.shortcuts import render
import requests
from django.http import HttpResponseRedirect
from django.urls import reverse
from home.models import SubmitModel
# Create your views here.


def all(request):
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
	return render(request, 'all.html', context)	



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






def SignUp_saveCows(request):
	if request.method != 'POST':
		return HttpResponseRedirect(reverse("home"))
	else:
		tagnum=request.POST.get("tagnum")
		sex=request.POST.get("sex")
		age=request.POST.get("age")
		comments=request.POST.get("comments")
		color=request.POST.get("color")
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, pic=pic)
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
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, pic=pic)
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
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, sire=sire, dam=dam, pic=pic)
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
		pic = request.FILES['pic']

		setup1=SubmitModel(tagnum=tagnum, sex=sex, age=age, comments=comments, color=color, pic=pic)
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
