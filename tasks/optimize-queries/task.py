from django.db import models


class Address(models.Model):
    city = models.CharField()


class Department(models.Model):
    name = models.CharField()


class User(models.Model):
    name = models.CharField()
    email = models.CharField()
    address = models.ForeignKey(Address)
    departments = models.ManyToManyField(Department)


for user in User.objects.filter(email__endswith="@gmail.com"):
    print(user.address.city)

for user in User.objects.filter(email__endswith="@gmail.com"):
    print([dep.name for dep in user.departments.all()])
