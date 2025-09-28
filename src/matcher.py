def calculate_score(user, internship):
    score = 0
    reasons = {}

    # Skills Match (50%)
    user_skills = set(s.lower() for s in user["skills"])
    jd_skills = set(s.lower() for s in internship.get("skills_required", []))
    matched = user_skills & jd_skills
    skill_score = (len(matched) / len(jd_skills)) * 50 if jd_skills else 0
    score += skill_score
    reasons["skills"] = f"Matched {list(matched)}"

    # Education Match (15%)
    if any(user["education"].lower() in e.lower() for e in internship.get("education", [])):
        score += 15
        reasons["education"] = "Education requirement satisfied"
    else:
        reasons["education"] = "Education mismatch"

    # Domain/Interest Match (15%)
    if any(i.lower() in internship.get("domain", "").lower() for i in user["interests"]):
        score += 15
        reasons["domain"] = "Domain aligned"
    else:
        reasons["domain"] = "Domain mismatch"

    # Work Mode Match (10%)
    if user["preferred_mode"].lower() == internship.get("work_mode", "").lower():
        score += 10
        reasons["work_mode"] = "Work mode matches"
    else:
        reasons["work_mode"] = f"Preferred {user['preferred_mode']} vs {internship.get('work_mode')}"

    # Experience Level Match (10%)
    if user["experience_level"].lower() in internship.get("experience_level", "").lower():
        score += 10
        reasons["experience"] = "Experience level matches"
    else:
        reasons["experience"] = "Experience mismatch"

    return score, reasons


def generate_recommendations(users, internships):
    results = {}
    for user in users:
        scored = []
        for jd in internships:
            score, reasons = calculate_score(user, jd)
            scored.append({
                "company": jd.get("company", "Unknown"),
                "title": jd.get("title", "Unknown"),
                "match_score": round(score, 2),
                "reasons": reasons
            })
        top5 = sorted(scored, key=lambda x: x["match_score"], reverse=True)[:5]
        results[user["name"]] = top5
    return results
