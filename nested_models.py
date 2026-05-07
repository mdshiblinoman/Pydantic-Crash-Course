from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'Khylna', 'state': 'Dacope', 'pin': '5075'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Noman', 'gender': 'male', 'age': 23, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump(include={'address'})

print(type(temp))
print(temp)