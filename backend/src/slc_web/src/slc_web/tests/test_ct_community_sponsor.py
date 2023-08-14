"""Community Sponsor Content Type tests for this package."""
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from slc_web import ADD_SPONSOR_ROLES
from slc_web import MANAGE_SPONSOR_ROLES
from slc_web.testing import SLC_WEB_INTEGRATION_TESTING
from zope.component import queryUtility

import unittest


class CommunitySponsorContentTypeTest(unittest.TestCase):
    """The Community Sponsor Content Type Test class

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])

    def test_ct_community_sponsor_fti(self):
        """Test If CommunitySponsor exits on Dexterity FTI."""
        fti = queryUtility(IDexterityFTI, name="CommunitySponsor")
        self.assertTrue(fti)
        # self.assertNotEqual(None, fti)

    def test_ct_community_sponsor_globally_addable(self):
        """Test If CommunitySponsor is globally addable."""

        setRoles(self.portal, TEST_USER_ID, ["Contributor"])
        fti = queryUtility(IDexterityFTI, name="CommunitySponsor")
        self.assertTrue(
            fti.global_allow,
            "{0} is not globally addable!".format(fti.id),
        )

    def test_ct_community_sponsor_roles(self):
        """Test correct assigning of permissions from rolemap.xml file."""

        # Test permission mapping for adding an Community Sponsor
        sponsor_roles = [
            r["name"]
            for r in self.portal.rolesOfPermission(
                "Community Sponsor: Add Community Sponsor"
            )
            if r["selected"]
        ]
        self.assertEqual(sponsor_roles, ADD_SPONSOR_ROLES)

        # Test permission mapping for View Detail
        sponsor_roles = [
            r["name"]
            for r in self.portal.rolesOfPermission("Community Sponsor: View Detail")
            if r["selected"]
        ]
        self.assertEqual(sponsor_roles, MANAGE_SPONSOR_ROLES)

        # Test permission mapping for managing Manage Sponsors
        sponsor_roles = [
            r["name"]
            for r in self.portal.rolesOfPermission("Community Sponsor: Manage Sponsors")
            if r["selected"]
        ]
        self.assertEqual(sponsor_roles, MANAGE_SPONSOR_ROLES)
