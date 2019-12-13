from django.shortcuts import render
from documents.models import Document
# Create your views here.
def index(request):
    documents = Document.objects.order_by('name')
    documents_dict = {'documents': documents}
    return render(request, 'documents/index.html', context=documents_dict)