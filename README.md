# Welcome to the tdd-python-book-2021 repository
https://read.amazon.co.uk/?asin=B074HXXXLS

useful Links
`https://docs.github.com/en/free-pro-team@latest/github/using-git/changing-a-remotes-url`

This is the second round of working on this book.
Have a great 2021

Finished work on Friday 8th at 17:38 on page 15

Finished work of about 90 minutes on Tuesday 12th January at 21:50 on page 46.

Finished work of about half an hour on
Sunday 17th January at 14:21 on page 70



## Running Test Code Coverage
`pip install coverage`

`coverage run --source='.' manage.py test`

with branches
`coverage run --source='.' --branch manage.py test`

setup .coveragerc file.

`coverage report -m --omit */dataEngine-env/*` 

`coverage report -m`

`coverage html`

## Tests

`python manage.py test` 

This runs both the unit tests and the functional_tests.

`python manage.py test lists`

This runs only the unit tests

`python manage.py test functional_tests`

This runs only the functional tests