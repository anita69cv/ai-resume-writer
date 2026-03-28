def generate_resume_prompt(
    name, phone, email, linkedin, github,
    college, education, is_student,
    skills, projects
):
    status = "Currently pursuing education" if is_student else "Education completed"

    return f"""
You are an expert resume writer.

Create a clean, professional, ATS-friendly resume.

STRICT RULES (VERY IMPORTANT):
- Do NOT change or reformat the phone number (keep exactly as given)
- Phone number must remain exactly 10 digits
- Do NOT modify email or URLs
- Do NOT add brackets or symbols to phone number
- Do NOT shorten or misspell links
- Keep formatting clean and readable

---------------------------------
HEADER
---------------------------------
{name}
{phone} | {email}
{linkedin} | {github}

---------------------------------
PROFESSIONAL SUMMARY
---------------------------------
Write a strong 2-3 line professional summary.

---------------------------------
SKILLS
---------------------------------
{skills}

---------------------------------
PROJECTS
---------------------------------
Convert the following into bullet points with strong action verbs:

{projects}

---------------------------------
EDUCATION
---------------------------------
College: {college}
Details: {education}
Status: {status}

---------------------------------

FINAL INSTRUCTIONS:
- Use proper spacing between sections
- Keep resume clean and structured
- Use bullet points for projects
- Use action verbs like Developed, Built, Designed, Implemented
- Keep the total length moderate (not too short, not too long)
"""