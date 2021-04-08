#!/usr/bin/env python

"""
Command line interface 
"""

import argparse
from extract import decimaldegree, extract

def parse_command_line():
    "parses args for the extract function"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--run",
        help="runs the extract",
        action="store_true")

    # parse args
    args = parser.parse_args()

    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()
    pdf_path = input("Please input full pdf path and add .pdf \n") 
    # pass argument to call darwinday function
    if args.run:
        extract(pdf_path)


if __name__== '__main__':    
    extract(pdf_path)