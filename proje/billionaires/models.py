from django.db import models

class billionaires_personal(models.Model):
    BillionaireID=models.IntegerField(primary_key=True)
    Age = models.IntegerField()
    Country=models.CharField(max_length=45)
    City=models.CharField(max_length=45)
    PersonName=models.CharField(max_length=45)
    State=models.CharField(max_length=45)
    CountryOfCitizenship=models.CharField(max_length=45)
    Title=models.CharField(max_length=45)
    Gender=models.CharField(max_length=10)
    email=models.CharField(max_length=255)

    class Meta:
        db_table = 'billionaires_personal'

    def __str__(self):
        return self.name

class country_physical(models.Model):
    CountryName = models.CharField(max_length=45,primary_key=True)
    Population=models.IntegerField()
    Latitude = models.FloatField()
    Longitude = models.FloatField()

    def __str__(self):
        return self.country
    class Meta:
        db_table = 'country_physical'

class country_indicators(models.Model):
    Country = models.CharField(max_length=45,primary_key=True)
    cpi=models.FloatField()
    cpiChange=models.FloatField()
    gdp = models.CharField(max_length=45)
    gross_tertiary_education_enrollment=models.FloatField()
    gross_primary_education_enrollment=models.FloatField()
    life_expectancy=models.FloatField()
    tax_revenue=models.FloatField()
    total_tax_rate=models.FloatField()

    def __str__(self):
        return self.country
    class Meta:
        db_table = 'country_indicators'
class billionaireship(models.Model):
    Name=models.CharField(max_length=45,primary_key=True)
    Rank=models.IntegerField()
    FinalWorth = models.IntegerField()
    Source=models.CharField(max_length=45)
    Organization=models.CharField(max_length=65)
    SelfMade=models.CharField(max_length=5)
    Status=models.CharField(max_length=1)
    Industry = models.CharField(max_length=100)

    class Meta:
        db_table = 'billionaireship'
    def __str__(self):
        return self.name

# Your user profile model here if you need additional user fields
