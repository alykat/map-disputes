#!/usr/bin/env python

import argparse
from flask import Flask, render_template

import app_config
from render_utils import make_context, urlencode_filter
import static

app = Flask(__name__)

app.jinja_env.filters['urlencode'] = urlencode_filter

# Example application views
@app.route('/')
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """

    context = make_context()

    # TODO(katie): dummy data, remove this
    context['disputes'] = [
        { 'name': 'Crimea',
          'slug': 'crimea',
          'image_us': 'http://cl.ly/image/0U3I3c30302z/Screen%20Shot%202014-06-22%20at%209.46.37%20AM.png',
          'claimants': [{'name': 'Russia',
                          'slug': 'russia',
                          'url': 'http://cl.ly/image/3U2O2I3W3N04/Screen%20Shot%202014-06-22%20at%209.46.07%20AM.png'},
                        {'name': 'Ukraine',
                          'slug': 'ukraine',
                          'url': 'http://cl.ly/image/0U3I3c30302z/Screen%20Shot%202014-06-22%20at%209.46.37%20AM.png'}]
        },
        { 'name': 'Jammu and Kashmir',
          'slug': 'jammu-kashmir',
          'image_us': 'http://f.cl.ly/items/2W2y3k1C102l0H2a453Q/Screen%20Shot%202014-06-22%20at%209.47.05%20AM.png',
          'claimants': [{'name': 'India',
                          'slug': 'india',
                          'url': 'http://cl.ly/image/3G2G0h063g3A/Screen%20Shot%202014-06-22%20at%209.46.59%20AM.png'}]
        }]

    return render_template('index.html', **context)

app.register_blueprint(static.static)

# Boilerplate
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port')
    args = parser.parse_args()
    server_port = 8000

    if args.port:
        server_port = int(args.port)

    app.run(host='0.0.0.0', port=server_port, debug=app_config.DEBUG)
