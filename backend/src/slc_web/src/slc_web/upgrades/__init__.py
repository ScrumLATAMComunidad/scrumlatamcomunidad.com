from plone import api
from slc_web import logger


def upgrade_plone(context):
    """_Upgrade Plone to latest version._

    Args:
        context (object): _context object_
    """
    mt = api.portal.get_tool("portal_migration")
    if mt.needUpgrading():
        mt.upgrade()
        logger.info("Upgraded Plone")


def upgrade_pas_plugins_authomatic(portal_setup):
    """_Upgrade pas.plugins.authomatic to latest version._

    Args:
        portal_setup (object): _portal_setup object_
    """
    portal_setup.upgradeProfile("profile-pas.plugins.authomatic:default")
    logger.info("Upgraded pas.plugins.authomatic")
