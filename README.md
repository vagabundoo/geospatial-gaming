# geospatial-gaming
This project is an exercise in exploiting geospatial data. The goal was to find a location that meets a list of geospatial criteria using a variety of tools.  
The assignment description can be found in *input/Geospartial-Project-description.md*

## Project goal
The idea was to find a location for a new gaming company, that met the following criteria: 
- The location needs to be close to gaming or design companies for inspiration for the employees 🎮
- Developers like to be near successful tech startups that have raised at least 1 Million dollars. 💰
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far. ☕
- 30% of the company have at least 1 child: location needs to be close to childcare facilities 🧒

## Output
The final list of locations, along with a visualization can be found in **presentation.ipynb** 🗺️

You can follow workflow during the project in the **workflow** folder, with jupyter notebooks with comments and annotations.

## Tools used
- **MongoDB** and **PyMongo** package to work with the [crunchbase database](crunchbase.com) of innovative companies 
- **Pandas** dataframes and **Geopandas** dataframes for working with geolocation data.
- **Cartoframes** and **Folium** for visualization on maps
- The [FourSquare API](https://foursquare.com/developers/) for geolocating bussinesses, and the **Requests** python package.


