RefStack Configuration
===========================

This is our documentation for how we get this set up::

1. Git you clone: `git clone http://github.com/stackforge/refstack`

1. Enter the directory: `cd refstack`

1. Setup or update the database

  1. NOTE: you are going to have to modify the db connection string in `alembic.ini` to get this working
  1. PROTIP: if you just want to test this out, use `-n alembic_sqlite` to
      1. `make a local sqlite db`
      1. `$ alembic -n alembic_sqlite upgrade head`
      1. `alembic upgrade head`

1. Plug this bad boy into your server infrastructure.
  1. We use nginx and gunicorn, you may use something else if you are smarter than we are.
  1. For the most basic setup that you can try right now, just kick off gunicorn:
    1. `gunicorn -b 0.0.0.0:8000 refstack.web:app`

1. To actually configure this winner, check out the config section and crack open refstack.cfg in vim.
  1. `vim refstack.cfg`

1. Now browse to `http://localhost:8000`
