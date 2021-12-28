from django.db import models

# Create your models here.
class SimpleQA(models.Model):
    project = models.CharField(max_length=30,default = ' ')
    test_suite = models.CharField(max_length=10,default= 'CTS')
    key1 = models.CharField(max_length=200)
    key2 = models.CharField(max_length=200)
    failure = models.TextField()
    reason = models.TextField()

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.project,self.test_suite,self.key1,self.key2)
