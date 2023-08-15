"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISiteSchema
from Products.CMFPlone.utils import get_installer
from slc_web import PACKAGE_NAME
from slc_web.testing import SLC_WEB_INTEGRATION_TESTING
from zope.component import getUtility

import unittest


class TestSetup(unittest.TestCase):
    """Test that slc_web is properly installed.

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if slc_web is installed."""
        self.assertTrue(self.installer.is_product_installed(PACKAGE_NAME))

    def test_browserlayer(self):
        """Test that ISLC_WEBLayer is registered."""
        from plone.browserlayer import utils
        from slc_web.interfaces import ISLC_WEBLayer

        self.assertIn(ISLC_WEBLayer, utils.registered_layers())

    def test_sitemap_enabled(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISiteSchema, prefix="plone", check=False)
        self.assertTrue(settings.enable_sitemap)

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile(f"{PACKAGE_NAME}:default")[0],
            "20230511001",
        )


class TestUninstall(unittest.TestCase):
    """Test that slc_web is properly uninstalled.

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product(PACKAGE_NAME)
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if slc_web is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(PACKAGE_NAME))

    def test_browserlayer_removed(self):
        """Test that ISLC_WEBLayer is removed."""
        from plone.browserlayer import utils
        from slc_web.interfaces import ISLC_WEBLayer

        self.assertNotIn(ISLC_WEBLayer, utils.registered_layers())
