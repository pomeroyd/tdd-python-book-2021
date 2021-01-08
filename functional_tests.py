from selenium import webdriver

browser = webdriver.Firefox()

assert 'Django' in browser.title

# Edith has heard about a cool new online to-do app.
# She goes to check out its homepage

browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists.
assert 'To-Do' in browser.title

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box. 
# (Edith's hobby is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

#There is still a text box inviting her to add another item.