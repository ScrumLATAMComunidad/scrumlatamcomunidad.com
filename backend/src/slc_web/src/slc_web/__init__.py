"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "slc_web"

# Permissions Roles
ADD_SPONSOR_ROLES = ["Manager", "Site Administrator", "Sponsorship Committee"]
MANAGE_SPONSOR_ROLES = ["Manager", "Sponsorship Committee"]

_ = MessageFactory("slc_web")

logger = logging.getLogger("slc_web")
