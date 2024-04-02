from Event import Event
import re


events = []     #List of saved events

def addEvent():

    title = input("Enter the event title: ")
    descr = input("Description: ")

    while True:
        date = input("Date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        print("\033[91mInvalid date....\033[0m")
        print("Use the YYYY-MM-DD format\n")
    
    while True:
        time = input("Time (HH:MM): ")
        if validate_time(time):
            break
        print("\033[91mInvalid time....\033[0m")
        print("Use the HH:MM format \n")

    events.append(Event(title, descr, date, time))

    print("\033[92mEvent successfully added.....\033[0m \n")



def validate_date(date):
    # Regex pattern for date in YYYY-MM-DD format

    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return bool(date_pattern.match(date))

def validate_time(time):
    #Regex pattern for time in HH:MM format

    time_pattern = re.compile(r'^\d{2}:\d{2}$')
    return bool(time_pattern.match(time))



def main():
    print("\033[35m" + "\033[1m" + "========== Event Scheduler ==========" + "\033[0m")

    while True:
        print("1. Add an event.")

        try:
            opt = eval(input(" > "))

            if opt == 1:
                addEvent()
        
        except Exception as e:
            print("Enter only the number option. \n", e)

main()
#print(validate_date("1"))