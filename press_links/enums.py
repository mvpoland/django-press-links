from django.utils.dates import MONTHS
from django.utils.translation import ugettext_lazy as _

LIVE_STATUS = 1
DRAFT_STATUS = 2
HIDDEN_STATUS = 3
STATUS_CHOICES = (
    (LIVE_STATUS, _('Live')),
    (DRAFT_STATUS, _('Draft')),
    (HIDDEN_STATUS, _('Hidden')),
)

# We're using the default translations from Django here by importing MONTHS and refer to it
MONTH_NAMES = ('', MONTHS[1], MONTHS[2], MONTHS[3], MONTHS[4], MONTHS[5], MONTHS[6], MONTHS[7], MONTHS[8], MONTHS[9],
               MONTHS[10], MONTHS[11], MONTHS[12])
