from faker import Faker

class DataProvider():

    headers = [{
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer 2c68e1e0f2997f710b9980c5307757f47c8deda728b6e4b43d3187b671c526e0"
    }]

    base_url = "https://gorest.co.in/"
    fake = Faker()
    name = fake.name()
    email = fake.email()
    #user_id = "6854194"

    requestPayload = [{
        "email": email,
        "name": "AB",
        "gender": "male",
        "status": "active",
    }]

    updatedPayload = [{
        "name": name,
        "email": email,
        "gender": "male",
        "status": "active"
    }]
