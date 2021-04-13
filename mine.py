import phonenumbers
from test import number

from phonenumbers import geocoder

cl_number=phonenumbers.parse(number,"ch")
print(geocoder.description_for_number(cl_number,'en'))

from phonenumbers import carrier
service_num=phonenumbers.parse(number,'RO')
print(carrier.name_for_number(service_num,'en'))