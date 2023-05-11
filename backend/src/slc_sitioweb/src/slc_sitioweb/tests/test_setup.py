"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from Products.CMFPlone.utils import get_installer
from slc_sitioweb.testing import SLC_SITIOWEB_INTEGRATION_TESTING

import unittest


class TestSetup(unittest.TestCase):
    """Test that slc_sitioweb is properly installed."""

    layer = SLC_SITIOWEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.setup = self.portal.portal_setup
        self.installer = get_installer(self.portal, self.layer["request"])

    def test_product_installed(self):
        """Test if slc_sitioweb is installed."""
        self.assertTrue(self.installer.is_product_installed("slc_sitioweb"))

    def test_browserlayer(self):
        """Test that ISLC_SITIOWEBLayer is registered."""
        from plone.browserlayer import utils
        from slc_sitioweb.interfaces import ISLC_SITIOWEBLayer

        self.assertIn(ISLC_SITIOWEBLayer, utils.registered_layers())

    def test_latest_version(self):
        """Test latest version of default profile."""
        self.assertEqual(
            self.setup.getLastVersionForProfile("slc_sitioweb:default")[0],
            "20230511001",
        )


class TestUninstall(unittest.TestCase):

    layer = SLC_SITIOWEB_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = get_installer(self.portal, self.layer["request"])
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("slc_sitioweb")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if slc_sitioweb is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("slc_sitioweb"))

    def test_browserlayer_removed(self):
        """Test that ISLC_SITIOWEBLayer is removed."""
        from plone.browserlayer import utils
        from slc_sitioweb.interfaces import ISLC_SITIOWEBLayer

        self.assertNotIn(ISLC_SITIOWEBLayer, utils.registered_layers())
