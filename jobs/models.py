from django.db import models

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    slug = models.CharField(max_length=255)
    class Meta:
        db_table = u'categories'

class Jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(Categories, null=True)
    user_id = models.IntegerField(null=True)
    job_type = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    logo = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=4000)
    how_to_apply = models.CharField(max_length=4000)
    is_public = models.IntegerField()
    is_activated = models.IntegerField()
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    class Meta:
        db_table = u'jobs'
