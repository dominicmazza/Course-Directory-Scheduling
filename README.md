# Course-Directory-Scheduling
AI program that creates a course directory for a school or institute given rooms, titles, times, teachers, and corequisites. By using backtracking search, I apprached the scheduling as if it were a constraint satisfaction problem. The program creates this schedule such that no corequisites are being taught simultaneously, no teachers are teaching two different courses simultaneously, and every class inputted must be scheduled.

Instructions:
Enter some inputs to generate the schedule: room, courses, times, teachers, and corequisites. The number of rooms must be less than the number of teachers inputted in the list form.

Here are some example inputs:

rooms = 5

courses = "Org & Arch, Advanced Algorithms, Database Systems, AI, Robotics, Machine Learning, Mobile App Development"

times = "9:30am, 12:30pm, 2pm"

teachers = "Joel, Shannon, Duke, Elizabeth, Ryan"

coreqs = "Robotics Machine Learning"

Here is what was created:

{1: {'9:30am': ['Database Systems', 'Shannon'], '12:30pm': ['Mobile App Development', 'Joel'], '2pm': ['Advanced Algorithms', 'Shannon']}, 2: {'9:30am': ['AI', 'Joel'], '12:30pm': ['Org & Arch', 'Duke'], '2pm': ['Advanced Algorithms', 'Joel']}, 3: {'9:30am': ['Org & Arch', 'Ryan'], '12:30pm': ['AI', 'Shannon'], '2pm': ['Machine Learning', 'Elizabeth']}, 4: {'9:30am': ['AI', 'Duke'], '12:30pm': ['Robotics', 'Ryan'], '2pm': ['Machine Learning', 'Duke']}, 5: {'9:30am': ['Mobile App Development', 'Elizabeth'], '12:30pm': ['Robotics', 'Elizabeth'], '2pm': ['Advanced Algorithms', 'Ryan']}}

Why:
My AI solves the problem of mainly writing out and planning a class directory. It makes the process much easier and more time efficient.
I implemented a table plotting library from pythonpool.com which created the graphic for my table. https://www.pythonpool.com/matplotlib-table/#Implementation_of_Matplotlib_table


