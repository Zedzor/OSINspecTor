from django.test import TestCase
from app.functionalities.common import geo
from app.functionalities.common import vuln
from app.functionalities.domain import dns
from app.functionalities.ip import reverse
# Create your tests here.
#vistas

#class ViewsTestCase(TestCase):
#    def test_index_loads_properly(self):
#        """The index page loads properly"""
#        response = self.client.get('127.0.0.1:8000')
#        self.assertEqual(response.status_code, 200)

#funciones
class GeoDomainTestCase(TestCase):
    def test_geo(self):
        info = geo.get_geo("udc.es")
        self.assertEqual(str(info), "{'results': {'latitude': 43.37126159667969, 'longitude': -8.389616012573242, 'city': 'A Coruña', 'region': 'Galicia', 'country': 'Spain', 'flag': '🇪🇸'}, 'status': 200}")

class GeoIPTestCase(TestCase):
    def test_geo(self):
        info = geo.get_geo("193.144.53.84")
        self.assertEqual(str(info), "{'results': {'latitude': 43.371490478515625, 'longitude': -8.395970344543457, 'city': 'A Coruña', 'region': 'Galicia', 'country': 'Spain', 'flag': '🇪🇸'}, 'status': 200}")

#class  VulIPTestCase(TestCase):
#    def test_vuln(self):
#        info = vuln.get_vulns("udc.es")
#        self.assertEqual(str(info), '')

class DnsDomainCase(TestCase):
    def test_dns(self):
        info = dns.get_dns("udc.es")
        self.assertEquals(str(info),"{'results': ['ineco.nic.es', 'nso.nic.es', 'chico.rediris.es', 'sun.rediris.es', 'zape.udc.es', 'zipi.udc.es'], 'status': 200}")

class RevIPCase(TestCase):
    def test_rev(self):
        info = reverse.get_reverse("193.144.53.84")
        self.assertEqual(str(info), "{'results': ['193.144.53.84', 'novas.udc.es', 'novas.udc.gal', 'udc.es', 'udc.gal', 'www.udc.es', 'www.udc.gal'], 'status': 200}")
