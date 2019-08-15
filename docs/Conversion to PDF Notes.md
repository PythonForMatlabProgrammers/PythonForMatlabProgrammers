## Notes for converting our .md files to HTML and then PDF

<br>

#### Aug 14, 2019
#### Mike P.

<br>

The _Python for MATLAB Programmers_ article was first written as an MS Word doc.
Early in 2019, however, we decided that we'd outgrown that format and wanted
something web-based.  Andrew recommended that we move to MarkDown on GitHub.
It's been a good choice.

The original conversion of Word to MarkDown was handled by Andrew.  Over the
course of months, Mike then cleaned up the MarkDown (the conversion was not
perfect) and began exploring ways to convert to HTML and/or PDF.

Pandoc was the obvious choice for the latter two conversions.  Mike attempted
but failed to get this to work well.  There were a few issues.  First, our .md
files employ a lot of unordered lists, with code blocks mixed in.  Pandoc
struggled to get our indentation working correctly.  I found that I could alter
the MarkDown, adding enough indentation to get the export correct, but that made
something of a mess of our .md files.

Second, Pandoc dropped the format of our hyperlinks; the links themselves
remained in the exported files, but the formatting was dropped.  I did not find
a way to resolve that (but there are a thousand Pandoc options to sort through).
And lastly, Pandoc was ignoring css that I had in the files.  Like the
hyperlinks there's probably an option to alter that behavior, but I did not find
it.

With some trial and error, I found the following process to create HTML and PDF
output.  It's fast, and it retains _all_ of our formatting.  

1. Using GitHub desktop, sync up a local repository with the online repository.

1. Open Windows Powershell, cd to the repository and enter the following command
to concatenate the various article chapters into one file:

    Get-Content 0*.md | Set-Content ".\Python for MATLAB Programmers.md"

1. Open the new file in the Atom editor.

1. For best results, switch the Atom theme to a light-colored one, such as _Atom
Light_.  This probably is a bug work-around, but with the dark themes, code
blocks will print with light text on a light background.  

1. Also, make the preview pane wide; if it is too narrow, you'll run the chance
of having horizontal scroll bars in the output.

1. Right-click on the preview and select 'Export HTML.'

1. The HTML file is done; no editing required.  If you want a PDF, the best
converter I found was a Python package called <a
href="https://pypi.org/project/pdfkit/">pdfkit</a>.  Here's my code snipped to
export the HTML file to PDF:
```python
import pdfkit
import os.path
inp = os.path.join('C:\\', 'Users', 'Owner', 'Downloads', 'a.html')
out = os.path.join('C:\\', 'Users', 'Owner', 'Downloads', 'a.pdf')
con = os.path.join('C:\\', 'Program Files', 'wkhtmltopdf', 'bin', 'wkhtmltopdf.exe')
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
```

1. To use the above, you'll need to install a package called _wkhtmltopdf_. Get
it <a rhref="https://wkhtmltopdf.org">here</a>

1. That's all there is to do.  Our .md files make no special allowances for the
above to work. There's no editing required of the .HTML file, and the PDF file
faithfully reproduces the input.
