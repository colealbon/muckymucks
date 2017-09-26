import models_generated
from django.db import models

class Source (models.Model):
    File = models.CharField(max_length=200)

class Submission (models.Model):
    Source = models.ForeignKey(Source)
    PrivateToPublic = models.CharField(max_length=200)
    AccessionNumber = models.CharField(max_length=200)
    PublicDocumentCount = models.CharField(max_length=200)
    Timestamp = models.CharField(max_length=200)
    FilingDate = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Deletion = models.CharField(max_length=200)
    Correction = models.CharField(max_length=200)
    DateOfFilingDateChange = models.CharField(max_length=200)
    Period = models.CharField(max_length=200)
    EffectivenessDate = models.CharField(max_length=200)
    ConfirmingCopy = models.CharField(max_length=200)
    Paper = models.CharField(max_length=200)
    ActionDate = models.CharField(max_length=200)
    ReceivedDate = models.CharField(max_length=200)

class FiledFor (models.Model):
    Submission = models.ManyToManyField(Submission)
    pass

class CompanyData (models.Model):
    FiledFor = models.ManyToManyField(FiledFor)
    IrsNumber = models.CharField(max_length=200)
    AssignedSic = models.CharField(max_length=200)
    StateOfIncorporation = models.CharField(max_length=200)
    ConformedName = models.CharField(max_length=200)
    FiscalYearEnd = models.CharField(max_length=200)
    Cik = models.CharField(max_length=200)
    pass

class FilingValues (models.Model):
    FiledFor = models.ManyToManyField(FiledFor)
    FormType = models.CharField(max_length=200)
    Act = models.CharField(max_length=200)
    FilmNumber = models.CharField(max_length=200)
    FileNumber = models.CharField(max_length=200)
    pass

class BusinessAddress (models.Model):
    FiledFor = models.ManyToManyField(FiledFor)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Zip = models.CharField(max_length=200)
    Phone = models.CharField(max_length=200)
    Street1 = models.CharField(max_length=200)
    Street2 = models.CharField(max_length=200)
    pass

class MailAddress (models.Model):
    FiledFor = models.ManyToManyField(FiledFor)
    City = models.CharField(max_length=200)
    State = models.CharField(max_length=200)
    Street2 = models.CharField(max_length=200)
    Zip = models.CharField(max_length=200)
    Street1 = models.CharField(max_length=200)
    pass

class FormerCompany (models.Model):
    FiledFor = models.ManyToManyField(FiledFor)
    FormerConformedName = models.CharField(max_length=200)
    DateChanged = models.CharField(max_length=200)
    pass

class ReportingOwner (models.Model):
    Submission = models.ManyToManyField(Submission)
    FilingValues = models.ManyToManyField(FilingValues)
    MailAddress = models.ManyToManyField(MailAddress)
    BusinessAddress = models.ManyToManyField(BusinessAddress)
    pass

class OwnerData (models.Model):
    ReportingOwner = models.ManyToManyField(ReportingOwner)
    Cik = models.CharField(max_length=200)
    ConformedName = models.CharField(max_length=200)
    StateOfIncorporation = models.CharField(max_length=200)
    FiscalYearEnd = models.CharField(max_length=200)
    AssignedSic = models.CharField(max_length=200)
    pass

class Issuer (models.Model):
    Submission = models.ManyToManyField(Submission)
    CompanyData = models.ManyToManyField(CompanyData)
    BusinessAddress = models.ManyToManyField(BusinessAddress)
    MailAddress = models.ManyToManyField(MailAddress)
    FormerCompany = models.ManyToManyField(FormerCompany)
    pass

class Ownershipdocument (models.Model):
    Source = models.ManyToManyField(Source)
    Issuer = models.ManyToManyField(Issuer)
    Schemaversion = models.CharField(max_length=200)
    Notsubjecttosection16 = models.CharField(max_length=200)
    Periodofreport = models.CharField(max_length=200)
    Documenttype = models.CharField(max_length=200)
    Dateoforiginalsubmission = models.CharField(max_length=200)
    Nosecuritiesowned = models.CharField(max_length=200)
    Form3Holdingsreported = models.CharField(max_length=200)
    Form4Transactionsreported = models.CharField(max_length=200)
    pass

class Reportingowner (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    pass

class Reportingownerid (models.Model):
    Reportingowner = models.ManyToManyField(Reportingowner)
    pass

class Reportingowneraddress (models.Model):
    Reportingowner = models.ManyToManyField(Reportingowner)
    Rptownerstreet1 = models.CharField(max_length=200)
    Rptownercity = models.CharField(max_length=200)
    Rptownerstreet2 = models.CharField(max_length=200)
    Rptownerzipcode = models.CharField(max_length=200)
    Rptownerstate = models.CharField(max_length=200)
    Rptownerstatedescription = models.CharField(max_length=200)
    pass

class Reportingownerrelationship (models.Model):
    Reportingowner = models.ManyToManyField(Reportingowner)
    Istenpercentowner = models.CharField(max_length=200)
    Isother = models.CharField(max_length=200)
    Isdirector = models.CharField(max_length=200)
    Isofficer = models.CharField(max_length=200)
    Officertitle = models.CharField(max_length=200)
    Othertext = models.CharField(max_length=200)
    pass

class Nonderivativetable (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    pass

class Nonderivativetransaction (models.Model):
    Nonderivativetable = models.ManyToManyField(Nonderivativetable)
    pass

class Securitytitle (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    pass

class Transactiondate (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    Value = models.CharField(max_length=200)
    pass

class Transactioncoding (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    Transactioncode = models.CharField(max_length=200)
    Transactionformtype = models.CharField(max_length=200)
    Equityswapinvolved = models.CharField(max_length=200)
    pass

class Transactiontimeliness (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    Value = models.CharField(max_length=200)
    pass

class Value (models.Model):
    Transactiontimeliness = models.ManyToManyField(Transactiontimeliness)
    pass

class Transactionamounts (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    pass

class Transactionshares (models.Model):
    Transactionamounts = models.ManyToManyField(Transactionamounts)
    pass

class Footnoteid (models.Model):
    Transactionshares = models.ManyToManyField(Transactionshares)
    Transactioncoding = models.ManyToManyField(Transactioncoding)
    Securitytitle = models.ManyToManyField(Securitytitle)
    Transactiondate = models.ManyToManyField(Transactiondate)
    Id = models.CharField(max_length=200)
    pass

class Transactionpricepershare (models.Model):
    Transactionamounts = models.ManyToManyField(Transactionamounts)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Transactionacquireddisposedcode (models.Model):
    Transactionamounts = models.ManyToManyField(Transactionamounts)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Posttransactionamounts (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    pass

class Sharesownedfollowingtransaction (models.Model):
    Posttransactionamounts = models.ManyToManyField(Posttransactionamounts)
    Footnoteid = models.ManyToManyField(Footnoteid)
    pass

class Ownershipnature (models.Model):
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    pass

class Directorindirectownership (models.Model):
    Ownershipnature = models.ManyToManyField(Ownershipnature)
    Footnoteid = models.ManyToManyField(Footnoteid)
    pass

class Natureofownership (models.Model):
    Ownershipnature = models.ManyToManyField(Ownershipnature)
    Value = models.ManyToManyField(Value)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Nonderivativeholding (models.Model):
    Nonderivativetable = models.ManyToManyField(Nonderivativetable)
    Securitytitle = models.ManyToManyField(Securitytitle)
    Posttransactionamounts = models.ManyToManyField(Posttransactionamounts)
    Ownershipnature = models.ManyToManyField(Ownershipnature)
    Transactioncoding = models.ManyToManyField(Transactioncoding)
    pass

class Footnotes (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    pass

class Footnote (models.Model):
    Footnotes = models.ManyToManyField(Footnotes)
    Text = models.CharField(max_length=200)
    Id = models.CharField(max_length=200)
    pass

class Ownersignature (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    Signaturename = models.CharField(max_length=200)
    Signaturedate = models.CharField(max_length=200)
    pass

class Filer (models.Model):
    Submission = models.ManyToManyField(Submission)
    CompanyData = models.ManyToManyField(CompanyData)
    FilingValues = models.ManyToManyField(FilingValues)
    BusinessAddress = models.ManyToManyField(BusinessAddress)
    MailAddress = models.ManyToManyField(MailAddress)
    FormerCompany = models.ManyToManyField(FormerCompany)
    pass

class Derivativetable (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    pass

class Derivativetransaction (models.Model):
    Derivativetable = models.ManyToManyField(Derivativetable)
    Securitytitle = models.ManyToManyField(Securitytitle)
    Transactiondate = models.ManyToManyField(Transactiondate)
    Transactioncoding = models.ManyToManyField(Transactioncoding)
    Transactionamounts = models.ManyToManyField(Transactionamounts)
    Posttransactionamounts = models.ManyToManyField(Posttransactionamounts)
    Ownershipnature = models.ManyToManyField(Ownershipnature)
    Transactiontimeliness = models.ManyToManyField(Transactiontimeliness)
    pass

class Conversionorexerciseprice (models.Model):
    Derivativetransaction = models.ManyToManyField(Derivativetransaction)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Exercisedate (models.Model):
    Derivativetransaction = models.ManyToManyField(Derivativetransaction)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Expirationdate (models.Model):
    Derivativetransaction = models.ManyToManyField(Derivativetransaction)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Underlyingsecurity (models.Model):
    Derivativetransaction = models.ManyToManyField(Derivativetransaction)
    pass

class Underlyingsecuritytitle (models.Model):
    Underlyingsecurity = models.ManyToManyField(Underlyingsecurity)
    Footnoteid = models.ManyToManyField(Footnoteid)
    pass

class Underlyingsecurityshares (models.Model):
    Underlyingsecurity = models.ManyToManyField(Underlyingsecurity)
    Footnoteid = models.ManyToManyField(Footnoteid)
    Value = models.CharField(max_length=200)
    pass

class Remarks (models.Model):
    Ownershipdocument = models.ManyToManyField(Ownershipdocument)
    Text = models.CharField(max_length=200)
    pass

class SeriesAndClassesContractsData (models.Model):
    Submission = models.ManyToManyField(Submission)
    pass

class ExistingSeriesAndClassesContracts (models.Model):
    SeriesAndClassesContractsData = models.ManyToManyField(SeriesAndClassesContractsData)
    pass

class Series (models.Model):
    ExistingSeriesAndClassesContracts = models.ManyToManyField(ExistingSeriesAndClassesContracts)
    OwnerCik = models.CharField(max_length=200)
    SeriesName = models.CharField(max_length=200)
    SeriesId = models.CharField(max_length=200)
    pass

class ClassContract (models.Model):
    Series = models.ManyToManyField(Series)
    ClassContractId = models.CharField(max_length=200)
    ClassContractName = models.CharField(max_length=200)
    ClassContractTickerSymbol = models.CharField(max_length=200)
    pass

class Derivativeholding (models.Model):
    Derivativetable = models.ManyToManyField(Derivativetable)
    Securitytitle = models.ManyToManyField(Securitytitle)
    Conversionorexerciseprice = models.ManyToManyField(Conversionorexerciseprice)
    Exercisedate = models.ManyToManyField(Exercisedate)
    Expirationdate = models.ManyToManyField(Expirationdate)
    Underlyingsecurity = models.ManyToManyField(Underlyingsecurity)
    Posttransactionamounts = models.ManyToManyField(Posttransactionamounts)
    Ownershipnature = models.ManyToManyField(Ownershipnature)
    Transactioncoding = models.ManyToManyField(Transactioncoding)
    pass

class FormerName (models.Model):
    ReportingOwner = models.ManyToManyField(ReportingOwner)
    FormerConformedName = models.CharField(max_length=200)
    DateChanged = models.CharField(max_length=200)
    pass

class Deemedexecutiondate (models.Model):
    Derivativetransaction = models.ManyToManyField(Derivativetransaction)
    Nonderivativetransaction = models.ManyToManyField(Nonderivativetransaction)
    Value = models.CharField(max_length=200)
    pass

class SubjectCompany (models.Model):
    Submission = models.ManyToManyField(Submission)
    CompanyData = models.ManyToManyField(CompanyData)
    FilingValues = models.ManyToManyField(FilingValues)
    BusinessAddress = models.ManyToManyField(BusinessAddress)
    MailAddress = models.ManyToManyField(MailAddress)
    FormerCompany = models.ManyToManyField(FormerCompany)
    pass

class FiledBy (models.Model):
    Submission = models.ManyToManyField(Submission)
    CompanyData = models.ManyToManyField(CompanyData)
    FilingValues = models.ManyToManyField(FilingValues)
    BusinessAddress = models.ManyToManyField(BusinessAddress)
    MailAddress = models.ManyToManyField(MailAddress)
    FormerCompany = models.ManyToManyField(FormerCompany)
    pass

class NewSeriesAndClassesContracts (models.Model):
    SeriesAndClassesContractsData = models.ManyToManyField(SeriesAndClassesContractsData)
    OwnerCik = models.CharField(max_length=200)
    pass

class NewClassesContracts (models.Model):
    NewSeriesAndClassesContracts = models.ManyToManyField(NewSeriesAndClassesContracts)
    ClassContract = models.ManyToManyField(ClassContract)
    SeriesName = models.CharField(max_length=200)
    SeriesId = models.CharField(max_length=200)
    pass

class GroupMember (models.Model):
    Submission = models.ManyToManyField(Submission)
    GroupMemberName = models.CharField(max_length=200)
    pass

class Valueownedfollowingtransaction (models.Model):
    Posttransactionamounts = models.ManyToManyField(Posttransactionamounts)
    pass

class NewSeries (models.Model):
    NewSeriesAndClassesContracts = models.ManyToManyField(NewSeriesAndClassesContracts)
    ClassContract = models.ManyToManyField(ClassContract)
    SeriesName = models.CharField(max_length=200)
    SeriesId = models.CharField(max_length=200)
    pass

class Transactiontotalvalue (models.Model):
    Transactionamounts = models.ManyToManyField(Transactionamounts)
    pass

class Rptownerstate (models.Model):
    Reportingowneraddress = models.ManyToManyField(Reportingowneraddress)
    pass

class Othertext (models.Model):
    Reportingownerrelationship = models.ManyToManyField(Reportingownerrelationship)
    pass

class Officertitle (models.Model):
    Reportingownerrelationship = models.ManyToManyField(Reportingownerrelationship)
    pass

class Underlyingsecurityvalue (models.Model):
    Underlyingsecurity = models.ManyToManyField(Underlyingsecurity)
    Value = models.CharField(max_length=200)
    pass

class MergerSeriesAndClassesContracts (models.Model):
    SeriesAndClassesContractsData = models.ManyToManyField(SeriesAndClassesContractsData)
    pass

class Merger (models.Model):
    MergerSeriesAndClassesContracts = models.ManyToManyField(MergerSeriesAndClassesContracts)
    pass

class AcquiringData (models.Model):
    Merger = models.ManyToManyField(Merger)
    Series = models.ManyToManyField(Series)
    Cik = models.CharField(max_length=200)
    pass

class TargetData (models.Model):
    Merger = models.ManyToManyField(Merger)
    Series = models.ManyToManyField(Series)
    Cik = models.CharField(max_length=200)
    pass

class Signaturename (models.Model):
    Ownersignature = models.ManyToManyField(Ownersignature)
    pass

class Transactionformtype (models.Model):
    Transactioncoding = models.ManyToManyField(Transactioncoding)
    pass
