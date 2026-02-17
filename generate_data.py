import pandas as pd
import random
from faker import Faker

fake = Faker()

rows = 1_000_000

data = {
    "id": range(1, rows + 1),
    "name": [fake.name() for _ in range(rows)],
    "age": [random.randint(20, 60) for _ in range(rows)],
    "salary": [random.randint(30000, 150000) for _ in range(rows)],
    "department": [random.choice(["HR", "IT", "Finance", "Sales"]) for _ in range(rows)]
}

df = pd.DataFrame(data)
df.to_csv("data.csv", index=False)

print("CSV file with 1 million rows generated successfully!")
