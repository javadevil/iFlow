from django.db import models

class Journal(models.Model):
	"""Journal model is the header of journal represent title of journal for general ledger"""
	name 		= models.CharField(blank=False, max_length=100)
	description = models.TextField(blank=True)
	
class Code(models.Model):
	"""Code model is use for store accounting code maximum code is 10 digit"""
	code  		= models.CharField(blank=False, max_length=10)
	description = models.CharField(blank=False, max_length=140)
	
class Statement(models.Model):
	"""Statement represent data in very small term of debit and credit"""
	journal 	= models.ForeignKey(Journal)
	code 		= models.ForeignKey(Code)
	description = models.CharField(blank=False, max_length=140)
	debit 		= models.FloatField()
	credit 		= models.FloatField()
	stamp		= models.DateTimeField(auto_now_add=True)
	