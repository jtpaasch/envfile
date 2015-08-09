ENVFILE
=======

Loads/unloads variables from a file into the environment. 


Usage
-----

Suppose you have a file called `.env` with the following contents:

    FOO=a
    BAR=b

You can load those values into your shell as environment variables like this:

    $ source envfile .env

You can later unload those variables from the environment using 
the `-u` or `--unload` flag:

    $ source envfile --unload .env


Interactive
-----------

If you use the `-i` or `--interactive` flag, `envfile` will ask you
about each variable before it loads it into the environment. You can
either just hit `Enter` to accept the current value, or you can type
in a new value.


Output
------

`envfile` prints the variables it loads to STDOUT. You can redirect that
output into a file if you want to save your state. For instance, you can
load the `.env` file from above, but use the interactive flag so you can
provide new values, then save the output as `.env2`:

    $ source envfile --interactive .env > .env2

Then later, you could reload those values into your environment:

    $ source envfile .env2

Help
----

    $ source envfile --help


