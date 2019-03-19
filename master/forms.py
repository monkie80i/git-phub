from django import forms
from master.choices import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from master.models import MyUser


class TestForm(forms.Form):
	def __init__(self,*args,**kwargs):
		super(TestForm,self).__init__(*args,**kwargs)

	ch1=forms.ChoiceField(label='1. At a party do you:',choices=CH1,widget=forms.RadioSelect())
	ch2=forms.ChoiceField(label='2. Are you more:',choices=CH2,widget=forms.RadioSelect())
	ch3=forms.ChoiceField(label='3. Is it worse to:',choices=CH3,widget=forms.RadioSelect())
	ch4=forms.ChoiceField(label='4. Are you more impressed by:',choices=CH4,widget=forms.RadioSelect())
	ch5=forms.ChoiceField(label='5.Are more drawn toward the:',choices=CH5,widget=forms.RadioSelect())
	ch6=forms.ChoiceField(label='6.Do you prefer to work:',choices=CH6,widget=forms.RadioSelect())
	ch7=forms.ChoiceField(label='7.Do you tend to choose:',choices=CH7,widget=forms.RadioSelect())
	ch8=forms.ChoiceField(label='8.At parties do you:',choices=CH8,widget=forms.RadioSelect())
	ch9=forms.ChoiceField(label='9.Are you more attracted to:',choices=CH9,widget=forms.RadioSelect())
	ch10=forms.ChoiceField(label='10.Are you more interested in:',choices=CH10,widget=forms.RadioSelect())
	ch11=forms.ChoiceField(label='11.In judging others are you more swayed by:',choices=CH11,widget=forms.RadioSelect())
	ch12=forms.ChoiceField(label='12.In approaching others is your inclination to be somewhat:',choices=CH12,widget=forms.RadioSelect())
	ch13=forms.ChoiceField(label='13. Are you more:',choices=CH13,widget=forms.RadioSelect())
	ch14=forms.ChoiceField(label='14. Does it bother you more having things:',choices=CH14,widget=forms.RadioSelect())
	ch15=forms.ChoiceField(label='15. In your social groups do you:',choices=CH15,widget=forms.RadioSelect())
	ch16=forms.ChoiceField(label='16. In doing ordinary things are you more likely to:',choices=CH16,widget=forms.RadioSelect())
	ch17=forms.ChoiceField(label='17. Writers should:',choices=CH17,widget=forms.RadioSelect())
	ch18=forms.ChoiceField(label='18. Which appeals to you more:',choices=CH18,widget=forms.RadioSelect())
	ch19=forms.ChoiceField(label='19. Are you more comfortable in making:',choices=CH19,widget=forms.RadioSelect())
	ch20=forms.ChoiceField(label='20. Do you want things:',choices=CH20,widget=forms.RadioSelect())
	ch21=forms.ChoiceField(label='21. Would you say you are more:',choices=CH21,widget=forms.RadioSelect())
	ch22=forms.ChoiceField(label='22. In phoning do you:',choices=CH22,widget=forms.RadioSelect())
	ch23=forms.ChoiceField(label='23. Facts:',choices=CH23,widget=forms.RadioSelect())
	ch24=forms.ChoiceField(label='24. Are visionaries:',choices=CH24,widget=forms.RadioSelect())
	ch25=forms.ChoiceField(label='25. Are you more often:',choices=CH25,widget=forms.RadioSelect())
	ch26=forms.ChoiceField(label='26. Is it worse to be:',choices=CH26,widget=forms.RadioSelect())
	ch27=forms.ChoiceField(label='27. Should one usually let events occur:',choices=CH27,widget=forms.RadioSelect())
	ch28=forms.ChoiceField(label='28. Do you feel better about:',choices=CH28,widget=forms.RadioSelect())
	ch29=forms.ChoiceField(label='29. In company do you:',choices=CH29,widget=forms.RadioSelect())
	ch30=forms.ChoiceField(label='30. Common sense is:',choices=CH30,widget=forms.RadioSelect())
	ch31=forms.ChoiceField(label='31. Children often do not:',choices=CH31,widget=forms.RadioSelect())
	ch32=forms.ChoiceField(label='32. In making decisions do you feel more comfortable with:',choices=CH32,widget=forms.RadioSelect())
	ch33=forms.ChoiceField(label='33. Are you more:',choices=CH33,widget=forms.RadioSelect())
	ch34=forms.ChoiceField(label='34. Which is more admirable:',choices=CH34,widget=forms.RadioSelect())
	ch35=forms.ChoiceField(label='35. Do you put more value on:',choices=CH35,widget=forms.RadioSelect())
	ch36=forms.ChoiceField(label='36. Does new and non-routine interaction with others:',choices=CH36,widget=forms.RadioSelect())
	ch37=forms.ChoiceField(label='37. Are you more frequently:',choices=CH37,widget=forms.RadioSelect())
	ch38=forms.ChoiceField(label='38. Are you more likely to:',choices=CH38,widget=forms.RadioSelect())
	ch39=forms.ChoiceField(label='39. Which is more satisfying:',choices=CH39,widget=forms.RadioSelect())
	ch40=forms.ChoiceField(label='40. Which rules you more:',choices=CH40,widget=forms.RadioSelect())
	ch41=forms.ChoiceField(label='41. Are you more comfortable with work that is:',choices=CH41,widget=forms.RadioSelect())
	ch42=forms.ChoiceField(label='42. What do you tend to look for:',choices=CH42,widget=forms.RadioSelect())
	ch43=forms.ChoiceField(label='43. Do you prefer:',choices=CH43,widget=forms.RadioSelect())
	ch44=forms.ChoiceField(label='44. Do you go more by:',choices=CH44,widget=forms.RadioSelect())
	ch45=forms.ChoiceField(label='45. Are you more interested in:',choices=CH45,widget=forms.RadioSelect())
	ch46=forms.ChoiceField(label='46. Which is more of a compliment:',choices=CH46,widget=forms.RadioSelect())
	ch47=forms.ChoiceField(label='47. Do you value in yourself more that you are:',choices=CH47,widget=forms.RadioSelect())
	ch48=forms.ChoiceField(label='48. Do you more often prefer the',choices=CH48,widget=forms.RadioSelect())
	ch49=forms.ChoiceField(label='49. Are you more comfortable:',choices=CH49,widget=forms.RadioSelect())
	ch50=forms.ChoiceField(label='50. Do you:',choices=CH50,widget=forms.RadioSelect())
	ch51=forms.ChoiceField(label='51. Are you more likely to trust your:',choices=CH51,widget=forms.RadioSelect())
	ch52=forms.ChoiceField(label='52. Do you feel:',choices=CH52,widget=forms.RadioSelect())
	ch53=forms.ChoiceField(label='53. person is more to be complimented - one of:',choices=CH53,widget=forms.RadioSelect())
	ch54=forms.ChoiceField(label='54. Are you inclined more to be:',choices=CH54,widget=forms.RadioSelect())
	ch55=forms.ChoiceField(label='55. Is it preferable mostly to:',choices=CH55,widget=forms.RadioSelect())
	ch56=forms.ChoiceField(label='56. In relationships should most things be:',choices=CH56,widget=forms.RadioSelect())
	ch57=forms.ChoiceField(label='57. When the phone rings do you:',choices=CH57,widget=forms.RadioSelect())
	ch58=forms.ChoiceField(label='58. Do you prize more in yourself:',choices=CH58,widget=forms.RadioSelect())
	ch59=forms.ChoiceField(label='59. Are you drawn more to:',choices=CH59,widget=forms.RadioSelect())
	ch60=forms.ChoiceField(label='60. Which seems the greater error:',choices=CH60,widget=forms.RadioSelect())
	ch61=forms.ChoiceField(label='61. Do you see yourself as basically:',choices=CH61,widget=forms.RadioSelect())
	ch62=forms.ChoiceField(label='62. Which situation appeals to you more:',choices=CH62,widget=forms.RadioSelect())
	ch63=forms.ChoiceField(label='63. Are you a person that is more:',choices=CH63,widget=forms.RadioSelect())
	ch64=forms.ChoiceField(label='64. Are you more inclined to be:',choices=CH64,widget=forms.RadioSelect())
	ch65=forms.ChoiceField(label='65. In writings do you prefer:',choices=CH65,widget=forms.RadioSelect())
	ch66=forms.ChoiceField(label='66. Is it harder for you to:',choices=CH66,widget=forms.RadioSelect())
	ch67=forms.ChoiceField(label='67. Which do you wish more for yourself:',choices=CH67,widget=forms.RadioSelect())
	ch68=forms.ChoiceField(label='68. Which is the greater fault:',choices=CH68,widget=forms.RadioSelect())
	ch69=forms.ChoiceField(label='69. Do you prefer the:',choices=CH69,widget=forms.RadioSelect())
	ch70=forms.ChoiceField(label='70. Do you tend to be more:',choices=CH70,widget=forms.RadioSelect())

	#lat=forms.DecimalField(widget=HiddenInput())
	#lon=forms.DecimalField(widget=HiddenInput())

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )