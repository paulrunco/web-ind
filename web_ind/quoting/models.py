from django.db import models

class Customer(models.Model):
    name = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.TextField(max_length=80)
    last_name = models.TextField(max_length=80)
    email = models.EmailField()


class Quote(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    creation_date = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return '{:08d} {}'.format(self.id, self.customer)

    class Status(models.TextChoices):
        DRAFT = ('DRAFT', 'Draft')
        APPROVED = ('APPROVED','Approved')
        SENT = ('SENT', 'Sent')

    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.DRAFT)

class Line(models.Model):
    number = models.IntegerField()
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE)
    part = models.TextField(max_length=100)
    revision = models.TextField(max_length=8)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    unit = models.TextField(max_length=2)

    def __str__(self) -> str:
        return f"{self.part} / {self.revision}"



    