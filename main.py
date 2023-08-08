from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="portrait", unit="mm", format="A4")

df = pd.read_csv("topics.csv", sep=',')
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There!", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi There!", align="L", ln=1, border=1)

pdf.output('output.pdf')