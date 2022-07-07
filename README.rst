cli-imagefetcher
================

Tool enabling users to search for and order EO products.
Python package built with `poetry` which provide an entrypoint to a small 
command line utility built with `typer`.

For an understanding of the application architecture open up the file
`applicationDiagram.drawio` on `App Diagrams <https://app.diagrams.net/>`_.

Distribution
------------
`pip` via `PyPi <https://pypi.org/project/cli-imagefetcher/#history>`_
A repo can also be found on `Github <https://github.com/alanscandrett/cli-imagefetcher>`_

Features
--------

* Search for Items via a Data API using an Area of Interest and Time of Interest.
* Order Items from an Ordering API and download them to disk.
* Builds a CLI utility installable via `pip` for dice rolls from the command line

Command-Line Utility
--------------------

The package also builds a command-line utility, `cli-imagefetcher`, that can be
used directly from the terminal once `pip`-installed (alternately, it can be 
run within the `poetry` environment with 
`poetry run cli-imagefetcher [OPTIONS] COMMAND [ARGS]`).


Mock Data
---------

* multiPolygon.geojson created in `geojson.io <https://geojson.io>`_
* searchResponse.json combined from an example found in [2] and [3]


Next Steps
----------
* Finish docs, diagrams, and docstrings; time got the best of me on these.
* Finish image clipping process, detailed comments in imageManipulation.py.
* Add typing that `typer` supports, time constraint.
* Add multiple orders to the orders array.
* Show image thumbnails previews using python pillow, requests, and a prompt.
* Save session details and creds in an ENV file through optional CLI prompt.
* Further test cases, basic validation of dates and key using Regex.
* Rate Limiting - timeouts around network requests in order.py and search.py
* Cloud cover filter, throw in another param and pass it through to search.py


References
----------

1. `Python CLI Utilities with Poetry and Typer <https://pluralsight.com/tech-blog/python-cli-utilities-with-poetry-and-typer>`_
2. `Data API Getting Started <https://github.com/planetlabs/notebooks/blob/master/jupyter-notebooks/data-api-tutorials/search_and_download_quickstart.ipynb>`_
3. `Data API Quick Search <https://developers.planet.com/docs/apis/data/quick-saved-search/>`_
4. `Order API <https://developers.planet.com/docs/orders/api-mechanics//>`_
5. `Ordering and Deliver <https://github.com/planetlabs/notebooks/blob/master/jupyter-notebooks/orders/ordering_and_delivery.ipynb>`_