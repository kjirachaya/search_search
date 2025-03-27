from django.db import models

class Specimen(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Principle(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Container(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    collect = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name

class TestRecord(models.Model):
    tags = models.CharField(max_length=255, help_text="Comma-separated tags", blank=True, null=True)
    keywords = models.CharField(max_length=255, help_text="Comma-separated keywords", blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    test_id = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    volumn = models.CharField(max_length=255, blank=True, null=True)
    test_date = models.CharField(max_length=255, blank=True, null=True)
    turn_around_time = models.CharField(max_length=255, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    reference_value = models.CharField(max_length=255, blank=True, null=True)
    specimen = models.ManyToManyField(Specimen, null=True, blank=True)
    principle = models.ManyToManyField(Principle, null=True, blank=True)
    container = models.ManyToManyField(Container, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.test_id + " - " + self.test_name
        
