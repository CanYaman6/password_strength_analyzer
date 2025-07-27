Password Strength Analyzer and Wordlist Generator
Overview
A Python tool to analyze password strength using zxcvbn and generate custom wordlists with variations (leetspeak, years) for cybersecurity testing. Includes a 1-2 page LaTeX report. Built for a cybersecurity course (Project 4).
Repository Contents

password_analyzer.py: Python script for password analysis and wordlist generation.
project_report.tex: LaTeX source for the report.
project_report.pdf: Compiled PDF report.
README.md: This file.

Prerequisites

Python 3 with zxcvbn (pip install zxcvbn).
LaTeX: MiKTeX (Windows), TeX Live (Linux), MacTeX (macOS), or Overleaf (online).

Setup

Clone the repository:git clone <repository-url>
cd <repository-folder>


Install Python library:pip install zxcvbn


Install LaTeX (optional if using Overleaf): Download MiKTeX (miktex.org) or use Overleaf.

Usage
Run the Script

Analyze password:python password_analyzer.py --password "P@ssw0rd"


Generate wordlist:python password_analyzer.py --inputs Mr.Robot 110 --output mylist.txt


Both:python password_analyzer.py --password "P@ssw0rd" --inputs Mr.Robot 110 --output mylist.txt



Compile the Report

Local (MiKTeX/TeX Live):cd <path-to-repository>
latexmk -pdf project_report.tex


Overleaf:
Upload project_report.tex to Overleaf.
Click “Recompile” to generate PDF.
Download project_report.pdf.



Deliverables

Code: password_analyzer.py for password analysis and wordlist generation.

Troubleshooting

Python: Ensure zxcvbn is installed and Python 3 is in PATH.
LaTeX: Allow MiKTeX to install packages (e.g., lmodern). Use latexmk -pdf -verbose for error details or switch to Overleaf.

License
For educational use only. Do not use for unauthorized activities.
