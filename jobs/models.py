from django.db import models
import uuid

#class JobsManager(models.Manager):

class CategoriesManager(models.Manager):
    def get_with_jobs(self):
        return self.extra(tables=["jobs"],
                          where=["""jobs.category_id = categories.id"""])

class Categories(models.Model):

    prepopulated_fields = {"slug": ("name",)}

    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(max_length=255)

    objects = CategoriesManager()

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

    # def get_file_path(instance, filename):
    #     ext = filename.split('.')[-1]
    #     filename = "%s.%s" % (uuid.uuid4(), ext)
    #     return os.path.join('uploads/jobs/logos', filename)

    id = models.AutoField(primary_key=True) 
    category = models.ForeignKey(Categories, null=True)
    user_id = models.IntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=255, choices=JOB_TYPES)
    company = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='uploads/jobs/logos', max_length=255, blank=True, null=True)
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

    #objects = JobsManager()

    def save(self, *args, **kwargs):
        import datetime
        if not self.id:
            self.created_at = datetime.datetime.now()

            import settings
            self.expires_at = self.created_at + datetime.timedelta(settings.JOB_EXPIRATION_DAY*365/12)
        else:
            self.updated_at = datetime.datetime.now()
        # Call the "real" save() method in the base class 'models.Model'
        super(Jobs, self).save(*args, **kwargs) 


    def __unicode__(self):
    	return self.company + 'is looking for ' + self.position


    class Meta:
        db_table = u'jobs'
