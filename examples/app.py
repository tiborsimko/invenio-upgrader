# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.


"""Minimal Flask application example for development.

Create database and tables:
.. code-block:: console
   $ cd examples
   $ flask -a app.py db init
   $ flask -a app.py db create


Common upgrader commands:

.. code-block:: console
   $ flask -a app.py upgrader pending
"""

from __future__ import absolute_import, print_function

import os

from flask import Flask
from flask_cli import FlaskCLI
from invenio_db import InvenioDB

from invenio_upgrader import InvenioUpgrader

# Create Flask application
app = Flask(__name__)
app.config.update(
    SECRET_KEY="CHANGE_ME",
    SQLALCHEMY_DATABASE_URI=os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db'
    ),
    CFG_LOGDIR='/tmp',
    TESTING=True,
)
FlaskCLI(app)
InvenioDB(app)
InvenioUpgrader(app)

if __name__ == "__main__":
    app.run()
