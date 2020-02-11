from pymongo import MongoClient


def queryNear(point):
    return {"location": {"$near": {"$geometry": point, "$maxDistance": 2000, "$minDistance": 0}}}


def getCompaniesNear(db, table_locations)
  compsnear = []
   for i, _ in enumerate(sbs.location):
        try:
            compsnear.append(list(over1m.collection.find(
                {"$and": [queryNear(table_locations[i]), search]}, {"name": 1, "_id": 0})))
        except:
            continue

    flatcompsnearSB = [val for sublist in compsnearSB for val in sublist]
    names = [[value for value in dict.values()] for dict in flatcompsnearSB]
    flatnames = [val for sublist in names for val in sublist]
    unique = set(flatnames)
    return list(unique)
