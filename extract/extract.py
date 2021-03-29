#!/usr/bin/env python

"""
A function to extract GPS coordinates from a PDF and outputting a CSV file with coordinates and plotting to a map
"""

## Make a class object where arguments are input path of pdf and output path of maps and csv file
# Class Extract(self, workingdir, pdf_file, outputdir)
	# def __init__: 
		# store input parameters
		# self.workdir = os.path.realpath(os.path.expanduser(workdir))
		# self.pdf_file = pdf_file		
		#store output paramters
		# self.outputdir = outputdir
	# def extract_content(pdf_path):		
		# """
		#This function will extract the content from a PDF file and retrun it
    	#when given a path
    	#"""    	
    	# opening up PDF with tika parser
    	#parsed_pdf = parser.from_file(pdf_path)    	
    	# saving content of PDF
    	#data = parsed_pdf['content']    	
    	#return(data)	
    # maybe combine with above function so end data is pandas DF of coordinates
	# def extract_gps(data):
    # def conversion(X):
    	# geo-pandas package?
    # def pdf_plot(Y):
    	# folium package 

# First step in creating program is to extract the relevant infromation from a PDF 

from tika import parser
import os
import re
import pandas as pd

def extract(pdf_path):
    """This function will parse the PDF into a string and from there it will extract 
    out gps coordiantes from the document
    """
    # opening up PDF with tika parser
    parsed_pdf = parser.from_file(pdf_path)
    
    # saving content of PDF
    pdf_data = parsed_pdf['content'] 

    # pattern for gps coordinates
    pattern = re.compile('''(\d{1,3}°\d{1,3}'\d{1,3}.\d{1,3}''S,\d{1,3}°\d{1,3}'\d{1,3}.\d{1,3}''E)''')  

    # match the pattern to the parsed data .
    gps_cords = pattern.match(pdf_data) 

    print(gps_cords)


# asks user to import the path to pdf that they want extract to get the content from (remeber to have .pdf at end of file --add
# that to the help section)
pdf_path = os.path.realpath("../project/documents/MurphyRTL2017.pdf") 


-------
# We discussed in out paired-programming meetings that once you are able to extract and convert decimal GPS points, your goal
# will be to plot these. In our group meeting, Jared mentioned the plotting program Folium. 

# Here is an example of plotting longitude and latitude points using folium

import folium
mapit = None
latlon = [ (51.249443914705175, -0.13878830247011467), (51.249443914705175, -0.13878830247011467), (51.249768239976866, -2.8610415615063034)]
for coord in latlon:
    mapit = folium.Map( location=[ coord[0], coord[1] ] )

mapit.save( 'map.html')

-------
