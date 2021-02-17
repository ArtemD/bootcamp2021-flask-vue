from database import License, Session, License
from sqlalchemy import or_

def __get_session():
    return Session()

def insert_db_data(name, address, postcode, city, date, type, businessid):
    new_row = License(name=name, address=address, postcode=postcode, city=city, license_granting_date=date,
                    license_type=type, business_id=businessid)
    db = __get_session()
    db.add(new_row)
    db.commit()
    id = new_row.id
    db.close()
    return id
    

def search_db_data(keyword):
    return __get_session().query(License).filter(or_(License.name.ilike('%{0}%'.format(keyword)), License.business_id.ilike('%{0}%'.format(keyword))))

def get_db_data():
    return __get_session().query(License).all()