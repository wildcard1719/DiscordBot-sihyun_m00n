import time
def logging(file_name, content):
    with open(file_name, 'a') as f:
        tm = time.localtime()
        year = tm.tm_year
        mon = tm.tm_mon
        day = tm.tm_mday
        hour = tm.tm_hour
        minute = tm.tm_min
        sec = tm.tm_sec
        time_log = '[' + str(year) + '-' + str(mon) + '-' + str(day) + '-' + str(hour) + ':' + str(minute) + ':' + str(sec) + '] '
        f.write(time_log + content + '\n')
