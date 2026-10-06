import re

SKILL_LIST = [
    "python", "java", "sql", "html", "css", "javascript", "git",
    "machine learning", "nlp", "excel", "powerpoint", "aws", "azure"
]

JOB_ROLES = {
    "Python Developer": ["python", "sql", "git"],
    "Java Developer": ["java", "sql", "git"],
    "Web Developer": ["html", "css", "javascript"],
    "Data/AI Intern": ["python", "machine learning", "sql", "nlp"]
}


def normalize(text):
    return re.sub(r"[^a-z0-9+#. ]", " ", text.lower())


def extract_skills(text):
    text = normalize(text)
    return [skill for skill in SKILL_LIST if skill in text]


def match_jobs(skills):
    results = []
    skill_set = set(skills)
    for role, required in JOB_ROLES.items():
        matched = [skill for skill in required if skill in skill_set]
        score = round((len(matched) / len(required)) * 100)
        results.append((role, score, matched, required))
    return sorted(results, key=lambda item: item[1], reverse=True)


def main():
    print("=" * 60)
    print("AI RESUME SCREENING & JOB MATCHING SYSTEM")
    print("=" * 60)
    print("Paste your resume text below. Type END on a new line when finished.\n")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)

    resume_text = " ".join(lines)
    skills = extract_skills(resume_text)

    print("\nDetected Skills:")
    if skills:
        for skill in skills:
            print(f"  - {skill}")
    else:
        print("  No supported skills detected.")

    print("\nJob Matching Results:")
    for role, score, matched, required in match_jobs(skills):
        print(f"\n{role}: {score}%")
        print(f"Matched skills : {', '.join(matched) if matched else 'None'}")
        print(f"Required skills: {', '.join(required)}")

    print("\nNote: This is a rule-based prototype for demonstration, not a real hiring decision system.")


if __name__ == "__main__":
    main()