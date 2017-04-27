# WOFpy

[![Build Status](https://travis-ci.org/ODM2/WOFpy.svg?branch=master)](https://travis-ci.org/ODM2/WOFpy) [![Build status](https://ci.appveyor.com/api/projects/status/piji7ib6wdjeoqku?svg=true)](https://ci.appveyor.com/project/ocefpaf/wofpy-4g2xh)

WOFpy is a Python package that implements [CUAHSI's](http://his.cuahsi.org) WaterOneFlow Web service.
WaterOneFlow is a Web service with methods for querying time series of water data at point locations,
and which returns data in WaterML format,
providing standardized access to water data.

WOFpy reads data from a Data Access Object (DAO) and translates the data into WaterML.
DAOs can represent a variety of data sources,
including databases, text files, and Web sites or services.
You can view example DAOs in the examples folder,
or write your own based on the BaseDao class in `wof/dao.py`.

WOFpy uses Python version 2.7.

Documentation
-------------

Extensive documentation is available at http://pythonhosted.org/WOFpy/

Installation
------------
In general, the easiest method is to utilize the conda package from the [ODM2](https://conda.anaconda.org/odm2) channel.

```
conda install wofpy --channel odm2
```


ODM2 and ODM1 Instructions
--------------------------

This is new material that is up to date.
The sections "Running the Examples" and "Publishing Your Data",
below, *might* be out of date.

- [ODM2](https://github.com/ODM2/WOFpy/blob/master/docs/Sphinx/ODM2Services.rst)
- [ODM1](https://github.com/ODM2/WOFpy/blob/master/docs/Sphinx/ODM1Services.rst)

Running the Examples
--------------------

Example services are included with WOFpy.
Each example consists of data,
Data Access Objects (DAOs), models,
and the service definition.
The examples are located in the **examples** folder.
See the documentation for more information.

A quick way to use the examples is via the `wofpy_config` CLI.
Type `wofpy_config --help` to display the usage Instructions.

```shell
wofpy_config MyWorkingDirectory
```

The command above will create and populate the `MyWorkingDirectory` with the files needed to run the `odm2 timeseries` example.
Right now that is is only one tested example, in the future extra options will enable the user to choose the base example used.

Publishing Your Data
--------------------

Follow the general steps below to publish your data with WOFpy.

1. Write a new DAO class based on wof.dao.BaseDao;
   the methods should return objects as defined in wof.models.
   This class helps WOFpy read your data.
2. Write a new config file like those found in the examples,
   e.g. examples/swis/swis_config.cfg.
   This file contains static descriptors of your Web service such as the name of your water observations network.
3. Write a new runserver script to use the new DAO you implemented.
   See files named runserver_*.py in the examples folder for examples.
4. To test, open a command window,
   navigate where your runserver file is located,
   and use Python to run the script, e.g., python runserver.py.

Credits
-------

This work was supported by National Science Foundation Grant [ACI-1339834](http://www.nsf.gov/awardsearch/showAward?AWD_ID=1339834).
Any opinions, findings,
and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
