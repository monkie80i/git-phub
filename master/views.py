from django.shortcuts import render
from django.views.generic import View,ListView,FormView
from master.forms import TestForm,SignUpForm
from master.shcripts import numberd
from master.models import TestAnswer,TestResult,TypeContent,MyUser
from django.contrib.auth.models import User
from django.shortcuts import redirect

from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test



# Create your views here.
class HomeView(View):
	template_name="home.html"
	def get(self,request):
		if request.user.is_staff or request.user.is_superuser :
			return render(request,self.template_name,{'value': 1})
		else:
			return render(request,self.template_name,{'value':10})

class MbtiView(View):
	template_name="mbti.html"
	def get(self,request):
		if request.user.is_staff or request.user.is_superuser :
			return render(request,self.template_name,{'value': 1})
		else:
			return render(request,self.template_name,{'value':10})	

class PersonalitiesView(View):
	template_name="16personalities.html"
	def get(self,request):
		if request.user.is_staff or request.user.is_superuser :
			return render(request,self.template_name,{'value': 1})
		else:
			return render(request,self.template_name,{'value':10})	

class ResourcesView(View):
	template_name="resources.html"
	def get(self,request):
		if request.user.is_staff or request.user.is_superuser :
			return render(request,self.template_name,{'value': 1})
		else:
			return render(request,self.template_name,{'value':10})	

class AboutView(View):
	template_name="about.html"
	def get(self,request):
		if request.user.is_staff or request.user.is_superuser :
			return render(request,self.template_name,{'value': 1})
		else:
			return render(request,self.template_name,{'value':10})	

			

class TestView(View):
	template_name="test.html"
	form_class=TestForm

	def get(self,request):
		form=self.form_class(initial={'ch1':'a','ch2':'a','ch3':'a','ch4':'a','ch5':'a','ch6':'a','ch7':'a','ch8':'a','ch9':'a','ch10':'a','ch11':'a','ch12':'a','ch13':'a','ch14':'a','ch15':'a','ch16':'a','ch17':'a','ch18':'a','ch19':'a','ch20':'a','ch21':'a','ch22':'a','ch23':'a','ch24':'a','ch25':'a','ch26':'a','ch27':'a','ch28':'a','ch29':'a','ch30':'a','ch31':'a','ch32':'a','ch33':'a','ch34':'a','ch35':'a','ch36':'a','ch37':'a','ch38':'a','ch39':'a','ch40':'a','ch41':'a','ch42':'a','ch43':'a','ch44':'a','ch45':'a','ch46':'a','ch47':'a','ch48':'a','ch49':'a','ch50':'a','ch51':'a','ch52':'a','ch53':'a','ch54':'a','ch55':'a','ch56':'a','ch57':'a','ch58':'a','ch59':'a','ch60':'a','ch61':'a','ch62':'a','ch63':'a','ch64':'a','ch65':'a','ch66':'a','ch67':'a','ch68':'a','ch69':'a','ch70':'a',})
		if request.user.is_staff or request.user.is_superuser :
			context={'form':form,'value': 1}
		else:
			context={'form':form,'value':10}
		
		return render(request,self.template_name,context)

	def post(self,request):
		form=self.form_class(request.POST)
		if form.is_valid():
			ans1=request.POST.get('ch1')			
			ans2=request.POST.get('ch2') 
			ans3=request.POST.get('ch3')
			ans4=request.POST.get('ch4')
			ans5=request.POST.get('ch5')
			ans6=request.POST.get('ch6')
			ans7=request.POST.get('ch7')
			ans8=request.POST.get('ch8')
			ans9=request.POST.get('ch9')
			ans10=request.POST.get('ch10')
			ans11=request.POST.get('ch11')
			ans12=request.POST.get('ch12')
			ans13=request.POST.get('ch13') 
			ans14=request.POST.get('ch14')
			ans15=request.POST.get('ch15') 
			ans16=request.POST.get('ch16') 
			ans17=request.POST.get('ch17') 
			ans18=request.POST.get('ch18') 
			ans19=request.POST.get('ch19')
			ans20=request.POST.get('ch20')
			ans21=request.POST.get('ch21')
			ans22=request.POST.get('ch22')
			ans23=request.POST.get('ch23')
			ans24=request.POST.get('ch24')
			ans25=request.POST.get('ch25')
			ans26=request.POST.get('ch26')
			ans27=request.POST.get('ch27')
			ans28=request.POST.get('ch28')
			ans29=request.POST.get('ch29')
			ans30=request.POST.get('ch30')
			ans31=request.POST.get('ch31')
			ans32=request.POST.get('ch32')
			ans33=request.POST.get('ch33')
			ans34=request.POST.get('ch34')
			ans35=request.POST.get('ch35')
			ans36=request.POST.get('ch36')
			ans37=request.POST.get('ch37')
			ans38=request.POST.get('ch38')
			ans39=request.POST.get('ch39')
			ans40=request.POST.get('ch40')
			ans41=request.POST.get('ch41')
			ans42=request.POST.get('ch42')
			ans43=request.POST.get('ch43')
			ans44=request.POST.get('ch44')
			ans45=request.POST.get('ch45')
			ans46=request.POST.get('ch46')
			ans47=request.POST.get('ch47')
			ans48=request.POST.get('ch48')
			ans49=request.POST.get('ch49')
			ans50=request.POST.get('ch50')
			ans51=request.POST.get('ch51')
			ans52=request.POST.get('ch52')
			ans53=request.POST.get('ch53')
			ans54=request.POST.get('ch54')
			ans55=request.POST.get('ch55')
			ans56=request.POST.get('ch56')
			ans57=request.POST.get('ch57')
			ans58=request.POST.get('ch58')
			ans59=request.POST.get('ch59')
			ans60=request.POST.get('ch60')
			ans61=request.POST.get('ch61')
			ans62=request.POST.get('ch62')
			ans63=request.POST.get('ch63')
			ans64=request.POST.get('ch64')
			ans65=request.POST.get('ch65')
			ans66=request.POST.get('ch66')
			ans67=request.POST.get('ch67')
			ans68=request.POST.get('ch68')
			ans69=request.POST.get('ch69')
			ans70=request.POST.get('ch70')

			answer_set=TestAnswer.objects.create(a1=ans1, a2=ans2, a3=ans3, a4=ans4, a5=ans5, a6=ans6, a7=ans7, a8=ans8, a9=ans9, a10=ans10, a11=ans11, a12=ans12, a13=ans13, a14=ans14, a15=ans15, a16=ans16, a17=ans17, a18=ans18, a19=ans19, a20=ans20, a21=ans21, a22=ans22, a23=ans23, a24=ans24, a25=ans25, a26=ans26, a27=ans27, a28=ans28, a29=ans29, a30=ans30, a31=ans31, a32=ans32, a33=ans33, a34=ans34, a35=ans35, a36=ans36, a37=ans37, a38=ans38, a39=ans39, a40=ans40, a41=ans41, a42=ans42, a43=ans43, a44=ans44, a45=ans45, a46=ans46, a47=ans47, a48=ans48, a49=ans49, a50=ans50, a51=ans51, a52=ans52, a53=ans53, a54=ans54, a55=ans55, a56=ans56, a57=ans57, a58=ans58, a59=ans59, a60=ans60, a61=ans61, a62=ans62, a63=ans63, a64=ans64, a65=ans65, a66=ans66, a67=ans67, a68=ans68, a69=ans69, a70=ans70 )
			answer_set.save()

			energy=numberd(ans1,ans8,ans15,ans22,ans29,ans36,ans43,ans50,ans57,ans64)
			information=numberd(ans2,ans9,ans16,ans23,ans30,ans37,ans44,ans51,ans58,ans65,ans3,ans10,ans17,ans24,ans31,ans38,ans45,ans52,ans59,ans66)
			decision=numberd(ans4,ans11,ans18,ans25,ans32,ans39,ans46,ans53,ans60,ans67,ans5,ans12,ans19,ans26,ans33,ans40,ans47,ans54,ans61,ans68)
			living=numberd(ans6,ans13,ans20,ans27,ans34,ans41,ans48,ans55,ans62,ans69,ans7,ans14,ans21,ans28,ans35,ans42,ans49,ans56,ans63,ans70)

			if energy['pref']=='a':
				preference='E'
			else:
				preference='I'

			if information['pref']=='a':
				preference=preference+"S"
			else:
				preference=preference+"N"	

			if decision['pref']=='a':
				preference=preference+"T"
			else:
				preference=preference+"F"

			if living['pref']=='a':
				preference=preference+"J"
			else:
				preference=preference+"P"
			
			type_content_obj=TypeContent.objects.get(typ=preference)

			if request.user.is_authenticated():
				user_id=request.user		
			else:
				user_id=0

			result_obj=TestResult.objects.create(answer_id=answer_set,extraversion=energy['a_percent'],introversion=energy['b_percent'],intuition=information['b_percent'],sensing=information['a_percent'],feeling=decision['b_percent'],thinking=decision['a_percent'],percieving=living['b_percent'],judging=living['a_percent'],abbrev=preference,type_id=type_content_obj,user_id=user_id)		
			result_obj.save()
			context={"from":form,'EP':energy['a_percent'],'IP':energy['b_percent'],'SP':information['a_percent'],'NP':information['b_percent'],'TP':decision['a_percent'],'FP':decision['b_percent'],'JP':living['a_percent'],'PP':living['b_percent'],'content':type_content_obj}
			return  render(request,"result.html",context)
		else:
			context={'form':form}
			return render(request,self.template_name,context)
			
def result_view(request):
	return render(request,"result.html")

class SignUpView(View):
	template_name="signup.html"
	def get(self,request):
		return render(request,self.template_name)

def nsignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_f=form.save()
            user_f.is_staff=True
            user_f.is_normal=True
            user_f.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'normalsignup.html', {'form': form})


def psignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_f=form.save()
            user_f.is_staff=True
            user_f.is_premium=True
            user_f.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'premsignup.html', {'form': form})

def ssignup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_f=form.save()
            user_f.is_staff=True
            user_f.is_superpremium=True
            user_f.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'supersignup.html', {'form': form})  



@user_passes_test(lambda u: u.is_normal)
def NormalHome(request):
    context = {}
    return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_premium)
def PremiumHome(request):
    context = {}
    return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_superpremium)
def SuperHome(request):
    context = {}
    return render(request, 'superhome.html', context)

