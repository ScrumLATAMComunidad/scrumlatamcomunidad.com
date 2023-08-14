"""Community Member Content Type tests for this package."""
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from slc_web.testing import SLC_WEB_INTEGRATION_TESTING
from zope.component import queryUtility

import unittest


class CommunityMemberContentTypeTest(unittest.TestCase):
    """The Community Member Content Type Test class

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_fti_community_member(self):
        fti = queryUtility(IDexterityFTI, name="CommunityMember")
        self.assertTrue(fti)
        # self.assertNotEqual(None, fti)
