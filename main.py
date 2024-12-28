import requests
import time
import csv

database = {}
with open("Database.csv","r") as f:
    cr = csv.reader(f)
    for row in cr:
        database[row[1]] = row[2]

spawn_url = "https://poketwitch.bframework.de/info/events/last_spawn/"
webhook_url = ""

while True:
    spawn_info = requests.get("https://poketwitch.bframework.de/info/events/last_spawn/").json()
    pokedex_id = str(spawn_info["pokedex_id"])

    data = {
        "content": f"{database[pokedex_id]} Spawn"
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Spawn Info posted successfully")
    else:
        print(f"Failed to send Spawn Info. Status code: {response.status_code}")
    
    print("Sleeping for",spawn_info["next_spawn"]+2)
    time.sleep(spawn_info["next_spawn"]+2)