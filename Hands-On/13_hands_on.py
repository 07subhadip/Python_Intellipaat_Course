nested_dict = {
    "Python": {
        "type": "Programming Language",
        "level": "Intermediate"
    },
    "Java": {
        "type": "Programming Language",
        "level": "Advanced"
    },
    "HTML": {
        "type": "Markup Language",
        "level": "Beginner"
    }
}

key_value = list(nested_dict.items())
print(key_value)

print("\n**********************************\n")

key_only = list(nested_dict.keys())
print(key_only)

print("\n**********************************\n")

first_key = list(nested_dict.keys())[0]
nested_dict.pop(first_key)
print(nested_dict)

print("\n**********************************\n")

last_key = list(nested_dict.keys())[-1]
nested_dict.pop(last_key)
print(nested_dict)

print("\n**********************************\n")

last_rem_key = list(nested_dict.keys())[-1]
nested_dict[last_rem_key] = {
    "name":"Subhadip",
    "age":24
}
print(nested_dict)