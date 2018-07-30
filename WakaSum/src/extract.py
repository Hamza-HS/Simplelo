import os
import re


def category(booleans, line):

    """Category switch when the for loop reach the category keyword"""

    if line == "Projects:\n":
        booleans["Projects"] = 1
    elif line == "Languages:\n":
        booleans["Languages"] = 1
    elif line == "Editors:\n":
        booleans["Editors"] = 1
    elif line == "Operating Systems:\n":
        booleans["Operating Systems"] = 1
    elif line == "\n":
        for key in booleans:
            booleans[key] = 0

    return booleans

def total_data(once, line, data):

    """ Collect all coding time """

    if once:
        if "hr" in line:
            mo = re.compile(r"(\d*)\shrs?\s(\d{1,2})\smins?").findall(line)
            if mo:
                data["Total"] += int(mo[0][0]) * 60 + int(mo[0][1])
                once = False
        elif "min" in line:
            mo = re.compile(r"(\d{1,2})\smins?").findall(line)
            if mo:
                data["Total"] += int(mo[0][0])
                once = False
    return once, data

def projects_data(booleans, line, data):

    """Collect projects names and their coding time"""

    if booleans["Projects"]:
        if "hr" in line:
            mo = re.compile(r"(.*)\s(\d*)\shrs?\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Projects"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
                except KeyError:
                    data["Projects"][mo[0][0]] = 0
                    data["Projects"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
        elif "min" in line:
            mo = re.compile(r"(.*)\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Projects"][mo[0][0]] += int(mo[0][1])
                except KeyError:
                    data["Projects"][mo[0][0]] = 0
                    data["Projects"][mo[0][0]] += int(mo[0][1])

    return data

def languages_data(booleans, line, data):

    """Collect programming languages that are used and coding time with them"""

    if booleans["Languages"]:
        if "hr" in line:
            mo = re.compile(r"(.*)\s(\d*)\shrs?\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Languages"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
                except KeyError:
                    data["Languages"][mo[0][0]] = 0
                    data["Languages"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
        elif "min" in line:
            mo = re.compile(r"(.*)\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Languages"][mo[0][0]] += int(mo[0][1])
                except KeyError:
                    data["Languages"][mo[0][0]] = 0
                    data["Languages"][mo[0][0]] += int(mo[0][1])
                    
    return data

def editors_data(booleans, line, data):

    """Collect the IDE or Editors that are used and the coding time"""

    if booleans["Editors"]:
        if "hr" in line:
            mo = re.compile(r"(.*)\s(\d*)\shrs?\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Editors"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
                except KeyError:
                    data["Editors"][mo[0][0]] = 0
                    data["Editors"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
        elif "min" in line:
            mo = re.compile(r"(.*)\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Editors"][mo[0][0]] += int(mo[0][1])
                except KeyError:
                    data["Editors"][mo[0][0]] = 0
                    data["Editors"][mo[0][0]] += int(mo[0][1])

    return data

def os_data(booleans, line, data):

    """Collect operating systems that are used and the coding time with them"""

    if booleans["Operating Systems"]:
        if "hr" in line:
            mo = re.compile(r"(.*)\s(\d*)\shrs?\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Operating Systems"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])
                except KeyError:
                    data["Operating Systems"][mo[0][0]] = 0
                    data["Operating Systems"][mo[0][0]] += int(mo[0][1]) * 60 + int(mo[0][2])             
        elif "min" in line:
            mo = re.compile(r"(.*)\s(\d{1,2})\smins?").findall(line)
            if mo:
                try:
                    data["Operating Systems"][mo[0][0]] += int(mo[0][1])
                except KeyError:
                    data["Operating Systems"][mo[0][0]] = 0
                    data["Operating Systems"][mo[0][0]] += int(mo[0][1])

    return data

def all_data(path):

    """Collecting all data from all text files in given path"""

    all_files = [path + "/" + file for file in os.listdir(path) if file.endswith(".txt")]
    booleans = {"Projects": 0, "Languages": 0, "Editors": 0, "Operating Systems": 0}
    data = {"Total": 0, "Projects": {}, \
            "Languages": {}, "Editors": {}, \
            "Operating Systems": {}}
    data_funcs = [projects_data, languages_data, editors_data, os_data]
    cur_file = 0
    once = True

    for file in all_files:
        cur_file = open(file, "r")
        once = True
        for line in cur_file.readlines():
            once, data = total_data(once, line, data)
            booleans = category(booleans, line)
            for func in data_funcs:
                data = func(booleans, line, data)
        cur_file.close()

    return data