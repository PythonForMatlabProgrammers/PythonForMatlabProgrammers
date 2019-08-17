"""PDF Generator

PyPi: https://pypi.org/project/pdfkit/
options: https://wkhtmltopdf.org/usage/wkhtmltopdf.txt
"""


import pdfkit
import os.path

inp = os.path.join('_site', 'PythonForMatlabProgrammers.html')
out = os.path.join('PythonForMatlabProgrammers.pdf')
con = os.path.join('/', 'usr', 'local', 'bin', 'wkhtmltopdf')

config = pdfkit.configuration(wkhtmltopdf=con)

options = {
    'page-size': 'A4',
    'margin-top': '1.25in',
    'margin-right': '1.25in',
    'margin-bottom': '1.25in',
    'margin-left': '1.25in',
    'footer-center': '[page]',
    'footer-spacing': '10',         # units: mm.  The only units allowed here.
}

pdfkit.from_file(inp, out, configuration=config, options=options)
