"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, flash, send_from_directory
import os
from .models import MovieProfile
from app.forms import MovieForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf



###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")




###
# The functions below should be applicable to all Flask apps.
###

@app.route("/api/v1/movies", methods=['POST'])
def movie_post():
    
    if request.method == "POST":
        form = MovieForm()
        if form.validate_on_submit():
            fileobj = request.files['poster']
            sanitizedname = secure_filename(fileobj.filename)
            if fileobj and (sanitizedname != "" and sanitizedname != " "):
                fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], sanitizedname))
                title = form.title.data
                description = form.description.data
                new_movie = MovieProfile(title,description,fileobj)
                db.session.add(new_movie)
                db.session.commit()
                feedback= {
                    "message": "Movie Successfully added",
                    "title": form.title.data,
                    "poster": form.poster.data,
                    "description": form.description.data
                }
                return jsonify(feedback)
        return jsonify(form_errors(form))
    return jsonify({'message': 'This is a problem'})
    
    form = MovieForm()
    if form.validate_on_submit():
        poster = form.poster.data
        filename = secure_filename(poster.filename)
        poster.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        title = form.title.data
        description = form.description.data
        new_movie = MovieProfile(title,description,filename)
        db.session.add(new_movie)
        db.session.commit()
        flash('Movie successfully added', 'success')
    form_errors(form)
    return jsonify(data=new_movie.serialize())
    
    

@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
 return jsonify({'csrf_token': generate_csrf()})

@app.route("/api/v1/images/<path:filename>")
def getImage(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404