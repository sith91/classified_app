from django import forms

from uploads.core.models import Deals, Category



class DocumentForm(forms.ModelForm):


    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=Category.objects.all())

    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    document = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    # Call attrs with form widget
    expire_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'class':'datepicker','id':'date','type': 'date'}))



    class Meta:
        model = Deals
        fields = ('category','description', 'document','expire_date')

