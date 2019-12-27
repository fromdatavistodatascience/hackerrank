sample_input = "07:05:45PM"


def timeConversion(s):
    "Function that converts 12-hour format into 24-hour format."
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    return str(ntime[:-2])


print(timeConversion(sample_input))
