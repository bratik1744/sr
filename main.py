from sirius import f

lst = [
    {"url": "https://edu.sirius.online/#/course/1289/12491/task_21339", "start": 213, "stop": 5000, "step": 1},
    {"url": "https://edu.sirius.online/#/course/1289/12491/task_21340", "start": 0, "stop": 50000, "step": 1}
]
for i in lst:
    f(i["url"], i["start"], i["stop"], i["step"])
