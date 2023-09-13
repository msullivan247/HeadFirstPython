import math
import statistics

FOLDER = 'swimdata/'

def read_swim_data(filename):
    name, ageGroup, distance, stroke = filename.removesuffix(".txt").split("-")
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times_strings = lines[0].strip().split(",")
        times = [get_seconds(time) for time in times_strings]
        average_time = statistics.mean(times)
        return name, ageGroup, distance, stroke, times_strings, format_swim_time(average_time)
        # print(f"Swimmer: {name}\nAge Group: {ageGroup}\nDistance: {distance}\nStroke: {stroke}\nTimes: {timesStrings}\nAverage Time: {format_swim_time(averageTime)}")

def get_seconds(time_string):
    if ":" in time_string:
        minutes, seconds = time_string.split(":")
        return int(minutes) * 60 + float(seconds)
    else:
        return float(time_string)
    

def format_swim_time(total_seconds):
    minutes = math.floor(total_seconds / 60)
    seconds = total_seconds % 60
    return ("%d:%.2f" % (minutes, seconds))