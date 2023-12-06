from django.db import models

class Billionaire(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class CountryPhysical(models.Model):
    country = models.CharField(max_length=100)
    population=models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.country

class CountryEconomic(models.Model):
    country = models.CharField(max_length=100)
    cpi_country=models.FloatField()
    cpi_change_country=models.FloatField()
    gross_tertiary_education_enrollment=models.FloatField()
    gross_primary_education_enrollment_country=models.FloatField()
    life_expectancy_country=models.FloatField()
    tax_revenue_country_country=models.FloatField()
    total_tax_rate_country=models.FloatField()
    gdp = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.country

class BillionaireEconomic(models.Model):
    rank=models.IntegerField()
    selfmade=models.BooleanField()
    final_worth = models.DecimalField(max_digits=20, decimal_places=2)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    country = models.ForeignKey(CountryPhysical, on_delete=models.CASCADE)
    organization=models.CharField(max_length=100)
    source=models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Your user profile model here if you need additional user fields
