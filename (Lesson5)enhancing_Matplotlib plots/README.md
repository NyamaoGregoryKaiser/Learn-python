# Lesson 5: Enhancing Your Matplotlib Plots

In this lesson, we focus on improving the clarity and visual appeal of Matplotlib plots by adding titles, labels, customizing line styles, and including legends.

## Topics Covered

1. **Adding Titles and Labels**
   - Add titles and labels to make graphs more informative.
   
2. **Customizing Line Styles**
   - Use different line styles and colors to make lines distinct.
   
3. **Adding Legends**
   - Legends clarify what each line or data set represents.

## Example Code

1. **Adding Titles and Labels**
   ```python
   plt.plot(months, books_read)
   plt.title("Books Read Per Month")
   plt.xlabel("Month")
   plt.ylabel("Number of Books")
   plt.show()
