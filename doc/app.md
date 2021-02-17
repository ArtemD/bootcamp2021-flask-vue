Module app
==========

Variables
---------

    
`app`
:   Flask instance

Functions
---------

    
`api()`
:   Return all rows found in database in JSON format

    
`form()`
:   Display form for content insertion

    
`index()`
:   Display homepage template

    
`search(keyword=None)`
:   Display search results in JSON format
    
    Parameters
    ----------
    keyword : str
        Search keyword. Default None

    
`submit()`
:   Process form's data or redirect if data is not correct.
    
    Also redirects if methods!=POST