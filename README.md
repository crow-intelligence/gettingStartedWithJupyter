# Getting Started with Jupyter

## Start the nb server
```jupyter notebook```

## Notes
+ Tested on Python 3.8.5, IPython 7.18.1
+ Ubuntu 20.04

## Installation notes
NOTE: It is a best practice to use virtual environments.
+ First, install pyppeteer ```pip install pyppeteer```
+ Install the pdf converter ```pip install nbconvert[webpdf]```
+ The webpdf converter first needs to download chromium``` jupyter nbconvert --to webpdf notebooks/Milestone03.ipynb --allow-chromium-download```
