from django.db import models

class billionaires_personal(models.Model):
    BillionaireId=models.IntegerField()
    Age = models.IntegerField()
    Country=models.CharField(max_length=45)
    City=models.CharField(max_length=45)
    PersonName = models.CharField(max_length=45)
    State=models.CharField(max_length=45)
    CountryOfCitizenship=models.CharField(max_length=45)
    Title=models.CharField(max_length=45)
    Gender = models.CharField(max_length=10)
    email=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class country_physical(models.Model):
    CountryName = models.CharField(max_length=100)
    Population=models.IntegerField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.country

class country_indicators(models.Model):
    Country = models.CharField(max_length=100)
    Cpi_country=models.FloatField()
    cpi_change_country=models.FloatField()
    gross_tertiary_education_enrollment=models.FloatField()
    gross_primary_education_enrollment_country=models.FloatField()
    life_expectancy_country=models.FloatField()
    tax_revenue_country_country=models.FloatField()
    total_tax_rate_country=models.FloatField()
    gdp = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.country

class billionaireship(models.Model):
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
