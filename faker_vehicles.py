from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)


print(fake.year())
print (fake.vehicle_year_make_model_cat())
