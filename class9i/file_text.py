with open("h:/Course/ReactDjangoPython/Practics/6/class9i/server.log") as file:
    for line in file:
        if "ERROR" in line:
            print(line.strip())