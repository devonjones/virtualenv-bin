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

-------
example
-------

I want to install and use httpie, but I don't want any of it's dependencies
interfering with my broader environment.  Note: for this example, I use
/opt/virtualenvs for all virtualenvs.

.. code-block:: bash

    $ mkvirtualenv httpie
    $ source /opt/virtualenvs/httpie/bin/activate
    $ pip install --upgrade httpie
    $ pip install virtualenv-bin
    $ cd ~/bin
    $ ln -s /opt/virtualenvs/httpie/bin/venvbin http
    $ ~/bin/http example.org

    HTTP/1.0 302 Found
    Connection: Keep-Alive
    Content-Length: 0
    Location: http://www.iana.org/domains/example/
    Server: BigIP

===========
venvsymlink
===========

Running this from a bin directory will automatically symlink all bins (except
the ones that are in all virtualenvs as well as any bins from virtualenv-bin)
from that virtualenv into your bin folder using venvbin

-------
example
-------

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
    $ ~/bin/http example.org

    HTTP/1.0 302 Found
    Connection: Keep-Alive
    Content-Length: 0
    Location: http://www.iana.org/domains/example/
    Server: BigIP

==========
venvlaunch
==========

Running this lets you execute a program that is inside a virtualenv directly

-------
example
-------

Here we are going to run http from directly inside the virtualenv.

.. code-block:: bash

    $ mkvirtualenv httpie
    $ source /opt/virtualenvs/httpie/bin/activate
    $ pip install --upgrade httpie
    $ pip install virtualenv-bin
    $ cd ~/bin
    $ /opt/virtualenvs/httpie/bin/venvsymlinks
    $ ~/bin/http --help
    $ /opt/virtualenvs/httpie/bin/venvlaunch http example.org

    HTTP/1.0 302 Found
    Connection: Keep-Alive
    Content-Length: 0
    Location: http://www.iana.org/domains/example/
    Server: BigIP



============
installation
============

You can install virtualenv-bin using pip.  There's no point to installing this
anywhere other then into a virtualenv you want to use it with.

.. code-block:: bash

    $ pip install virtualenv-bin


