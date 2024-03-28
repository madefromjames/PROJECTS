from django.test import TestCase

# Create your tests here.
entries = ['CSS', 'Django', 'Git', 'HTML', 'Python']
def search_substring(query, entries):
    liste = [entry for entry in entries if query.lower() in entry.lower()]
    q = ""
    for li in liste:
        q += li + '\n\n'
    return q

query = input("query: ")

results = search_substring(query, entries)
print(results)