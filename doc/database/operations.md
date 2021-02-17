Module database.operations
==========================

Functions
---------

    
`get_db_data()`
:   Returns all rows found in database

    
`insert_db_data(name, address, postcode, city, date, type, businessid)`
:   Insert new row into database
    
    Returns
    -------
    int
        Id of the row inserted

    
`search_db_data(keyword)`
:   Return all rows matching keyword (searches name and business_id)