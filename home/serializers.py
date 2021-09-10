from django import forms
from drf_braces.serializers.form_serializer import FormSerializer

class MyForm(forms.Form):
    #tagnum = forms.CharField(max_length=32)
    #bar = forms.DateTimeField()
	sex=forms.ForeignKey(SEX, on_delete=models.PROTECT, null=True)
	owner=forms.ForeignKey(OWNER, on_delete=models.PROTECT, null=True)
	pasture=forms.ForeignKey(PASTURE, on_delete=models.PROTECT, null=True)

class MySerializer(FormSerializer):
    class Meta(object):
        form = MyForm