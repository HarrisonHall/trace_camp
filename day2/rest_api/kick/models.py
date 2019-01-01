from django.db import models
import csv

class KickstarterTypes(models.Model):
    backers_count=models.IntegerField()
    blurb=models.TextField()
    '''
    category=models.TextField()
    converted_pledged_amount=models.IntegerField()
    country=models.TextField()
    created_at=models.TextField() #date?
    creator=models.TextField()
    currency=models.TextField()
    deadline=models.TextField() #date
    disable_communication=models.BooleanField()
    fx_rate=models.FloatField()
    goal=models.FloatField()
    kickstarter_id=models.IntegerField()
    launched_at=models.TextField() #date
    location=models.TextField()
    name=models.TextField()
    photo=models.TextField()
    pledged=models.FloatField()
    profile=models.TextField()
    slug=models.TextField()
    source_url=models.URLField()
    spotlight=models.BooleanField()
    staff_pick=models.BooleanField()
    state=models.TextField()
    state_changed_at=models.TextField() #date
    static_usd_rate=models.FloatField()
    urls=models.TextField()
    usd_pledged=models.FloatField()
    usd_type=models.TextField()
    '''

