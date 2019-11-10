from constance.apps import ConstanceConfig as _ConstanceConfig
from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'blogger.apps.common'
    verbose_name = 'Blogger'


class ConstanceConfig(_ConstanceConfig):
    verbose_name = 'Settings'

    class Meta:
        app_label = 'common'
