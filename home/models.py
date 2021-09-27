from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey

class SEX(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class OWNER(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class PASTURE(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class SIRE(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class DAM(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name



class SubmitModel(models.Model):
	id=models.AutoField(primary_key=True)
	tagnum=models.SlugField(default=0)
	sex=models.ForeignKey(SEX, on_delete=models.PROTECT, null=True)
	age=models.IntegerField(default=0)
	color=models.CharField(max_length=225)
	comments=models.CharField(max_length=225, default=0)
	sire=models.ForeignKey(SIRE, on_delete=models.PROTECT, null=True)
	dam=models.ForeignKey(DAM, on_delete=models.PROTECT, null=True)
	owner=models.ForeignKey(OWNER, on_delete=models.PROTECT, null=True)
	pasture=models.ForeignKey(PASTURE, on_delete=models.PROTECT, null=True)
	pic=models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100, null=True)
	objects=models.Manager()