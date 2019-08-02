# Dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from datetime import datetime
import datetime as dt
 
#Create an app, being sure to pass_name__
app = Flask(__name__)

# Database Setup
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Assign the classes to respective tables
Measurements = Base.classes.measurements
Stations = Base.classes.stations

# Create session
session = Session(engine)

  
@app.route("/")
def home():
    print("Server received request for 'Home' page.")
    """Listing of the available API routes"""
    return (
        f"Welcome to the Surf Up API<br>"
        f"Available Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0<start>/<end><br>"
    )"

  
@app.route("/api/v1.0/precipitation")
def precipitation():
   
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= "08-23-2017").all()

    last_year_prcp = list(np.ravel(results))
    
    #results.___dict___
    # Convert the query results from last year to a Dictionary using `date` as the key and `prcp` as the value 
    """"last_year_prcp = []
    for result in results:
        prcp_dict = {}
        prcp_dict[Measurement.date] = prcp_dict[Measurement.prcp]
        last_year_prcp.append(prcp_dict)""""

    return jsonify(last_year_prcp)"

  
@app.route("/api/v1.0/stations")
def stations():
    
    # Return a json list of stations from the dataset.

    station_results = session.query(Station.station).all()
    
    # Convert the list of tuples into a normal list:
    all_stations = list(np.ravel(station_results))

    return jsonify(all_stations)"

  
@app.route("/api/v1.0/tobs")
def temperature():
    
    #Return a json list of Temperature Observations (tobs) for the previous year
    
    last_year_tobs = []
    
    temp_results = session.query(Measurement.tobs).filter(Measurement.date >= "08-23-2017").all()

    last_year_tobs = list(np.ravel(temp_results))

    return jsonify(last_year_tobs)"

  
@app.route("/api/v1.0/<start>")
def start_trip_temp(start_date):
    
    #Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

    start_trip = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date == start_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date == start_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date == start_date).all()

    start_trip = list(np.ravel(results_min, results_max, results_avg))

    return jsonify(start_trip)

def greater_start_date(start_date):

    start_trip_date_temps = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()

    start_trip_date_temps = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(start_trip_date_temps)"

  
@app.route("/api/v1.0/<start>/<end>")

def start_end_trip(start_date, end_date):

    start_end_trip_temps = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date == start_date, Measurement.date == end_date).all()

    start_end_trip_temps = list(np.ravel(results_min,results_max, results_avg))

    return jsonify(start_end_trip_temps)

def start_end_trip(start_date, end_date):

    round_trip_temps = []

    results_min = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()
    results_max = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()
    results_avg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start_date, Measurement.date >= end_date).all()

    round_trip_temps = list(np.ravel(results_min,results_max, results_avg))

return jsonify(round_trip_temps)


if __name__ == '__main__':
    app.run(debug=True)"
