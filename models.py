from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Area(db.Model):

  __tablename__ = 'Area'

  id = db.Column(db.Integer, primary_key=True)
  city = db.Column(db.String(120))
  state = db.Column(db.String(120))
  venues = db.relationship('Venue', backref='area')

  def __init__(self, city, state):
      self.city = city
      self.state = state

class Venue(db.Model):

    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    area_id = db.Column(db.Integer, db.ForeignKey('Area.id'))
    shows = db.relationship('Show', backref='venue')

    def __init__(self, name, image_link, facebook_link, area_id):
       self.name = name
       self.image_link = image_link
       self.facebook_link = facebook_link
       self.area_id = area_id

class Artist(db.Model):

    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artist')

    def __init__(self, name, image_link, facebook_link):
      self.name = name
      self.image_link = image_link
      self.facebook_link = facebook_link

class Show(db.Model):

  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime)
  artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))

  def __init__(self, artist, venue, start_time):
     self.artist_id = artist
     self.venue_id = venue
     self.start_time = start_time