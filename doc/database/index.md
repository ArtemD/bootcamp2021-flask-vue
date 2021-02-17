Module database
===============

Sub-modules
-----------
* database.operations

Variables
---------

    
`DATABASE_URL`
:   Database URI string

    
`Session`
:   Database session

    
`db`
:   Database connection

Classes
-------

`License(**kwargs)`
:   License object
    
    A simple constructor that allows initialization from kwargs.
    
    Sets attributes on the constructed instance using the names and
    values in ``kwargs``.
    
    Only keys that are present as
    attributes of the instance's class are allowed. These could be,
    for example, any mapped columns or relationships.

    ### Ancestors (in MRO)

    * sqlalchemy.ext.declarative.api.Base

    ### Instance variables

    `address`
    :   Address

    `business_id`
    :   Business id or N/A if not applicable

    `city`
    :   City

    `created_at`
    :   Automatically generated date and time of insertion

    `id`
    :   Primary key

    `license_granting_date`
    :   License granting date in format dd.mm.yyyy

    `license_type`
    :   License type as a string (in Finnish)

    `name`
    :   License holder's name

    `postcode`
    :   Postcode