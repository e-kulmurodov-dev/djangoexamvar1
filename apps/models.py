from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    email_confirmed = models.BooleanField(default=False)
    activation_link_used = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


'''
django i18n

LANGUAGES(
    ()
    ()

)

LOCALE_PATHS = [BASE_DIR / 'locale']

verbose_name = _('products')
gettext_lazy as _
i18n_patterns (urls.py)
'''
