def planet_data(planet_name):    
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    data = [[0.1, 88],[2.6, 225],[23.45, 365],[25.19, 687],[3.12, 4333],[26.73, 10759],[82.14, 30687],[29.56, 60190],[60.4, 90498]]
    for i in range(len(planets)):
        if planets[i] == planet_name:
            obl = data[i][0]
            per = data[i][1]

    return obl, per
