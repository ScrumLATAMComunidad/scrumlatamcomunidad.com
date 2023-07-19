from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing.zope import WSGI_SERVER_FIXTURE

import slc_web


class SLC_WEBLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=slc_web)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "slc_web:default")
        applyProfile(portal, "slc_web:initial")


SLC_WEB_FIXTURE = SLC_WEBLayer()


SLC_WEB_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SLC_WEB_FIXTURE,),
    name="SLC_WEBLayer:IntegrationTesting",
)


SLC_WEB_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SLC_WEB_FIXTURE, WSGI_SERVER_FIXTURE),
    name="SLC_WEBLayer:FunctionalTesting",
)


SLC_WEBACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SLC_WEB_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        WSGI_SERVER_FIXTURE,
    ),
    name="SLC_WEBLayer:AcceptanceTesting",
)
