ENVFILE
=======

Loads/unloads variables from a file into the environment.

    $ source envfile --help


Usage
-----

Create a file with some regular old bash variables in it, e.g.:

    $ echo 'FOO=a' >> .env
    $ echo 'BAR=b' >> .env

Load those into the environment as environment variables:

    $ source envfile .env

Confirm that it worked.

    $ echo $FOO # outputs 'a'

Unload the variables from the environment:

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

