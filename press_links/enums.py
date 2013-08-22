from django.utils.translation import ugettext_lazy as _

LIVE_STATUS = 1
DRAFT_STATUS = 2
HIDDEN_STATUS = 3
STATUS_CHOICES = (
    (LIVE_STATUS, _('Live')),
    (DRAFT_STATUS, _('Draft')),
    (HIDDEN_STATUS, _('Hidden')),
)
