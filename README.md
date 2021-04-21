# `extract`

`extract` is a Python package which processes PDF files and extracts GPS coordinates. This pacakge will extract and clean GPS coordinate data to produce an interactive map. In addition, a csv file of the GPS coordinates will output to the documents subdirectory. 

---
## In development 

The following packages are needed to run the extract package: 

-``tika`` Java version 7 is needed

-``pandas``

-``folium`` 

To install the following packages use 

```
conda install -c conda-forge folium pandas tika
```

To contribute to the development of `extract`, you can clone this repository using the following commands: 

```
git clone git@github.com:aparnac25/extract.git
cd ./extract
```

### To install and run code

-Install

```
cd ./extract
pip install -e .
```

-Run

Open a jupyter notebook. Run the folowing code to run `extract`. The PDF path will be to the downloaded extract folder in the documents subdirectory where the test PDF "MurphyRTL2017.pdf" can be found. Currently the `extract` module only has one set of GPS coordinates. 

```
from extract import extract

extract("/Insert/Pdf/Path/to/extract/documents/MurphyRTL2017.pdf")
```
