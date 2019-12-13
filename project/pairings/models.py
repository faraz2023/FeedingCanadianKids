from django.db import models
# from profiles.models import Restaurant, Program, Schedule
# Create your models here.

class Pairing(models.Model):
    created_at = models.DateTimeField()
    restaurant_id = models.ForeignKey('profiles.Restaurant', related_name='restaurant',\
                                      on_delete=models.DO_NOTHING)
    program_id = models. ForeignKey('profiles.Program', related_name="program",\
                                    on_delete=models.DO_NOTHING)
    schedule_id = models.ForeignKey('profiles.Schedule', related_name='schedule',\
                                    on_delete=models.DO_NOTHING)

