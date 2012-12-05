=====
scaws
=====

This project contains some components and extensions for using Scrapy on Amazon
AWS.

Requirements
============

* Scrapy 0.13 or above
* boto 1.8 or above

Install
=======

Download and run: ``python setup.py install``

Available components
====================

SimpleDB stats collector
------------------------

Module: ``scaws.statscol``

.. class:: SimpledbStatsCollector

    A Stats collector which persists stats to `Amazon SimpleDB`_, using one
    SimpleDB item per scraping run (ie. it keeps history of all scraping runs).
    The data is persisted to the SimpleDB domain specified by the
    `STATS_SDB_DOMAIN`_ setting. The domain will be created if it
    doesn't exist.
    
    In addition to the existing stats keys, the following keys are added at
    persitance time:

        * ``spider``: the spider name (so you can use it later for querying stats
          for that spider)
        * ``timestamp``: the timestamp when the stats were persisted

    Both the ``spider`` and ``timestamp`` are used to generate the SimpleDB
    item name in order to avoid overwriting stats of previous scraping runs.

    As `required by SimpleDB`_, datetimes are stored in ISO 8601 format and
    numbers are zero-padded to 16 digits. Negative numbers are not currently
    supported.

    This Stats Collector requires the `boto`_ library.

.. _Amazon SimpleDB: http://aws.amazon.com/simpledb/
.. _required by SimpleDB: http://docs.amazonwebservices.com/AmazonSimpleDB/2009-04-15/DeveloperGuide/ZeroPadding.html
.. _boto: http://code.google.com/p/boto/

This Stats Collector can be configured through the following settings:

* `STATS_SDB_DOMAIN`_
* `STATS_SDB_ASYNC`_

.. _STATS_SDB_DOMAIN:

STATS_SDB_DOMAIN
~~~~~~~~~~~~~~~~

Default: ``'scrapy_stats'``

A string containing the SimpleDB domain to use for collecting the stats.

.. _STATS_SDB_ASYNC:

STATS_SDB_ASYNC
~~~~~~~~~~~~~~~

Default: ``False``

If ``True``, communication with SimpleDB will be performed asynchronously. If
``False`` blocking IO will be used instead. This is the default as using
asynchronous communication can result in the stats not being persisted if the
Scrapy engine is shut down in the middle (for example, when you run only one
spider in a process and then exit).


