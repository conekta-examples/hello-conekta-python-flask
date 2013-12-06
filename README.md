hello-conekta-python-flask
==========================

Bare bones flask app which implements payment calls via conekta-python.

To run, execute the following commands:

virtualenv venv --distribute
source venv/bin/activate
pip install Flask gunicorn
pip install git+git://github.com/conekta/conekta-python.git@api_V0.3.0
foreman start
