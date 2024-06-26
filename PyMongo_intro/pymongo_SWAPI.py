import requests
# import json
import pymongo

client = pymongo.MongoClient()
db = client.starwars
db.starships.drop()
db.create_collection("starships")

# url = f'https://swapi.dev/api/starships/?page=4'
# response = requests.get(url)
# sw_list_full = json.loads(response.text)
# sw_list = response.json()['results']
# print(sw_list_full)
# print(response.json()['next'])


def starship_info(starship_name):
    page_num = 1
    url = f'https://swapi.dev/api/starships/?page={page_num}'
    response = requests.get(url)
    sw_list = response.json()['results']
    # print('\n \n')
    # print(sw_list)
    # print(response.json()['next'])

    pilot_names = []
    ship_check = False
    next_page = True
    while next_page:
        for ship_names in sw_list:
            if ship_names['name'] == starship_name:
                # print(f"Information on {starship_name}:")
                # print(ship_names['url'])
                # print(ship_names['model'])
                # print(ship_names['manufacturer'])
                # print(ship_names['length'])
                # print(ship_names['max_atmosphering_speed'])
                # print(ship_names['crew'])
                # print(ship_names['passengers'])
                # print(ship_names['pilots'])

                pilots_list = (ship_names['pilots'])
                ship_check = True
                # print(pilots_list)
        if response.json()['next'] is None:
            next_page = False
        else:
            page_num += 1
            url = f'https://swapi.dev/api/starships/?page={page_num}'
            response = requests.get(url)
            response_data = response.json()
            sw_list = response_data['results']

    if ship_check is False:
        #
        return "No such ship."

    for pilot in pilots_list:
        pilot_url = pilot
        response_pilot = requests.get(pilot_url)
        pilot_names.append(response_pilot.json()['name'])

    # print(pilot_names)
    id_list = []
    for a_pilot in pilot_names:
        # print(db.characters.find_one({
        #     'name': a_pilot
        # },
        #     {'name': 1}))
        pilot_objid = db.characters.find_one({
            'name': a_pilot
        },
            {'name': 1})['_id']
        id_list.append(pilot_objid)

    return id_list


def add_starship(starship_name):

    next_page = True
    id_list = starship_info(starship_name)
    if id_list == "No such ship.":
        return
    page_num_b = 1

    while next_page:
        url_2 = f'https://swapi.dev/api/starships/?page={page_num_b}'
        response_2 = requests.get(url_2)
        response_data = response_2.json()
        print(response_data)
        sw_list_2 = response_data['results']

        print(id_list)
        # db.temp_test.insert_one({'pilot': id_list})
        # what_was_added = db.temp_test.find_one({'pilot': id_list})
        # print(what_was_added)

        for ship in sw_list_2:
            if ship['name'] == starship_name:
                # ship_name = ship['name']
                # ship_model = ship['model']
                # ship_manu = ship['manufacturer']
                # ship_len = ship['length']
                # ship_maspeed =
                # ship_crew
                # ship_pass
                db.starships.insert_one({
                    'name': ship['name'],
                    'model': ship['model'],
                    'manufacturer': ship['manufacturer'],
                    'length': ship['length'],
                    'max_atmosphering_speed': ship['max_atmosphering_speed'],
                    'crew': ship['crew'],
                    'passengers': ship['passengers'],
                    'pilot': id_list


                })
                print("Passed")
                return
        else:
            if response_data['next'] is None:
                next_page = False
            else:
                page_num_b += 1


def all_starships():
    page_check = True
    page_num = 1
    while page_check:

        url = f'https://swapi.dev/api/starships/?page={page_num}'
        response = requests.get(url)
        # sw_list_full = json.loads(response.text)
        response_data = response.json()
        sw_list = response_data['results']
        for ship_names in sw_list:
            pilot_names = []

            pilots_list = (ship_names['pilots'])
            # ship_check = True
            # print(pilots_list)

            for pilot in pilots_list:
                pilot_url = pilot
                response_pilot = requests.get(pilot_url)
                pilot_names.append(response_pilot.json()['name'])

        # print(pilot_names)
            id_list = []
            for a_pilot in pilot_names:
                # print(db.characters.find_one({
                #     'name': a_pilot
                # },
                #     {'name': 1}))
                pilot_objid = db.characters.find_one({
                    'name': a_pilot
                },
                    {'name': 1})['_id']
                # print(pilot_objid)
                id_list.append(pilot_objid)
            db.starships.insert_one({
                'name': ship_names['name'],
                'model': ship_names['model'],
                'manufacturer': ship_names['manufacturer'],
                'length': ship_names['length'],
                'max_atmosphering_speed': ship_names['max_atmosphering_speed'],
                'crew': ship_names['crew'],
                'passengers': ship_names['passengers'],
                'pilot': id_list
            })
        else:
            print("Page complete")
            if response_data['next'] is None:
                # page_check = False
                print("All pages checked")
                return 0
            else:
                page_num += 1


# print(starship_info('Slave 1'))
# add_starship('Slave 1')
all_starships()
