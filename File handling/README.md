# Lesson 6: Creating a Mini-Diary App with Python

In this lesson, we learn how to create a simple diary application using Python's file handling capabilities. The app allows users to write entries with timestamps and read back past entries.

## Topics Covered

1. **Understanding File Handling**
   - The importance of file handling for saving data persistently.

2. **Types of File Operations**
   - Reading: Open and read data from a file.
   - Writing: Add new data or overwrite existing data in a file.

3. **Building the Mini-Diary App**
   - Write new diary entries with timestamps.
   - Read past entries from the diary file.

## Example Code

1. **Writing to a File**
   ```python
   with open("diary.txt", "a") as file:
       file.write("Your text here\n")

