from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

df = pd.read_csv("topics.csv", sep=',')

for index, row in df.iterrows():
    pdf.add_page()

    #Set Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)

    pdf.line(10,21, 200, 21)

    #Set Footer
    pdf.ln(265)

    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")


    for i in range(row["Pages"]):
        pdf.add_page()

        # Set Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

pdf.output('output.pdf')