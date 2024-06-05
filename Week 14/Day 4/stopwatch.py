from flask import Flask
import time

app = Flask(__name__)

current_time = 0
elapsed_time = 0
running = False

@app.get("/starttime")
def starttime():
    global running, current_time
    if not running:
        running = True
        current_time = time.time()
    return str(elapsed_time)

@app.get("/stoptime")
def stoptime():
    global running, elapsed_time, current_time
    if running == True:
        running = False
        # elapsed_time += current_time - elapsed_time
        elapsed_time = current_time - elapsed_time
    
    return str(time.time() - elapsed_time)

@app.get("/elapsedtime")
def elapsedtime():
    global elapsed_time, current_time
    if running == True:
        return time.time() - elapsed_time
    else:
        return elapsed_time

@app.get("/resettime")
def resettime():
    global running, elapsed_time, current_time
    running = False
    elapsed_time = 0
    current_time = 0
    return "reset"

