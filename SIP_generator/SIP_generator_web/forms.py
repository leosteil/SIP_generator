from django import forms
from django.contrib import admin
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import *

class DublinCoreMeta(forms.Form):
	contributor = forms.CharField(max_length=255, required = False)
	coverage = forms.CharField(max_length=255, required = False)
	"""creator = forms.CharField(label="Creator", max_length=255)
	date = forms.DateField(label="Date")
	descripition = forms.CharField(label="Descripiton", max_length=255)
	format_ = forms.CharField(label="Format", max_length=255)
	identifier = forms.CharField(label="Identifier", max_length=255)
	language = forms.CharField(label="Language", max_length=255)
	publisher = forms.CharField(label="Publisher", max_length=255)
	relation = forms.CharField(label="Relation", max_length=255)
	rights = forms.CharField(label="Rights", max_length=255)
	source = forms.CharField(label="Source", max_length=255)
	subject = forms.CharField(label="Subject", max_length=255)
	title = forms.CharField(label="Title", max_length=255)
	type_ = forms.CharField(label="Type", max_length=255)"""

	class Meta:
		model = DublinCoreMetaModel
		fields = ['contributor', 'coverage']

	def save(request):
		if request.method == 'POST':
			form = DublinCoreMeta(request.POST)
			if form.is_valid():
				form.save()
				return Httpresponse("Ok")
			else:
				return Httpresponse("Not Valid")

