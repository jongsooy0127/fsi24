"""
    Stopwatch -Features:
    - Persists between browser refreshes
    -Updates per second
    -Start/stop/reset
    -Stores all previous times just prior to reset
"""

from time import sleep
from flask import Flask, request, json, render_template

app = Flask(__name__)

# timelist = {"second": 30, "minute": 10, "hour": 0}

@app.post("/inputtimer")
def inputTimer():
    second = request.json.get("second")
    minute = request.json.get("minute")
    hour = request.json.get("hour")
    timer_dict = {"second": second, "minute": minute, "hour": hour}
    with open("time.json", "w", encoding="utf-8") as f:
        json.dump(timer_dict, f)
    return "Done"
    

@app.get("/")
def main():
    return render_template("stopwatch.html")

@app.get("/timerstart")
def startTimer():
    with open("time.json", "r", encoding="utf-8") as f:
        get_dict = json.load(f)
    seconds = int(get_dict["second"])
    minutes = int(get_dict["minute"])
    hours = int(get_dict["hour"])

    total_seconds = seconds + minutes*60 + hours*3600

    return str(total_seconds)

    # while total_seconds >= 0:
    #     sec = total_seconds % 60
    #     min = (total_seconds // 60) % 60    
    #     hour = total_seconds // 3600
    #     sleep(1)
    #     total_seconds -= 1
    #     timer = f"{hour:02}:{min:02}:{sec:02}"
    #     return str(total_seconds)
    
# total_seconds = 289
# while total_seconds >= 0:
#     sec = total_seconds % 60
#     min = (total_seconds // 60) % 60    
#     hour = total_seconds // 3600
#     sleep(1)
#     total_seconds -=1
#     print(f"{hour:02}:{min:02}:{sec:02}"   ) 