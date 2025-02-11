from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        if hasattr(self, 'photo_path'):
            self.image(self.photo_path, 160, 10, 30)  # Photo at top-right
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Santosh Mahato Koiri - CV", ln=True, align="C")
        self.ln(10)
    
    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)
    
    def section_content(self, content):
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 8, content)
        self.ln(4)

pdf = PDF()
pdf.photo_path = "myphoto.jpg"  # Replace with the actual path
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Contact Information
pdf.section_title("Contact Information")
pdf.section_content("""
Email: kushwahaabhimanyu49@gmail.com
GitHub: github.com/LUV-KUSHWAHA
LinkedIn: linkedin.com/in/santosh-mahato-koiri
""")

# Education
pdf.section_title("Education")
pdf.section_content("""
Bachelor of Computer Engineering (3rd Year)
Advanced College of Engineering and Management, Kalanki, Kathmandu
January 2023 - Present

+2 (NEB Board)
Hetauda School of Management and Social Science Secondary School
August 2019 - June 2022 | GPA: 3.52

SEE (Government Board Exam)
Shree Nepal Rastriya Secondary School
May 2017 - April 2019 | GPA: 3.95
""")

# Skills
pdf.section_title("Technical Skills")
pdf.section_content("""
- Programming Languages: C++, Python, JavaScript
- Web Technologies: HTML, CSS, React.js, Node.js
- Databases: MySQL, Firebase
- Tools: Git, Linux, VS Code
""")

# Projects
pdf.section_title("Projects")
pdf.section_content("""
Library Management System (C++)
GitHub: github.com/LUV-KUSHWAHA/Library-Management-System

Scientific Calculator (C++)
GitHub: github.com/LUV-KUSHWAHA/059
""")

# Save the PDF
pdf.output("Santosh_Mahato_Koiri_CV.pdf")
print("CV generated successfully!")
