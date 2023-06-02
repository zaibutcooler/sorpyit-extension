from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Country(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

# class Currency(models.Model):
# 	name=models.CharField(max_length=100)
# 	country=models.ForeignKey(Country,on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.name

class Keyword(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name

class JobOffer(models.Model):

	CURRENCY_CHOICES = (
        ("Dollar", 'Dollar'),
        ("Yenn", 'Yenn'),
        ("Euro", 'Euro'),
        ("Yuan", 'Yuan'),
        ("Kyats", 'Kyats'),

    )
	currency = models.CharField(max_length=100,choices=CURRENCY_CHOICES)
	uploader=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	description=models.TextField(null=True,blank=True)
	country=models.ForeignKey(Country,on_delete=models.CASCADE)
	city=models.CharField(max_length=100)
	salary=models.IntegerField()
	onsite=models.BooleanField()
	requirements=models.TextField()
	responsibilities=models.TextField(null=True,blank=True)
	email=models.EmailField()
	phonenumber=models.CharField(max_length=15)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class JobApply(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	joboffer=models.ForeignKey(JobOffer,on_delete=models.CASCADE)
	created=models.DateTimeField(auto_now_add=True)











# const mongoose = require("mongoose");
# const jobSchema = new mongoose.Schema({
#   title: { type: String, require: true },
#   description: { type: String },
#   salary: {
#     amount: { type: Number, require: true },
#     currency: { type: String },
#   },
#   onsite: { type: Boolean, require: true },
#   location: { type: String, require: true },
#   requirements: [{ type: String }],
#   responsibilities: { type: [String] },
#   contactEmail: { type: String, require: true },
#   createdAt: { type: Date, default: Date.now },
# });

# module.exports = mongoose.model("Job", jobSchema);