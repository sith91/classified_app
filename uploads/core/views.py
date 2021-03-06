from clever_selects.views import ChainedSelectChoicesView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from uploads.core.models import Deals, SubCategory
from uploads.core.forms import DocumentForm
from uploads.core.serializers import DealSerializer


class PromiseCreateView(CreateView):
    model = Deals
    form_class = DocumentForm


def home(request):
    deal = Deals.objects.all()

    return render(request, 'home.html',{
        'deal': deal
    })

class AjaxChainedView(ChainedSelectChoicesView):
    def get_child_set(self):
        return SubCategory.object.filter(catego=self.parent_value)

"""def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')
"""

@login_required(login_url="/login/")
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
                instance = form.save(commit= False)
                instance.vendor_deal= request.user
                instance.save()
                return redirect('http://127.0.0.1:8000/')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })


class DealViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Deals.objects.all()
    serializer_class = DealSerializer