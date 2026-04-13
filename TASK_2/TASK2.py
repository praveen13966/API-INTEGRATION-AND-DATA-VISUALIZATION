!pip install fpdf
import pandas as pd
from fpdf import FPDF
data_file = "/content/sample_data.csv"
df = pd.read_csv(data_file)
summary = {
    "Total Records": len(df),
    "Average Age": df['Age'].mean(),
    "Average Score": df['Score'].mean(),
    "Highest Score": df['Score'].max(),
    "Lowest Score": df['Score'].min()
}
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDFReport()
pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Data Analysis Summary", ln=True)
pdf.set_font("Arial", "", 11)
for key, value in summary.items():
    pdf.cell(0, 10, f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}", ln=True)
pdf.ln(10)
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Detailed Data", ln=True)
pdf.set_font("Arial", "", 10)
col_width = pdf.w / 4
row_height = pdf.font_size + 2
for col in df.columns:
    pdf.cell(col_width, row_height, col, border=1)
pdf.ln(row_height)
for i in range(len(df)):
    for col in df.columns:
        pdf.cell(col_width, row_height, str(df.iloc[i][col]), border=1)
    pdf.ln(row_height)
pdf.output("sample_report.pdf")
print("Report generated: sample_report.pdf")
