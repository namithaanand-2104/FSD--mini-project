from django import forms
from .models import Experiment, DataEntry, ReportTemplate

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description', 'date']

class DataEntryForm(forms.ModelForm):
    class Meta:
        model = DataEntry
        fields = ['data_label', 'data_value']

class ReportTemplateForm(forms.ModelForm):
    class Meta:
        model = ReportTemplate
        fields = ['name', 'template']
