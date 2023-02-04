from django.db import models
from django.conf import settings
from django.core.validators import FileExtensionValidator

# Create your models here.


def userDirectoryPath(uname, file):
	return 'user_{0}/{1}'.format(uname, file)

class FileUpload(models.Model):

	#uname = models.CharField(default='', max_length=100)

	file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['txt'])])
	


