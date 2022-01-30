from django import forms
from lajme.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'summary_p')