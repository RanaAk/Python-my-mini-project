
data = {
    (5, "Sarah", "Williams"): {"a": "programming", "b": "development", "c": 80000},
    (6, "Michael", "Brown"): {"e": 25, "f": "coding", "g": 95000},
    (7, "Emily", "Davis"): {"h": 30, "i": "project", "j": "programming"},
    (8, "Daniel", "Wilson"): {"k": 35, "l": "testing", "m": 120000}
}

# Accessing the values using the keys
print(data[(5, "Sarah", "Williams")]["a"])
print(data[(6, "Michael", "Brown")]["f"])
print(data[(7, "Emily", "Davis")]["j"])

data[(5, "Sarah", "Williams")]["a"] = {"b": "testing", "c": 80000}
data[(7, "Emily", "Davis")]["j"] = {"h": 30, "i": "project"}
print(data[(5, "Sarah", "Williams")]["a"])
print(data[(7, "Emily", "Davis")]["j"])
