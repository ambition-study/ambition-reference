from django.test import TestCase, tag

from edc_reference.site import site_reference_configs
from pprint import pprint


class TestReference(TestCase):

    def test_(self):
        site_reference_configs.validate()
        pprint(site_reference_configs.registry)
