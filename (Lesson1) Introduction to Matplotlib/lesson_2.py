import matplotlib.pyplot as plt

# Example 1: Simple Line Plot (Mood Changes)
time_of_day = ['Morning', 'Noon', 'Afternoon', 'Evening', 'Night']
mood_level = [5, 8, 6, 7, 3]
plt.plot(time_of_day, mood_level, color='purple', marker='o')
plt.title('Mood Changes Throughout the Day')
plt.xlabel('Time of Day')
plt.ylabel('Mood Level')
plt.show()

# Example 2: Bar Graph (Favorite Snacks)
snacks = ['Chips', 'Candy', 'Cookies', 'Fruit']
likes = [10, 6, 8, 12]
plt.bar(snacks, likes, color='orange')
plt.title('Favorite Snacks')
plt.xlabel('Snacks')
plt.ylabel('Likes')
plt.show()

# Example 3: Scatter Plot (Sleep vs Test Scores)
sleep_hours = [6, 7, 8, 5, 9]
test_scores = [70, 80, 90, 60, 95]
plt.scatter(sleep_hours, test_scores, color='blue')
plt.title('Sleep vs Test Scores')
plt.xlabel('Hours of Sleep')
plt.ylabel('Test Scores')
plt.show()

