from django.db import models


class Person(models.Model):
    positions = (
        ("CEO", 'CEO'),
        ("CTO", 'CTO'),
        ("BigManager", 'BigManager'),
        ("Manager", 'Manager'),
        ("Programmer", 'Programmer'),
    )
    full_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='person/')

    position = models.CharField(max_length=60, choices=positions, default='Programmer')
    date = models.DateTimeField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.full_name

