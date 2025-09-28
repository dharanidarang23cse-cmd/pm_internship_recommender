import json
from src.matcher import generate_recommendations

# Step 1: Load structured internships
with open("data/internship_dataset_25.json", "r", encoding="utf-8") as f:
    internships = json.load(f)

# Step 2: Load user profiles
with open("data/user_profiles_25.json", "r", encoding="utf-8") as f:
    users = json.load(f)

# Pick ONE user (example: first user in list)
user = users[0]   # 🔹 Change index or filter by name/id

# Step 3: Generate recommendations for just this user
results = generate_recommendations([user], internships)

# Step 4: Save output
with open("data/recommendations.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"✅ Top 5 recommendations saved for user: {user['name']} in data/recommendations.json")
