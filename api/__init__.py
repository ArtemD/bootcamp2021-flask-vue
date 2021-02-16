from flask import jsonify, abort
from database.operations import search_db_data, get_db_data

def __generate_json(results):
    data = []
    line = 0 

    for row in results:
        r = [row['name'],row['address'], row['postcode'],  row['city'],  row['license_granting_date'],  row['license_type'], row['business_id']]
        data.insert(line, r)
        line +=1

    return jsonify({'data': data})

def get_json(all=True, search_keyword=None):
    if all==True:
        results = get_db_data()
        return __generate_json(results)
    elif all==False and search_keyword!=None:
        results = search_db_data(search_keyword)
        return __generate_json(results)
    else:
        abort(404)