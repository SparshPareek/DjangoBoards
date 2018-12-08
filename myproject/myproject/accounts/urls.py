from django.conf.urls import url
from django.urls import reverse_lazy
from . import views
from django.contrib.auth import views as auth_view

app_name = 'accounts'
urlpatterns = [
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^accounts/logout/$', auth_view.LogoutView.as_view(), name='logout'),
    url(r'^accounts/login/$', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^reset/$', auth_view.PasswordResetView.as_view(template_name='password_reset.html',
                                                         email_template_name='password_reset_email.html',
                                                         subject_template_name='password_reset_subject.txt',
                                                         success_url=reverse_lazy('accounts:password_reset_done')),
        name='password_reset'),
    url(r'^reset/done/$', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',
                                                   success_url=reverse_lazy('accounts:password_reset_complete')),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_view.PasswordChangeView.as_view(template_name='password_change.html',
        success_url=reverse_lazy('accounts:password_change_done')),
        name='password_change'),
    url(r'^settings/password/done/$', auth_view.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'), name='password_change_done'),

    url(r'^settings/account/$', views.UserUpdateView.as_view(), name='my_account'),
]

