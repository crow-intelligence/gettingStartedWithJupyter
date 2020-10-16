# Getting Started with Jupyter

## Notes
+ Tested on Python 3.8.5, IPython 7.18.1
+ Ubuntu 20.04

## Installation notes
+ First, install pyppeteer ```pip install pyppeteer```
+ Install the pdf converter ```pip install nbconvert[webpdf]```
+ The webpdf converter first needs to download chromium``` jupyter nbconvert --to webpdf notebooks/Milestone03.ipynb --allow-chromium-download```
