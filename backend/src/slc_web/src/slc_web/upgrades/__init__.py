from plone import api
from slc_web import logger


def upgrade_plone(context):
    """Upgrade Plone to latest version.

    Args:
        context (object): context object
    """
    mt = api.portal.get_tool("portal_migration")
    if mt.needUpgrading():
        mt.upgrade()
        logger.info("Upgraded Plone")


def upgrade_pas_plugins_authomatic(portal_setup):
    """Upgrade pas.plugins.authomatic to latest version.

    Args:
        portal_setup (object): portal_setup object
    """
    portal_setup.upgradeProfile("profile-pas.plugins.authomatic:default")
    logger.info("Upgraded pas.plugins.authomatic")
