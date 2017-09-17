File upload script
==================
A simple file upload script using the [Bottle web framework][bottle-home].

Running with python
-------------------
First make sure the Bottle framework can be imported without any problems:

    $ python -c 'import bottle'

You should then be able to run `file_upload.py` without any problem:

    $ python file_upload.py
    Bottle v0.12.13 server starting up (using WSGIRefServer())...
    Listening on http://0.0.0.0:8080/
    Hit Ctrl-C to quit.

Running under Apache with mod_wsgi
----------------------------------
Alternatively you can run the upload script behind Apache using
[mod_wsgi][mod_wsgi-docs]. To do this you will need Apache configuration
similar to the following:

    <IfModule !wsgi_module>
    LoadModule wsgi_module modules/mod_wsgi.so
    </IfModule>

    WSGIScriptAlias /upload /var/www/file_upload/file_upload.py

__Note__: you may also want to add authentication, refer to the [Apache
docs][apache-auth-docs] for info on how to do this.

Alternative upload directory
----------------------------
Be default files are uploaded to the `files` directory. This behaviour can be
changed by updating `file_upload.conf`.

[apache-auth-docs]: https://httpd.apache.org/docs/2.4/howto/auth.html
[bottle-home]: https://bottlepy.org
[mod_wsgi-docs]: https://modwsgi.readthedocs.io
