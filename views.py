from django.shortcuts import render, redirect
from .forms import ExperimentForm, DataEntryForm, ReportTemplateForm
from .models import Experiment, DataEntry, ReportTemplate, GeneratedReport

def create_experiment(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_experiments')
    else:
        form = ExperimentForm()
    return render(request, 'reports/create_experiment.html', {'form': form})

def list_experiments(request):
    experiments = Experiment.objects.all()
    return render(request, 'reports/list_experiments.html', {'experiments': experiments})

def add_data_entry(request, experiment_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            data_entry = form.save(commit=False)
            data_entry.experiment = experiment
            data_entry.save()
            return redirect('list_experiments')
    else:
        form = DataEntryForm()
    return render(request, 'reports/add_data_entry.html', {'form': form, 'experiment': experiment})

def create_template(request):
    if request.method == 'POST':
        form = ReportTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_templates')
    else:
        form = ReportTemplateForm()
    return render(request, 'reports/create_template.html', {'form': form})

def list_templates(request):
    templates = ReportTemplate.objects.all()
    return render(request, 'reports/list_templates.html', {'templates': templates})

def generate_report(request, experiment_id, template_id):
    experiment = Experiment.objects.get(pk=experiment_id)
    template = ReportTemplate.objects.get(pk=template_id)
    data_entries = DataEntry.objects.filter(experiment=experiment)

    report_content = template.template.format(
        experiment_name=experiment.name,
        experiment_description=experiment.description,
        experiment_date=experiment.date,
        data_entries=data_entries
    )

    generated_report = GeneratedReport(
        experiment=experiment,
        template=template,
        content=report_content
    )
    generated_report.save()

    return render(request, 'reports/view_report.html', {'report': generated_report})
def index(request):
    return redirect('list_experiments')
