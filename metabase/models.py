from django.db import models
from datetime import datetime





class metamodels(models.Model):

    UserId = models.ForeignKey('user_ivin.UserIvinModel', related_name='Metabase', on_delete=models.CASCADE,default=True)
    QuestionId = models.IntegerField()
    Sequence = models.IntegerField()
    Createdby = models.CharField(max_length=200)
    Updatedby = models.CharField(max_length=200)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)

    objects = models.Manager



    class Meta:
        db_table = "Metabase_post"
