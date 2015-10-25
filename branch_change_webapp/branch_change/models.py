from django.db import models

# Create your models here.

class userpost(models.Model):
	ge='GE'
	obc='OBC'
	sc='SC'
	st='ST'
	
	CATEGORY_LIST = (('ge',ge),('obc',obc),('sc',sc),('st',st),)

	none = 'none'
	aebtech ='AE B.Tech'
	cebtech ='CE B.Tech'
	ch ='CH'
	clbtech ='CL B.Tech'
	cldualdeg ='CL Dual Deg'
	csbtech ='CS B.Tech'
	eebtech ='EE B.Tech'
	eedualdege1 ='EE Dual Deg E1'
	eedualdege2 ='EE Dual Deg E2'
	endualdeg ='EN Dual Deg'
	epbtech ='EP B.Tech'
	epdualdegn1 ='EP Dual Deg N1'
	mebtech ='ME B.Tech'
	medualdegm2 ='ME Dual Deg M2'
	mmbtech ='MM B.Tech'
	mmdualdegy1 ='MM Dual Deg Y1'
	mmdualdegy2 ='MM Dual Deg Y2'	

	BRANCH_LIST = (('',none),('aebtech',aebtech),('cebtech',cebtech),('ch',ch),('clbtech',clbtech),('cldualdeg',cldualdeg),('csbtech',csbtech),('eebtech',eebtech),('eedualdege1',eedualdege1),('eedualdege2',eedualdege2),('endualdeg',endualdeg),('epbtech',epbtech),('epdualdegn1',epdualdegn1),('mebtech',mebtech),('medualdegm2',medualdegm2),('mmbtech',mmbtech),('mmdualdegy1',mmdualdegy1),('mmdualdegy2',mmdualdegy2),)

	user_name = models.CharField(max_length = 100 , verbose_name = '')
	roll_number = models.CharField( max_length = 9 , verbose_name='Roll No')
	name = models.CharField( max_length = 100 ,verbose_name='Name')
	present_branch = models.CharField( max_length = 25 ,verbose_name='Present Branch', choices = BRANCH_LIST )
	category = models.CharField( max_length = 5 ,verbose_name='Category' , choices= CATEGORY_LIST , default = 'GE')
	cpi = models.DecimalField( max_digits = 5, decimal_places=2,verbose_name = 'CPI' )
	pref1 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 1' , choices = BRANCH_LIST )
	pref2 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 2' , choices = BRANCH_LIST )
	pref3 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 3' , choices = BRANCH_LIST )
	pref4 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 4' , choices = BRANCH_LIST )
	pref5 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 5' , choices = BRANCH_LIST )
	pref6 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 6' , choices = BRANCH_LIST )
	pref7 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 7' , choices = BRANCH_LIST )
	pref8 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 8' , choices = BRANCH_LIST )
	pref9 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 9' , choices = BRANCH_LIST )
	pref10 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 10' , choices = BRANCH_LIST )
	pref11 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 11' , choices = BRANCH_LIST )
	pref12 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 12' , choices = BRANCH_LIST )
	pref13 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 13' , choices = BRANCH_LIST )

	pref14 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 14' , choices = BRANCH_LIST )
	pref15 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 15' , choices = BRANCH_LIST )
	pref16 = models.CharField( max_length = 25 , verbose_name = 'Wish to go to Pref 16' , choices = BRANCH_LIST )	

	def __str__(self):
		return self.user_name

'''
class loginpost(models.Model):
	username = models.CharField(max_length = 100 ,verbose_name='username')
	password = models.CharField(max_length = 100 ,verbose_name='password')
'''


