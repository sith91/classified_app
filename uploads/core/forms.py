from django import forms
from clever_selects.forms import ChainedModelChoiceField
from django.urls import reverse_lazy

from uploads.core.models import Deals, Category, SubCategory


class DocumentForm(forms.ModelForm):


    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=Category.objects.all())

    subcategory = ChainedModelChoiceField(parent_field='category', ajax_url=reverse_lazy('ajax_chained_models'),
        empty_label=(u'Select Sub Category'), model=SubCategory, required=True, widget=forms.Select(attrs={'class':'form-control'}))

    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    # Call attrs with form widget
    expire_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'class':'datepicker','id':'date','type': 'date'}))


    class Meta:
        model = Deals
        fields = ('category', 'subcategory', 'description', 'document', 'expire_date')

