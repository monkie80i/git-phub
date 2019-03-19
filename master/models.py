from django.db import models
from django.contrib.auth.models import User
from master.choices import *


# Create your models here.
class TypeContent(models.Model):
	#"_p" atributes are for premium members
	typ=models.CharField(max_length=4)
	intro=models.TextField()
	intro_p=models.TextField()
	jung_pref=models.TextField()
	strength=models.TextField()
	strength_p=models.TextField()
	weakness=models.TextField()
	weakness_p=models.TextField()
	success=models.TextField()
	s2f=models.TextField()
	pot_prob=models.TextField()
	solns=models.TextField()
	living_happy=models.TextField()
	rules=models.TextField()
	rules_p=models.TextField() 
	create_date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.typ
	
class TestAnswer(models.Model):
	a1=models.CharField(choices=CH1,max_length=1)
	a2=models.CharField(choices=CH2,max_length=1)
	a3=models.CharField(choices=CH3,max_length=1)
	a4=models.CharField(choices=CH4,max_length=1)
	a5=models.CharField(choices=CH5,max_length=1)
	a6=models.CharField(choices=CH6,max_length=1)
	a7=models.CharField(choices=CH7,max_length=1)
	a8=models.CharField(choices=CH8,max_length=1) 
	a9=models.CharField(choices=CH9,max_length=1)
	a10=models.CharField(choices=CH10,max_length=1)
	a11=models.CharField(choices=CH11,max_length=1)
	a12=models.CharField(choices=CH12,max_length=1)
	a13=models.CharField(choices=CH13,max_length=1) 
	a14=models.CharField(choices=CH14,max_length=1)
	a15=models.CharField(choices=CH15,max_length=1) 
	a16=models.CharField(choices=CH16,max_length=1) 
	a17=models.CharField(choices=CH17,max_length=1) 
	a18=models.CharField(choices=CH18,max_length=1) 
	a19=models.CharField(choices=CH19,max_length=1)
	a20=models.CharField(choices=CH20,max_length=1) 
	a21=models.CharField(choices=CH21,max_length=1)
	a22=models.CharField(choices=CH22,max_length=1)
	a23=models.CharField(choices=CH23,max_length=1)
	a24=models.CharField(choices=CH24,max_length=1)
	a25=models.CharField(choices=CH25,max_length=1)
	a26=models.CharField(choices=CH26,max_length=1)
	a27=models.CharField(choices=CH27,max_length=1)
	a28=models.CharField(choices=CH28,max_length=1)
	a29=models.CharField(choices=CH29,max_length=1)
	a30=models.CharField(choices=CH30,max_length=1)
	a31=models.CharField(choices=CH31,max_length=1)
	a32=models.CharField(choices=CH32,max_length=1)
	a33=models.CharField(choices=CH33,max_length=1)
	a34=models.CharField(choices=CH34,max_length=1)
	a35=models.CharField(choices=CH35,max_length=1)
	a36=models.CharField(choices=CH36,max_length=1)
	a37=models.CharField(choices=CH37,max_length=1)
	a38=models.CharField(choices=CH38,max_length=1)
	a39=models.CharField(choices=CH39,max_length=1)
	a40=models.CharField(choices=CH40,max_length=1)
	a41=models.CharField(choices=CH41,max_length=1)
	a42=models.CharField(choices=CH42,max_length=1)
	a43=models.CharField(choices=CH43,max_length=1)
	a44=models.CharField(choices=CH44,max_length=1)
	a45=models.CharField(choices=CH45,max_length=1)
	a46=models.CharField(choices=CH46,max_length=1)
	a47=models.CharField(choices=CH47,max_length=1)
	a48=models.CharField(choices=CH48,max_length=1)
	a49=models.CharField(choices=CH49,max_length=1)
	a50=models.CharField(choices=CH50,max_length=1)
	a51=models.CharField(choices=CH51,max_length=1)
	a52=models.CharField(choices=CH52,max_length=1)
	a53=models.CharField(choices=CH53,max_length=1)
	a54=models.CharField(choices=CH54,max_length=1)
	a55=models.CharField(choices=CH55,max_length=1)
	a56=models.CharField(choices=CH56,max_length=1)
	a57=models.CharField(choices=CH57,max_length=1)
	a58=models.CharField(choices=CH58,max_length=1)
	a59=models.CharField(choices=CH59,max_length=1)
	a60=models.CharField(choices=CH60,max_length=1)
	a61=models.CharField(choices=CH61,max_length=1)
	a62=models.CharField(choices=CH62,max_length=1)
	a63=models.CharField(choices=CH63,max_length=1)
	a64=models.CharField(choices=CH64,max_length=1)
	a65=models.CharField(choices=CH65,max_length=1)
	a66=models.CharField(choices=CH66,max_length=1)
	a67=models.CharField(choices=CH67,max_length=1)
	a68=models.CharField(choices=CH68,max_length=1)
	a69=models.CharField(choices=CH69,max_length=1)
	a70=models.CharField(choices=CH70,max_length=1)

	def __str__(self):
		return str(self.pk)

class TestResult(models.Model):
	answer_id=models.ForeignKey(TestAnswer)
	extraversion=models.DecimalField(max_digits=6,decimal_places=3)
	introversion=models.DecimalField(max_digits=6,decimal_places=3)
	intuition=models.DecimalField(max_digits=6,decimal_places=3)
	sensing=models.DecimalField(max_digits=6,decimal_places=3)
	feeling=models.DecimalField(max_digits=6,decimal_places=3)
	thinking=models.DecimalField(max_digits=6,decimal_places=3)
	percieving=models.DecimalField(max_digits=6,decimal_places=3)
	judging=models.DecimalField(max_digits=6,decimal_places=3)
	abbrev=models.CharField(max_length=4)
	type_id=models.ForeignKey(TypeContent)
	create_date=models.DateTimeField(auto_now=True)
	user_id=models.ForeignKey(User,default=0)
	#geo_id=models.ForeignKey(Geolocation)
	def __str__(self):
		return str(self.pk)

#class Geolocation(models.Model):
#	lat=models.DecimalField()
#	lon=models.DecimalField()	


class MyUser(models.Model):
    user_data = models.OneToOneField(User)
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.place 