import phonenumbers
#carrier:to know the name of service-provider of that phone-number'''
from phonenumbers import carrier
#geocoder:to know the specific location to that phone-number
from phonenumbers import geocoder
x=input("Enter Number:")
sp=phonenumbers.parse(x)
#for print country-name
print(geocoder.description_for_number(sp,'en'))
#for print name of the service-provider
print(carrier.name_for_number(sp,'en'))

    