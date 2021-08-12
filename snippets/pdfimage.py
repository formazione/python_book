PDFTOPPMPATH = r"G:\\poppler\\poppler-0.68.0_x86\\poppler-0.68.0\\bin\\pdftoppm.exe"
PDFFILE = "flash_fattura.pdf"

import subprocess
subprocess.Popen('"%s" -png "%s" out' % (PDFTOPPMPATH, PDFFILE))