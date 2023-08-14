Adding and updating locales
---------------------------

For every language you want to translate into you need a
locales/[language]/LC_MESSAGES/slc_web.po
(e.g. locales/de/LC_MESSAGES/slc_web.po)

For German

.. code-block:: console

    $ mkdir de

For updating locales

.. code-block:: console

    $ ./bin/update_locale

Note
----

The script uses ``gettext`` package for internationalization.

Install it before running the script.

On Linux
--------

.. code-block:: console

    $ sudo apt install gettext

On macOS
--------

.. code-block:: console

    $ brew install gettext

On Windows
----------

see https://mlocati.github.io/articles/gettext-iconv-windows.html


Python dependencies
-------------------

You need to install dependencies for updating locales,
executing the following command:

.. code-block:: console

    $ pip install i18ndude==5.5.0
