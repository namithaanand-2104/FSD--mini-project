from django.contrib import admin
from .models import Experiment, DataEntry, ReportTemplate, GeneratedReport

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date')
    search_fields = ('name', 'description')

@admin.register(DataEntry)
class DataEntryAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'data_label', 'data_value')
    search_fields = ('data_label', 'data_value')
    list_filter = ('experiment',)

@admin.register(ReportTemplate)
class ReportTemplateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(GeneratedReport)
class GeneratedReportAdmin(admin.ModelAdmin):
    list_display = ('experiment', 'template')
    search_fields = ('experiment__name', 'template__name')
    list_filter = ('experiment', 'template')
