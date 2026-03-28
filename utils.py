from fpdf import FPDF

def clean_text(text):
    return text.encode("latin-1", "ignore").decode("latin-1")

def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    text = clean_text(text)   # 👈 important fix

    for line in text.split("\n"):
        pdf.cell(200, 10, txt=line, ln=True)

    return pdf.output(dest="S").encode("latin-1")