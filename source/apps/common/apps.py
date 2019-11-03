from django.apps import AppConfig
from constance.apps import ConstanceConfig as _ConstanceConfig


class CommonConfig(AppConfig):
    name = 'source.apps.common'


class ConstanceConfig(_ConstanceConfig):
    verbose_name = 'Settings'

    class Meta:
        app_label = 'common'
