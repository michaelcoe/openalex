# Some Q&D python tools to get data from OpenAlex, using pyalex.

anton@angelo.nz


## Country Summary (countrysummary.py)
Summary of Open Alex's knowledge of the academic output for a particular country

- You need to set your email, and the ISO country code in openalex.py
- Full openalex results are written into a python dictionary (full results)
- The short list (default 25) of instututions are also in a python dictionary (short results)
- The output is in a csv file. 
## Green, green, everywhere (greenworks.py)
Where are your green OA works, which repository?  Finsd the best OA location (as long as its a repository)

## APC guesses (apcguesses.py)

How much does OA cost?  This script looks at an institution, and gets the _maximum_ cost for all the articles published. Just add the instituion's [ROR id](https://ror.org/)  