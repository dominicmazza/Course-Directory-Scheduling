# -*- coding: utf-8 -*-
"""
AI Final Project
Constraint Satisfaction Class Scheduling
"""
___author = 'Dominic Mazza'


import random

#------FUNCTIONS--------------------------------------------------------------
#create_schedule makes a schedule for one room. This room is returned
#so that the main can add it to the collective schedule
def create_room_schedule(rooms, courses, times, teachers, i):
    avail_slots = {}
    room = rooms[i]
    coursescopy = courses.copy()
    time_slots = {}
    for time in times:
        if len(coursescopy) > 0:
            rand_course = random.choice(courses)
            rand_teacher = random.choice(teachers)
            rand_picks = []
            rand_picks.append(rand_course)
            rand_picks.append(rand_teacher)
            time_slots[time] = rand_picks
    avail_slots[room] = time_slots
    return avail_slots

#calc_conflicts utilizes the corequisite and time conflict functions
#to calculate the total number of conflictsp
def calc_conflicts(avail_slots, i, rooms):
    conflicts = 0
    conflicts += cofl_coreq(avail_slots, coreqs, times, rooms)
    conflicts += conf_times(avail_slots, times)
    if len(rooms) == len(avail_slots):
        conflicts += all_courses(avail_slots, rooms, courses)
    return conflicts    

#cofl_coreq finds the number of conflicts that result from the
#current schedule by checking if there are corequisite classes
#being taught at the same time
def cofl_coreq(avail_slots, coreqs, times, rooms):
    conflicts = 0
    for time in times:
        courses = []
        for room in avail_slots:
            times = avail_slots[room]
            for t in times:
                if t == time:
                    pair = times[time]
                    courses.append(pair[0])
        for pair in coreqs:
            count = 0
            for coreq in pair:
                if coreq in courses:
                    count += 1
            if count > 1:
                conflicts += 1
    return conflicts

#cofl_times checks if there is a teacher scheduled to teach two classes
#at the same time, if so 1 is added to conflicts
def conf_times(avail_slots, times):
    conflicts = 0
    for time in times:
        teach_at_time = []
        for room in avail_slots:
            times = avail_slots[room]
            for key in times:
                pair = times[key]
                teacher = pair[1]
                if key == time:
                    teach_at_time.append(teacher)
        for teach in teach_at_time:
            if teach_at_time.count(teach) > 1:
                conflicts += 1
                teach_at_time = [i for i in teachers if i != teach]
    return conflicts                     

def all_courses(avial_clots, rooms, courses):
    scheduled_courses = []
    coursescopy = courses.copy()
    for slot in avail_slots.values():
        for pair in slot.values():
            scheduled_courses.append(pair[0])
    for course in scheduled_courses:
        if course in coursescopy:
            coursescopy.remove(course)
    conflicts = len(coursescopy)
    return conflicts

#c_t_pairing_matrix creates pairs of courses and teachers which are used
#as text for each of the cells in my graphic table
def c_t_pairing_matrix(avail_slots, rooms):
    pair_matrix = []
    for slot in avail_slots.values():
        pair_row = []
        for pair in slot.values():
            pairstring = ""
            pairstring += str(pair[0]) + " " + "with "
            pairstring += str(pair[1])
            pair_row.append(pairstring)
        pair_matrix.append(pair_row)
    return pair_matrix 

#show_table this function creates the graphic at the end of the
#program
#https://www.pythonpool.com/matplotlib-table/#Implementation_of_Matplotlib_table
#Library implemented from pythonpool.com
def show_table(roomscopy, courses, times, teachers, pairs):
    import matplotlib.pyplot as plt 
    fig, ax = plt.subplots() 
    ax.set_axis_off() 
    for i in range(len(rooms)):
        rooms[i] = "Room " + str(rooms[i])
    table = ax.table( 
        cellText = pairs,  
        rowLabels = rooms,
        colLabels = times, 
        rowColours =["lightblue"] * 15,  
        colColours =["lightblue"] * 15, 
        cellLoc ='center',  
        loc ='upper left')    
    ax.set_title('Class Schedule', 
                 fontweight ="heavy") 
    plt.rcParams['figure.dpi'] = 1200
    plt.show()
#-----------------------------------------------------------------------------

#------USER INPUTS------------------------------------------------------------
#Example Inputs

#rooms = 5
#courses = "Org & Arch, Advanced Algorithms, Database Systems, AI, Robotics, Machine Learning, Mobile App Development"
#times = "9:30am, 12:30pm, 2pm"
#teachers = "Joel, Shannon, Duke, Elizabeth, Ryan"
#coreqs = "Robotics Machine Learning"


rooms = input("Please enter the number of rooms avaliable.\nMust be equal or less rooms than teachers\n")
numrooms = int(rooms)
rooms = []
for i in range(numrooms):
    rooms.append(i+1)
    
courses = input("Please enter the courses you would like to schedule seperated by a comma and space.\n")
courses = courses.split(", ")

times = input("Please enter a list of times seperated by a comma and space.\n")
times = times.split(", ")

        
teachers = input("Please enter teacher names seperated by a comma.\n")
teachers = teachers.split(", ")
        
coreqs = input("Please enter classes that are co-requisites in pairs seperated by commas, or enter None.\nex. Writing Literature, Algebra Geometry\n")
if "None" in coreqs:
    pairs = coreqs.split(",")
    coreqs = []
    for pair in pairs:
        pair = pair.strip()
        coreq = pair.split()
        coreqs.append(coreq)
#-----------------------------------------------------------------------------
    
#------MAIN-------------------------------------------------------------------
conflicts = 5
i = len(rooms) - 1
avail_slots = create_room_schedule(rooms, courses, times, teachers, i)
cost = 0
while conflicts != 0 or i != -1:
    avail_slots.update(create_room_schedule(rooms, courses, times, teachers, i))
    conflicts = calc_conflicts(avail_slots, i, rooms)
    if conflicts == 0:
        i -= 1
    cost += 1

schedule = {}
for k,v in reversed(list(avail_slots.items())):
    schedule[k] = v
pairs = c_t_pairing_matrix(schedule, rooms)
show_table(rooms, courses, times, teachers, pairs)


print(schedule)
print("\nCost:", cost)




    
