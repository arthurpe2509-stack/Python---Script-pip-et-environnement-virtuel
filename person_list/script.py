from faker import Faker
from tabulate import tabulate

fake = Faker("fr_FR")

persons = [
    {
        "Nom": fake.name(),
        "Email": fake.email(),
        "Ville": fake.city(),
    }
    for _ in range(10)
]

print(tabulate(persons, headers="keys", tablefmt="rounded_outline"))
