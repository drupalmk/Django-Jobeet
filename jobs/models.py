from django.db import models

class Categories(models.Model):

    prepopulated_fields = {"slug": ("name",)}

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
    	return self.name

    class Meta:
        db_table = u'categories'


class Jobs(models.Model):

    JOB_TYPES = (
        ('fulltime', 'Full time'),
        ('parttime', 'Part time'),
        ('freelance', 'Freelance'),
    )

    id = models.AutoField(primary_key=True) 
    category = models.ForeignKey(Categories, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPES)
    company = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='jobs', max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=4000)
    how_to_apply = models.TextField(max_length=4000)
    is_public = models.BooleanField()
    is_activated = models.BooleanField()
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()

    def __unicode__(self):
    	return self.company + 'is looking for ' + self.position


    class Meta:
        db_table = u'jobs'
