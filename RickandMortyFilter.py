import requests
import json
import pandas
import argparse
import re

url = "https://rickandmortyapi.com/api/character/"

def search_character(search):
    r = requests.get(url, params=search)
    data = r.json()
    characters = data['results']
        
    df = pandas.DataFrame(characters)
    df['episode'] =  df['episode'].apply(lambda x: ", ".join(x))
    df['episode'] = df['episode'].apply(lambda x: re.sub(r'[^0-9,]', '',x))

    columns = df[['name','status','species','gender','episode']]
    print(columns)

def main():

    parser = argparse.ArgumentParser(description="Filter characters from Rick and Morty API")
    parser.add_argument("-n", "--name", type=str, help="The name of the character.")
    parser.add_argument("-s", "--status", type=str, help="The status of the character ('Alive','Dead' or 'unknown').")
    parser.add_argument("-p", "--species", type=str, help="The species of the character.")
    parser.add_argument("-g", "--gender", type=str, help="The gender of the character ('Female','Male','Genderless' or 'unknown')")

    args = parser.parse_args()

    search = {}
    if args.name:
        search['name'] = args.name
    if args.status:
        search['status'] = args.status
    if args.species:
        search['species'] = args.species
    if args.gender:
        search['gender'] = args.gender

    search_character(search=search)

if __name__ == "__main__":
    main()
