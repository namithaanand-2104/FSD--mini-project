from django.db import models

class Experiment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

class DataEntry(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    data_label = models.CharField(max_length=100)
    data_value = models.CharField(max_length=100)

class ReportTemplate(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField()

class GeneratedReport(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    template = models.ForeignKey(ReportTemplate, on_delete=models.CASCADE)
    content = models.TextField()
