'''
Using pyalex to guess how much we pay in APCs

anton@angelo.nz
'''

import pprint
from pyalex import Works, Authors, Sources, Institutions, Concepts, Publishers, Funders
import pyalex
from itertools import chain
from collections import Counter
import time
import csv

timestr = time.strftime("%Y%m%d-%H%M%S")
yearstr = time.strftime("%Y")

def pretty_to_file(toprint, filename):
    with open(filename, "w", encoding="utf8") as output:
        pprint.pprint(toprint, output)

pyalex.config.email = "anton.angelo@canterbury.ac.nz" # set this to your own email.  It puts you in the openalex polite queue


results_filename =  "apcguesses_results_"+timestr+".csv"
results_directory = "results/"
publication_years = range(2000,2024)

fields_to_report = ["apc_paid","doi","type","authorships"]

with open(results_directory+results_filename, "w",encoding="utf8") as resultsfile:
    resultswriter = csv.writer(resultsfile, quotechar='"')
    resultswriter.writerow(["year", "number_of_works", "output_type","number_of_authors","doi","usd_value"])

    for year in publication_years:
        print(year)
        works = Works() \
                .filter(authorships={"institutions": {"ror": "https://ror.org/03y7q9t39"}}) \
                .filter(is_oa =True) \
                .filter(publication_year=year) \
                .select(fields_to_report) \
                .paginate(per_page=200)

        works_list = []
        for item in chain(*works):
            works_list.append(item)
            
#        pretty_to_file(works_list, "results\guess-full"+timestr+".py")

        number_of_works = len(works_list)

        print(number_of_works)



        for research_output in works_list:
            output_type = research_output["type"]
            doi = research_output["doi"]
            number_of_authors = str(len(research_output["authorships"]))
            if research_output["apc_paid"] != None:
                usd_value = str(research_output["apc_paid"]["value_usd"])
            else:
                usd_value = "0"

            result_list=[year, number_of_works, output_type,number_of_authors,doi,usd_value]
            resultswriter.writerow(result_list)


