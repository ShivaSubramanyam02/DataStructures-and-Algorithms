tvs = [
    {"comp_name": "Sony", "manf_year": 2024, "cost": 30000},
    {"comp_name": "Samsung", "manf_year": 2023, "cost": 45000},
    {"comp_name": "LG", "manf_year": 2022, "cost": 25000}
]


sorted_tvs = sorted(tvs, key=lambda x: x["cost"], reverse=True)

print(sorted_tvs)
