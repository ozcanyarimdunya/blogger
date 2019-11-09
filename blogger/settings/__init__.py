import logging

from blogger.core.utils import FolderUtils
from .base import *

logger = logging.getLogger('blogger')
logger.error("Current mode: %s" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .prod import *
else:
    from .dev import *

FolderUtils.create_folders([STATIC_ROOT, MEDIA_ROOT] + [i for i in STATICFILES_DIRS])
