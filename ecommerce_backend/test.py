import math

def generate_coordinates(lat, lon, distance_km, num_points=2000):
    # Radius of the Earth in km
    R = 6371.0
    
    # Convert latitude and longitude from degrees to radians
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)
    
    # Generate coordinates
    coordinates = []
    for i in range(num_points):
        # Angle for this point
        angle = math.radians(360 / num_points * i)
        
        # Calculate new latitude and longitude using Haversine formula
        new_lat = math.asin(math.sin(lat_rad) * math.cos(distance_km / R) +
                            math.cos(lat_rad) * math.sin(distance_km / R) * math.cos(angle))
        
        new_lon = lon_rad + math.atan2(math.sin(angle) * math.sin(distance_km / R) * math.cos(lat_rad),
                                       math.cos(distance_km / R) - math.sin(lat_rad) * math.sin(new_lat))
        
        # Convert back to degrees
        new_lat_deg = math.degrees(new_lat)
        new_lon_deg = math.degrees(new_lon)
        
        coordinates.append((new_lat_deg, new_lon_deg))
    
    return coordinates

# Example usage
#23.88826, 90.39065
latitude = 23.88826  # Latitude of San Francisco
longitude = 90.39065  # Longitude of San Francisco
distance = 2  # 10 km radius

coords = generate_coordinates(latitude, longitude, distance)
for coord in coords:
    print(f"{coord[0]}, {coord[1]}")
