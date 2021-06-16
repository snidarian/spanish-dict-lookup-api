#!/usr/bin/python3


import argparse as ap
import requests as rq
import json as j
from colorama import Style, Fore


# ANSI color sequence codes
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE
yellow = Fore.YELLOW
reset = Fore.RESET


# ---------------------------------------------------------------------------
# argparse setup

parser = ap.ArgumentParser(description="Uses api.dictionaryapi to define Spanish words in Spanish")
parser.add_argument("query", help="Dict term for definition", type=str)
parser.add_argument('--json', "--джсон", help="prints additional prettified json of returned data", action='store_true')
args = parser.parse_args()

# ---------------------------------------------------------------------------
# Get Request from web api

# requests to the api are made in the following fashion
#result = rq.get('https://api.dictionaryapi.dev/api/v2/entries/'langauge_code'/'query_term')

result = rq.get(f'https://api.dictionaryapi.dev/api/v2/entries/es/{args.query}')


json_payload = result.json()

#print(type(json_payload))
#print(json_payload)

#print(type(result))
#print(type(json_payload[0]))

# ------------------------------------------------------------------------------
# print output of data to terminal


try:
    # .json() method returns list with json as the zeroth item
    json_payload = json_payload[0]
    # The definitions list is nested within the json structure.
    definitions_list = json_payload['meanings'][0]['definitions']
    number_order = 1
    # cycle through list items and print numbered definition for each with following example (if any)
    for definition_item in definitions_list:
        print(str(number_order), end=". ")
        number_order+=1
        print(green + definition_item['definition'] + reset)
        # if there's an example for a given definition, print it, otherwise DO NOT throw an error and disrupt program
        try:
            print("\tEjemplo: " + yellow + definition_item['example'] + reset)
        except:
            print(red + "\tNo hay ejemplos en cuanto a esta definicion..." + reset)
    # prettified json structure of json returned from web api
    if args.json:
        prettified_json_object = j.dumps(json_payload, indent=2, ensure_ascii=False)
        # prints prettified json structure as python object
        print(prettified_json_object)
except KeyError:
    print("No definition available for that term")



