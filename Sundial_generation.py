import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def gen_sundial(latitude):

    rad_lat = np.radians(np.abs(latitude))

    angles = np.array([np.arctan(np.tan(np.radians(-90 + (3.75 * i))) * np.sin(rad_lat)) - (np.pi/2) for i in range(49)])
    angles2 = np.array([np.arctan(np.tan(np.radians(-90 + (3.75 * i))) * np.sin(rad_lat)) + (np.pi/2) for i in range(1, 13)])
    angles3 = np.array([-np.pi - (np.arctan(np.tan(np.radians(-90 + (3.75 * i))) * np.sin(rad_lat)) + (np.pi/2)) for i in range(1, 13)])

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw circles
    circle = plt.Circle((0, 0), 1, color='white', ec='black')
    ax.add_artist(circle)

    circle2 = plt.Circle((0, 0), 0.85, color='white', ec='black')
    ax.add_artist(circle2)

    #Draw the inner arc
    emp_ang = (360 - np.abs(np.degrees(angles3[11]))) - np.degrees(angles2[11])
    arc = Arc(xy=(0, 0), width=1.5, height=1.5, angle=np.degrees(angles2[11]), theta1=emp_ang, theta2=360, ec='black')
    ax.add_artist(arc)

    # Draw lines and labels
    for i, angle in enumerate(angles):
      if i % 4 == 0:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = 0, 0
      else:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = np.cos(angle) * 0.75, np.sin(angle) * 0.75

      # Draw line
      ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=0.5)

      # Draw hour numerals
      if i % 4 == 0:
        hours = ['VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'I', 'II', 'III', 'IV', 'V', 'VI']
        hours = list(reversed(hours))
        text_x = np.cos(angle) * 0.92
        text_y = np.sin(angle) * 0.92
        ax.text(text_x, text_y, hours[i // 4], color='black', ha='center', va='center')

    # Draw lines and labels
    for i, angle in enumerate(angles2):
      if (i + 1) % 4 == 0:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = 0, 0
      else:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = np.cos(angle) * 0.75, np.sin(angle) * 0.75

      # Draw line
      ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=0.5)

      # Draw hour numerals
      if (i + 1) % 4 == 0:
        hours = ['V', 'IV', 'III']
        text_x = np.cos(angle) * 0.92
        text_y = np.sin(angle) * 0.92
        ax.text(text_x, text_y, hours[(i - 3) // 4], color='black', ha='center', va='center')


    # Draw lines and labels
    for i, angle in enumerate(angles3):
      if (i + 1) % 4 == 0:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = 0, 0
      else:
        start_x, start_y = np.cos(angle) * 0.85, np.sin(angle) * 0.85
        end_x, end_y = np.cos(angle) * 0.75, np.sin(angle) * 0.75

      # Draw line
      ax.plot([start_x, end_x], [start_y, end_y], color='black', lw=0.5)

      # Draw hour numerals
      if (i + 1) % 4 == 0:
        hours = ['VII', 'VIII', 'IX']
        text_x = np.cos(angle) * 0.92
        text_y = np.sin(angle) * 0.92
        ax.text(text_x, text_y, hours[(i - 3) // 4], color='black', ha='center', va='center')

        # Set limits and aspect ratio
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_aspect('equal')

    # Hide axes
    #ax.axis('off')

    # Show plot
    plt.show()


latitude = 60
gen_sundial(latitude)