from django.conf.urls import url
from django.contrib import admin
from master import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'phub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/',views.HomeView.as_view(),name="home"),
    url(r'^mbti/',views.MbtiView.as_view(),name="mbti"),
    url(r'^16personalities/',views.PersonalitiesView.as_view(),name="16personalities"),
    url(r'^test/',views.TestView.as_view(),name="test"),
    url(r'^resources/',views.ResourcesView.as_view(),name="resources"),
    url(r'^about/',views.AboutView.as_view(),name="about"),
    url(r'^result/',views.result_view,name="result"),
    url(r'^signup/',views.SignUpView.as_view(),name="signup"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^nsignup/',views.nsignup,name="nsignup"),
    url(r'^psignup/',views.psignup,name="psignup"),
    url(r'^ssignup/',views.ssignup,name="ssignup"),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

