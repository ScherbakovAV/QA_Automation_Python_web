"""https://dss.cryptopro.ru/verify/service.svc?wsdl"""

from zeep import Client

wsdl = 'https://dss.cryptopro.ru/verify/service.svc?wsdl'
sign = 'Нужна верная подпись'
client = Client(wsdl=wsdl)


def test_step1():
    assert client.service.VerifySignature('CMS', sign)['Result'], 'SOAP test FAILED'
