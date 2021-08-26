from django import forms
from drf_braces.serializers.form_serializer import FormSerializer

class MyForm(forms.Form):
    #tagnum = forms.CharField(max_length=32)
    #bar = forms.DateTimeField()
    id=forms.AutoField(primary_key=True)
	tagnum=forms.SlugField(default=0)
	sex=forms.ForeignKey(SEX, on_delete=models.PROTECT, null=True)
	age=forms.IntegerField(default=0)
	color=forms.CharField(max_length=225)
	comments=forms.CharField(max_length=225, default=0)
	sire=forms.SlugField(default=0)
	dam=forms.SlugField(default=0)
	owner=forms.ForeignKey(OWNER, on_delete=models.PROTECT, null=True)
	pasture=forms.ForeignKey(PASTURE, on_delete=models.PROTECT, null=True)
	pic=forms.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100, null=True)

class MySerializer(FormSerializer):
    class Meta(object):
        form = MyForm