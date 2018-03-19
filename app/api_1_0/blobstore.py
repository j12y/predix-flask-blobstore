
from flask import jsonify
from flask.globals import request
from werkzeug.utils import secure_filename

import predix.data.blobstore

from . import api

blobstore = predix.data.blobstore.BlobStore()

@api.route('/buckets')
def buckets(bucket_name):
    objs = blobstore.list_buckets()
    return jsonify(objs)

@api.route('/list')
def list():
    objs = blobstore.list_objects()
    return jsonify(objs)

@api.route('/list/<bucket_name>')
def list_bucket(bucket_name):
    objs = blobstore.list_objects(bucket_name=bucket_name)
    return jsonify(objs)

@app.route('/store', methods=['POST'])
def store():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    src_filepath = '/tmp/' + filename
    uploaded_file.save(src_filepath)

    blobstore.upload_file(src_filepath, filename)
