Quickstart
==========

Installation
------------

python-codeforces can be installed using ``pip`` as follows:

.. code-block:: shell

   pip install python-codeforces

Installation from source can be done from the root of the project with
the following command.

.. code-block:: shell

   pip install .

Using python-codeforces
-----------------------

Introduction
^^^^^^^^^^^^

Direct `API <https://codeforces.com/api/help>`_ calls can be made with the ``codeforces.api.call`` function. For Example:

.. code-block:: python

   >>> from codeforces import api
   >>> api.call('user.info', handles="mukundan314")
   [{'lastName': 'Senthil', 'country': 'India', 'lastOnlineTimeSeconds': 1547349164, 'city': 'Coimbatore', 'rating': 1495, 'friendOfCount': 4, 'titlePhoto': '//userpic.codeforces.com/765517/title/93ffab462a95eb16.jpg', 'handle': 'Mukundan314', 'avatar': '//userpic.codeforces.com/765517/avatar/b0cea461ab905c83.jpg', 'firstName': 'Mukundan', 'contribution': 0, 'organization': 'Block Lab', 'rank': 'specialist', 'maxRating': 1502, 'registrationTimeSeconds': 1531657670, 'email': 'mukundan314@gmail.com', 'maxRank': 'specialist'}]

Authorization
^^^^^^^^^^^^^

To make authorized API calls you need to generate a API key at https://codeforces.com/settings/api.

And when making authorized call:

.. code-block:: python

   from codeforces import api

   api_key = "xxx"
   api_secret = "yyy"

   api.call("method_name", key=api_key, secret=api_secret, arg=arg_for_method)
