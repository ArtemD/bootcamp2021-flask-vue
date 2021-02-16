from database import db, text

def insert_db_data(name, address, postcode, city, date, type, businessid):
    sql = text("""INSERT INTO 
    alcohol_license_places("name", address, postcode, city, license_granting_date, license_type, business_id)
    VALUES ( :name, :address, :postcode, :city, :date, :license_type, :bid )""")
    return db.execute(sql, {'name':name, 'address':address, 'postcode':postcode, 'city':city, 'date':date, 'license_type':type, 'bid':businessid})

def search_db_data(keyword):
    clean_keyword = keyword.replace(';', '')
    clean_keyword2 = clean_keyword.replace('\\', '')
    sql = "SELECT * from alcohol_license_places WHERE \"name\" LIKE '%%{0}%%' OR business_id LIKE '%%{0}%%'".format(clean_keyword2)
    results = db.execute(sql)
    return results

def get_db_data():
    sql = text('SELECT * from alcohol_license_places')
    results = db.execute(sql)
    return results