import logging

from source.utils.folder import create_folders
from .base import *

logger = logging.getLogger('source')
logger.error("Current mode: %s" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *

create_folders([STATIC_ROOT, MEDIA_ROOT] + [i for i in STATICFILES_DIRS])