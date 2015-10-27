from django import forms
from branch_change.models import userpost
#from branch_change.models import loginpost
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from branch_change.models import allocated_branch

from branch_change.models import branch_stats

class userpostform(forms.ModelForm):
	ge='GE'
	obc='OBC'
	sc='SC'
	st='ST'
	
	CATEGORY_LIST = ((ge,ge),(obc,obc),(sc,sc),(st,st),)

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

	BRANCH_LIST = (('',none),(aebtech,aebtech),(cebtech,cebtech),(ch,ch),(clbtech,clbtech),(cldualdeg,cldualdeg),(csbtech,csbtech),(eebtech,eebtech),(eedualdege1,eedualdege1),(eedualdege2,eedualdege2),(endualdeg,endualdeg),(epbtech,epbtech),(epdualdegn1,epdualdegn1),(mebtech,mebtech),(medualdegm2,medualdegm2),(mmbtech,mmbtech),(mmdualdegy1,mmdualdegy1),(mmdualdegy2,mmdualdegy2),)

	category = forms.ChoiceField(choices = CATEGORY_LIST, required = True , widget=forms.Select(attrs={'class':'form-control'}))
	present_branch = forms.ChoiceField(choices = BRANCH_LIST , required = True , widget=forms.Select(attrs={'class':'form-control'}))
	pref1 = forms.ChoiceField(choices = BRANCH_LIST , required = True , widget=forms.Select(attrs={'class':'form-control'}))
	pref2 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref3 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref4 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref5 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref6 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref7 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref8 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref9 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref10 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref11 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref12 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref13 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref14 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))
	pref15 = forms.ChoiceField(choices = BRANCH_LIST , required = False , widget=forms.Select(attrs={'class':'form-control'}))

	

	class Meta:
		model = userpost
		fields = ('user_name','roll_number','name','category','present_branch','cpi','pref1','pref2','pref3','pref4','pref5','pref6','pref7','pref8','pref9','pref10','pref11','pref12','pref13','pref14','pref15')
		widgets = { 'user_name':forms.TextInput(attrs={'class':'form-control','readonly': 'True' ,'style':'display:none'}),'name':forms.TextInput(attrs={'placeholder':'Name','class':'form-control'}), 'roll_number':forms.TextInput(attrs={'placeholder': 'Valid Roll No 15XXXXXXX' , 'class':'form-control'}), 'cpi':forms.TextInput(attrs={'placeholder':'Valid CPI in [0,10] only','class':'form-control'}),'present_branch':forms.TextInput(attrs={'placeholder':'','class':'form-control'}),}
		
'''
class loginpostform(forms.ModelForm):
	class Meta:
		model = loginpost
		fields = ('username','password')
		widgets = { 'username':forms.TextInput(attrs={'placeholder':'username','class':'form-control'}),'password':forms.TextInput(attrs={'placeholder':'password','class':'form-control'}),}



class userform(forms.ModelForm):
	class Meta:
		model = userpost

class userprofileform(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude = ['user']


class usercreateform(UserCreationForm):
	class Meta:
		model = User
		fields = ('username','password1','password2')

	def save(self,commit=True):
		user = super(usercreateform,self).save(commit=False)
		if commit:
			user.save()
		return user

'''


# class adminfileform(forms.ModelForm):
# 	file = forms.FileField()

# 	class Meta:
# 		model = adminfile
# 		fields = ('file',)



class allocated_branchform(forms.ModelForm):
	roll_number = forms.CharField(max_length = 9)
	name = forms.CharField(max_length = 100)
	initial_branch = forms.CharField(max_length = 25)
	alloted_branch = forms.CharField(max_length = 25)

	class Meta:
		model = allocated_branch
		fields = ('roll_number','name','initial_branch','alloted_branch')


class branch_statsform(forms.ModelForm):
	branch_name = forms.CharField(max_length = 25)
	cutoff = forms.CharField(max_length = 10)
	sanctioned_st = forms.CharField(max_length=10)
	original_st = forms.CharField(max_length=10)
	final_st = forms.CharField(max_length=10)

	class Meta:
		model = branch_stats
		fields = ('branch_name','cutoff','sanctioned_st','original_st','final_st')


# class branch_statsform(forms.ModelForm):
# 	branch_name = forms.CharField(max_length = 25)
# 	cutoff = forms.DecimalField(max_digits=10, decimal_places=5)
# 	sanctioned_st = forms.IntegerField()
# 	original_st = forms.IntegerField()
# 	final_st = forms.IntegerField()

# 	class Meta:
# 		model = branch_stats
# 		fields = ('branch_name','cutoff','sanctioned_st','original_st','final_st')