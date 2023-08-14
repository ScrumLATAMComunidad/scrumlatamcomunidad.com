"""This is an integration "unit" test for Site Structure."""
from slc_web.testing import SLC_WEB_INTEGRATION_TESTING

import unittest


class SiteStructureTest(unittest.TestCase):
    """The class that tests the Plone Site Structure was created.

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.existing = self.portal.objectIds()

    def test_default_content_is_removed(self):
        """This method test that the default content is removed."""
        existing = self.portal.objectIds()
        self.assertTrue("front-page" not in existing)
        self.assertTrue("events" not in existing)
        self.assertTrue("news" not in existing)
        self.assertTrue("Members" not in existing)
