r"""

--.--                         |
  |  ,---..   .,-.-.,---.,---.|---
  |  |    |   || | ||   ||---'|
  `  `    `---'` ' '|---'`---'`---'
                    |

"""

__title__ = 'Django Trumpet'
__version__ = '0.1.0'
__author__ = 'VentureGeek'
__license__ = 'MIT License'
__copyright__ = 'Copyright 2019 VentureGeek LLC'

# Version synonym
VERSION = __version__


def connect_signal():
    from django.db.models.signals import post_save
    from trumpet.signals import update_bucket_version

    post_save.connect(update_bucket_version)