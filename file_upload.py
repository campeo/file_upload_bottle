#!/usr/bin/env python

"""A very simple upload server

This is a simple upload server using the Bottle micro framework. It can either
be run directly with Python:

    python file_upload.py

Or run behind a web server such as Apache with configuration similar to the
following:

    <IfModule !wsgi_module>
    LoadModule wsgi_module modules/mod_wsgi.so
    </IfModule>

    WSGIScriptAlias /upload /var/www/file_upload/file_upload.py

"""

import os
import bottle

def do_index():
    """List all uploaded files"""
    root = '%s/' % bottle.request.environ.get('SCRIPT_NAME')
    return bottle.template('index.html', files=os.listdir(app.config['file_upload.dir']), root=root)

def do_download(filename):
    """Return a static file from the files directory"""
    return bottle.static_file(filename, root=app.config['file_upload.dir'])

def do_upload():
    """Upload a file if it's missing"""
    upload = bottle.request.files.get('upload') # pylint: disable-msg=E1101
    try:
        upload.save(app.config['file_upload.dir'])
    except IOError as io_error:
        return bottle.HTTPError(409, io_error)

    root = '%s/' % bottle.request.environ.get('SCRIPT_NAME')
    bottle.redirect(root)

def create_files_dir(path):
    """Create a directory to upload files to if it's missing."""
    if not os.path.isdir(path):
        os.mkdir(path)

bottle.route('/', 'GET', do_index)
bottle.route('/download/<filename>', 'GET', do_download)
bottle.route('/upload', 'POST', do_upload)

# Change working directory so relative paths (and template lookup) work
os.chdir(os.path.dirname(os.path.abspath(__file__)))

app = bottle.default_app() # pylint: disable-msg=C0103
app.config.setdefault('file_upload.dir', 'files')

if os.path.exists('file_upload.conf'):
    app.config.load_config('file_upload.conf')

create_files_dir(app.config['file_upload.dir'])

if __name__ == '__main__':
    bottle.run(app, host='0.0.0.0', port=8080)
else:
    # Run using separate WSGI application server
    application = app # pylint: disable-msg=C0103
