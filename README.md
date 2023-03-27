## Dojo assignment: Counter

# What I learned:
How to decode a cookie:
open python shell
First import:
>> import base64
Then run this command:
>> base64.urlsafe_b64decode('date_from_cookie_up_to_but_not_including_.')

Returns:
b'{"key":value}'

Forms can use GET method if they aren't sending any information to the server to process. For example, my reset button works as a form though it is just resetting session['counter'].