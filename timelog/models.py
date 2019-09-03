from django.db import models
from django.conf import settings

# Create your models here.


class TimeLog(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    CICO_STATUS = (('Check In', 'CHECK IN'), ('Check Out', 'CHECK OUT'),)  # chocies for the CI_CO FIELD
    CI_CO = models.CharField('Check In/Check Out', max_length=50, choices=CICO_STATUS)

    def __str__(self):
        return f'{self.user_id} | {self.CI_CO} | {self.date} | {self.time}'
