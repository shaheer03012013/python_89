country_code = {
    "India": "+91",
    "United States": "+1",
    "United Kingdom": "+44",
}

print("India lookup:")
print(country_code.get("India", "Not Found"))

print("Japan lookup:")
print(country_code.get("Japan", "Not Found"))