from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class LinksManager(models.Manager):
    def build_link(self,url):
        link = self.create(url=url)
        link.save()
        return True,link.index

    def get_url(self,index):
        try:
            link = self.get(index=index)
        except ObjectDoesNotExist:
            return False,"请检查短链是否正确"
        return True,link.url

class Links(models.Model):
    index = models.AutoField(verbose_name="短链",unique=True,primary_key=True)
    url = models.CharField(verbose_name="目标url",max_length=255)

    objects = LinksManager()