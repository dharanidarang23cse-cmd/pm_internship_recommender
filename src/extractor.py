import ollama
import json

def extract_from_jd(jd_text: str):
    prompt = f"""
    Extract the following details in JSON format:
    - skills_required
    - education
    - title
    - part_time (true/false)
    - work_mode (Onsite/Remote/Hybrid)
    - domain
    - summary
    - experience_level (Fresher/Graduate/Postgraduate)

    JD: {jd_text}
    """

    response = ollama.chat(
        model="llama2",   # ✅ using llama2
        messages=[{"role": "user", "content": prompt}]
    )

    try:
        structured = json.loads(response["message"]["content"])
    except Exception:
        structured = {"error": "Could not parse", "raw": response["message"]["content"]}

    return structured
