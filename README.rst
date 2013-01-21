**************
virtualenv-bin
**************

Tools to install into a python virtualenv to make life easier.
If you install virtualenv-bin into a virtualenv, you will get two useful
programs.

=======
venvbin
=======

If you symlink to this program where it sits in a virtualenv and name the
symlink for any program in the bin folder, executing the symlink will
activate the virtualenv and then run the program, passing through all args
and exit codes.

===========
venvsymlink
===========

Running this from a bin directory will automatically symlink all bins
from that virtualenv into your bin folder using venvbin

=======
example
=======

I want to install and use httpie, but I don't want any of it's dependencies
interfering with my broader environment.  Note: for this example, I use
/opt/virtualenvs for all virtualenvs.

.. code-block:: bash

    $ mkvirtualenv httpie
    $ source /opt/virtualenvs/httpie/bin/activate
    $ pip install --upgrade httpie
    $ pip install virtualenv-bin
    $ cd ~/bin
    $ /opt/virtualenvs/httpie/bin/venvsymlinks
    $ ~/bin/http --help

============
installation
============

You can install virtualenv-bin using pip:

.. code-block:: bash

    $ pip install --upgrade virtualenv-bin


