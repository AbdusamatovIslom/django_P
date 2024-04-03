from django.db import models




# docker start 1a9
# docker exec -itu 81 psql
# docker exec -it 1a9 sh
# su postgres
# psql


class Project(models.Model):
    name = models.CharField(max_length=155)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=155)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField()