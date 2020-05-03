from flask import make_response

def prepare_response(data):
    response = make_response(data) 
    #HTTP Strict Transport Security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

    #X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'

    #X-Frame-Options
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'

    #X-XSS-Protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    return response