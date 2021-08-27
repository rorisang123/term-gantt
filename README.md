# term-gantt
## Description
This program displays a gantt chart onto terminal. Coded in Python.

## Example code
Download the module and import it into your python file. Use the template below to get started.
```python
import gantt

print(' '*10, 'MAKE GOOD LEMONADE TO SELL AT WEEKEND STAND\n')
tasks = ['Research', 'MakeRecipe', 'Make test batch', 'Get Feedback']
starts = [0, 2, 3, 5] #These are the start dates of each task
durations = [2, 2, 1, 1] #These are the durations of each task. Make sure they correspond to the order used in starts.

gantt.chart(tasks, starts, durations)
```

## Screenshot  
![Screenshot 1](https://github.com/rorisang123/term-gantt/blob/main/img/picture%202.JPG)
