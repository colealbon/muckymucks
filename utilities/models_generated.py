from django.db import models
class Source (models.Model):
    File = models.CharField(max_length=200)
    pass

class Submission (models.Model):
    Source = models.ManyToManyField(Source)
    PublicDocumentCount = models.CharField(max_length=200)
    Period = models.CharField(max_length=200)
    AccessionNumber = models.CharField(max_length=200)
    DateOfFilingDateChange = models.CharField(max_length=200)
    FilingDate = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    pass

class Filer (models.Model):
    Submission = models.ManyToManyField(Submission)
    pass

class CompanyData (models.Model):
    Filer = models.ManyToManyField(Filer)
    FiscalYearEnd = models.CharField(max_length=200)
    Cik = models.CharField(max_length=200)
    IrsNumber = models.CharField(max_length=200)
    StateOfIncorporation = models.CharField(max_length=200)
    ConformedName = models.CharField(max_length=200)
    AssignedSic = models.CharField(max_length=200)
    pass

class FilingValues (models.Model):
    Filer = models.ManyToManyField(Filer)
    FormType = models.CharField(max_length=200)
    FileNumber = models.CharField(max_length=200)
    FilmNumber = models.CharField(max_length=200)
    Act = models.CharField(max_length=200)
    pass

class BusinessAddress (models.Model):
    Filer = models.ManyToManyField(Filer)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Zip = models.CharField(max_length=200)
    Street1 = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    pass

