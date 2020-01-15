from django.db.models import Model, ImageField, CharField, IntegerField, FloatField, URLField

# Create your models here.

class Stock(Model):
    image = ImageField(upload_to='images/')
    name = CharField(max_length=50)
    summary = CharField(max_length=200)
    schemeCode = IntegerField(validators=[MaxValueValidator(199999),MinValueValidator(100000)])
    schemeNumber = CharField(max_length=12)
    folioNumber = CharField(max_length=20)
    schemeName = CharField(max_length=50)
    investAmount = FloatField
    navAmount = FloatField
    siteAddr = URLField(max_length=200)
    curStatus = CharField(max_length=1)
    userName = CharField(max_length=50, null=True, blank=True)
    password = CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.summary