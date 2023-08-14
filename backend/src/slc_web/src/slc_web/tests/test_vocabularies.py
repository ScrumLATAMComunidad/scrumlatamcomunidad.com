"""Vocabularies tests for this package."""
from slc_web import PACKAGE_NAME
from slc_web.testing import SLC_WEB_INTEGRATION_TESTING
from slc_web.vocabularies import industries_vocabulary
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest


class IndustriesVocabularyTest(unittest.TestCase):
    """Test fot the slc_web Vocabularies.

    Args:
        unittest (class): unittest TestCase
    """

    layer = SLC_WEB_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]

    def test_vocabulary(self):
        """Check that the vocabulary exists."""
        self.assertTrue(industries_vocabulary)

    def test_vocabulary_industries_total(self):
        """Checkout the industries vocabulary total size."""
        factory = getUtility(
            IVocabularyFactory, f"{PACKAGE_NAME}.vocabulary.industries"
        )
        vocabulary = factory(self.portal)
        self.assertEqual(len(vocabulary), 8)

    def test_vocabulary_industry_exits(self):
        """Check that 'NGO' item is in the vocabulary."""
        factory = getUtility(
            IVocabularyFactory, f"{PACKAGE_NAME}.vocabulary.industries"
        )
        vocabulary = factory(self.portal)
        industries = [industry.title for industry in vocabulary]
        self.assertIn("NGO", industries)
