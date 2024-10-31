
### lesson5_kids_playing_outside.py


import matplotlib.pyplot as plt

# Example data
months = ["January", "February", "March", "April", "May"]
kids_playing = [10, 12, 8, 15, 9]

# Adding Titles and Labels
plt.plot(months, kids_playing)
plt.title("Kids Playing Outside Each Month")
plt.xlabel("Month")
plt.ylabel("Number of Kids")
plt.show()

# Customizing Line Styles
plt.plot(months, kids_playing, linestyle='--', color='purple')  # Dashed purple line
plt.show()

# Adding Legends
plt.plot(months, kids_playing, label='Kids Playing Outside')
plt.legend()
plt.show()

# Challenge: Customize the plot
plt.plot(months, kids_playing, linestyle='-.', color='orange', label="Kids Playing")
plt.title("Outdoor Play Activity by Month")
plt.xlabel("Months")
plt.ylabel("Number of Kids Outside")
plt.legend()
plt.show()
