from django.db import models

class SubmitModel(models.Model):
	id=models.AutoField(primary_key=True)
	tagnum=models.IntegerField(default=0)
	sex=models.CharField(max_length=225)
	age=models.IntegerField(default=0)
	color=models.CharField(max_length=225)
	comments=models.CharField(max_length=225, default=0)
	sire=models.IntegerField(default=0)
	dam=models.IntegerField(default=0)
	pic=models.FileField(null=True)
	objects=models.Manager()