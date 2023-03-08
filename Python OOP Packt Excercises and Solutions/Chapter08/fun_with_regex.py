import re

search_string = "hello world"
pattern = "hello world"

if match := re.match(pattern, search_string):
    print("regex matches")


# email address
pattern = "^[a-zA-Z.]+@([a-z.]*\.[a-z]+)$"
search_string = "some.user@example.com"
if match := re.match(pattern, search_string):
    domain = match.groups()[0]
    print(domain)
