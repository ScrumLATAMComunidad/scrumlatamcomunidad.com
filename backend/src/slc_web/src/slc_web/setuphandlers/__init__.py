from plone import api
from Products.CMFPlacefulWorkflow.PlacefulWorkflowTool import (  # noqa
    WorkflowPolicyConfig_id,
)
from Products.CMFPlone.interfaces import INonInstallable
from slc_web import logger
from slc_web.setuphandlers import content
from slc_web.setuphandlers import users
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quick-installer."""
        return [
            "slc_web:uninstall",
        ]


def populate_portal(context):
    """Post install script"""
    portal = api.portal.get()
    # Delete content
    content.delete_content(portal)
    logger.info("Deleted default portal content")
    user = users.create_default_user()
    creators = [user.id]
    logger.info("Created default user")
    # Create other users
    users.create_team_accounts()
    logger.info("Created team accounts")
    # Create Initial content
    content.populate_portal(portal, creators)
    logger.info("Created initial content")
    # Update cover content
    content.update_home(portal, creators)


# def set_community_sponsor_workflow_policy(obj):
#     """Assume code that finds or creates the portal location
#     where the policy should apply the result of this code is
#     'folder'.
#     Change the workflow of the object using CMFPlacefulWorkflow.

#     Args:
#         portal (_type_): _description_
#     """
#     obj.manage_addProduct["CMFPlacefulWorkflow"].manage_addWorkflowPolicyConfig()
#     pc = getattr(obj, WorkflowPolicyConfig_id)
#     pc.setPolicyIn("community_sponsor_policy")
#     pc.setPolicyBelow("community_sponsor_policy")
#     logger.info("Workflow changed for element %s" % obj.getId())
