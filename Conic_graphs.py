import matplotlib.pyplot as plt
import numpy as np

# This function graphs the general equation for the sundial shadow path
def graph_conic(lat, days, height):

  x = np.linspace(-1, 1, 5000)
  y = np.linspace(-1, 1, 5000)
  x, y = np.meshgrid(x, y)

  obl = 23.45
  rad_lat = np.radians(lat)
  dec = np.radians(obl * np.sin((0.0172 * (284 + days))))
  print(dec)
  a = (np.sin(rad_lat) ** 2) * (np.tan(dec) ** 2)

  fig, ax = plt.subplots()
  if dec >= rad_lat - np.pi/2:
    if dec > -0.003 and dec < 0.003:
      eq = height * np.tan(rad_lat)
      ax.hlines(eq, -20, 20)
    else:
      ax.contour(x, y, a * (x**2 + y**2) - (y * np.cos(rad_lat) - height * np.sin(rad_lat)) ** 2, [0])


  ax.set_aspect('equal')
  ax.set_xlabel('x coordinates')
  ax.set_ylabel('y coordinates')
  ax.set_title('The sunpath conic section')
  plt.show()


#This function solves the problem of hyperbola branches.
def graph_right_hyp(lat, days, height):

  rad_lat = np.radians(lat)
  obl = 23.45
  dec = np.radians(obl * np.sin((0.0172 * (284 + days))))
  fig, ax = plt.subplots()

  t = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
  A = np.sin(rad_lat)**2 * np.tan(dec)**2
  C = np.cos(rad_lat)**2 - np.sin(rad_lat)**2 * np.tan(dec)**2
  E = height * np.cos(rad_lat) * np.sin(rad_lat)
  F = - (height**2) * np.sin(rad_lat)**2



  if dec  == 0:
    eq = height * np.tan(rad_lat)
    ax.hlines(eq, -20, 20)
  else:
    if dec > 0:
      xval = np.sqrt((E**2 + F * C) / (A * C)) * np.sinh(t)
      yval = - np.sqrt((E**2 + F * C) / (C**2)) * np.cosh(t) + E/C
    else:
      xval = np.sqrt((E**2 + F * C) / (A * C)) * np.sinh(t)
      yval = np.sqrt((E**2 + F * C) / (C**2)) * np.cosh(t) + E/C
    ax.plot(xval, yval)



  ax.set_aspect('equal')
  ax.set_xlim(-1, 1)
  ax.set_ylim(-1, 1)
  ax.set_title('The right-side of the Hyperbola')
  plt.show()

graph_right_hyp(60, 263.95, 0.1)