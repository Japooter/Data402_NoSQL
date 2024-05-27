import pymongo
client = pymongo.MongoClient()

# Both of these lines work
db = client.starwars
# db = client["starwars"]


# This is a commented-out first test of pymongo, it is not an exercise

# luke = db.characters.find_one({'name': 'Luke Skywalker'})
#
# print(luke['species'])
#
# smaller_luke_theory = db.characters.find_one({'name': 'Luke Skywalker'},
#                               {"name": 1, "height": 1, "_id": 0})
# print(smaller_luke_theory)
#
# print(db.characters.find_one({'name': 'Ackbar'})['species'])
#
# droids = db.characters.find({'species.name': 'Droid'})
# for i in droids:
#     print(i['name'])

print('\n Exercise 1:')
vader_height = db.characters.find_one({'name': 'Darth Vader'}, {'name': 1, 'height': 1, '_id': 0})
print(vader_height)

print('\n Exercise 2:')
yellow_eyes = db.characters.find({'eye_color': 'yellow'}, {'name': 1, '_id': 0})
for names in yellow_eyes:
    print(names)

print('\n Exercise 3:')
males = db.characters.find({'gender': 'male'}, {'name': 1, '_id': 0})
for i in range(0, 3):
    print(males[i])

print('\n Exercise 4')
maybe_dead = db.characters.find({'homeworld.name': 'Alderaan'},
                                {'name': 1, 'homeworld.name': 1, '_id': 0})
for rip in maybe_dead:
    print(rip)

# Aggregation exercises

print('\n Aggregation Exercise 1')
avg_female_height = db.characters.aggregate([{'$match': {'gender': 'female'}},
                                             {'$group': {'_id': '$gender',
                                                         'heightAvg': {'$avg': '$height'}}}])
for i in avg_female_height:
    print(i)

print('\n Aggregation Exercise 2')
tallest_character = db.characters.aggregate([{'$project': { 'maxHeight': {'$max': '$height'},
                                                            'nameList': {'$max': '$name'}}}])
height_list = []
name_list = []
for i in tallest_character:
    # print(i)
    if i['maxHeight'] != None:

        #print(i['maxHeight'])
        height_list.append(i['maxHeight'])
        name_list.append(i['nameList'])
# print(max(height_list))
ref = height_list.index(max(height_list))
# print(name_list[ref])
print(f"The tallest character is {name_list[ref]}, with a height of {max(height_list)} cm.")


# starships_attempt = db.starships.aggregate([
#   { '$lookup': {
#     'from': "characters",
#     'localField': "pilot",
#     'foreignField': "_id",
#     'as': "matched_pilot"
#   } },
#     { '$project': {'name': 1, 'model': 1, 'matched_pilot.name': 1}}
# ])
#
# for star_info in starships_attempt:
#     print(star_info)

find_pilot = db.characters.aggregate([
    {'$lookup': {
        'from': 'starships',
        'localField': '_id',
        'foreignField': 'pilot',
        'as': 'pilot_for'
    } },
    {'$match': {'pilot_for': {'$nin': [[]]}}},
    {'$project': {'name': 1, 'homeworld.name': 1, 'pilot_for.name': 1, 'pilot_for.model': 1,
                  'pilot_for.manufacturer': 1, '_id': 0}}

])

for star_info in find_pilot:
    print('\n')
    print(star_info)


# Max height
max_height = db.characters.aggregate([
    {"$group":
         {"_id": None, "max_height": {"$max": "$height"}}
    }
]).next()["max_height"]

for tallest in db.characters.find({"height": max_height}):
    print(tallest["name"], tallest["height"])