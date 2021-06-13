from django.test import TestCase
from app.functionalities.common import geo
from app.functionalities.common import vuln
# Create your tests here.
#vistas

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

#funciones
class GeoDomainTestCase(TestCase):
    def test_geo(self):
        info = geo.get_geo("udc.es")
        self.assertEqual(str(info), '{"ip":"2001:720:121c:e000::203","type":"ipv6","continent_code":"EU","continent_name":"Europe","country_code":"ES","country_name":"Spain","region_code":"GA","region_name":"Galicia","city":"A Coru\u00f1a","zip":null,"latitude":43.37126159667969,"longitude":-8.389616012573242,"location":{"geoname_id":3119841,"capital":"Madrid","languages":[{"code":"es","name":"Spanish","native":"Espa\u00f1ol"},{"code":"eu","name":"Basque","native":"Euskara"},{"code":"ca","name":"Catalan","native":"Catal\u00e0"},{"code":"gl","name":"Galician","native":"Galego"},{"code":"oc","name":"Occitan","native":"Occitan"}],"country_flag":"http:\/\/assets.ipstack.com\/flags\/es.svg","country_flag_emoji":"\ud83c\uddea\ud83c\uddf8","country_flag_emoji_unicode":"U+1F1EA U+1F1F8","calling_code":"34","is_eu":true}}')

class GeoIPTestCase(TestCase):
    def test_geo(self):
        info = geo.get_geo("193.144.53.84")
        #cambiar
        self.assertEqual(str(info), '{"ip":"2001:720:121c:e000::203","type":"ipv6","continent_code":"EU","continent_name":"Europe","country_code":"ES","country_name":"Spain","region_code":"GA","region_name":"Galicia","city":"A Coru\u00f1a","zip":null,"latitude":43.37126159667969,"longitude":-8.389616012573242,"location":{"geoname_id":3119841,"capital":"Madrid","languages":[{"code":"es","name":"Spanish","native":"Espa\u00f1ol"},{"code":"eu","name":"Basque","native":"Euskara"},{"code":"ca","name":"Catalan","native":"Catal\u00e0"},{"code":"gl","name":"Galician","native":"Galego"},{"code":"oc","name":"Occitan","native":"Occitan"}],"country_flag":"http:\/\/assets.ipstack.com\/flags\/es.svg","country_flag_emoji":"\ud83c\uddea\ud83c\uddf8","country_flag_emoji_unicode":"U+1F1EA U+1F1F8","calling_code":"34","is_eu":true}}')

class  VulIPTestCase(TestCase):
    def test_vuln(self):
        info = vuln.get_vulns("udc.es")
        self.assertEqual(str(info), '')

