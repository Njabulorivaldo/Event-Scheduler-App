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
    #2024-04-03

    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')       #pattern
    if bool(date_pattern.match(date)):
        if ((int(date[0:4]) < 2024) or (int(date[5:7]) > 12) or (int(date[5:7]) < 1) or (int(date[8:11]) > 31) or (int(date[8:11]) < 1)):
            return False 
        return True 
    
    return False

def validate_time(time):
    #Regex pattern for time in HH:MM format
    #00:00

    time_pattern = re.compile(r'^\d{2}:\d{2}$')     #pattern
    if bool(time_pattern.match(time)):
        if ((int(time[0:2]) > 24) or (int(time[0:2]) < 0) or (int(time[3:5]) > 59) or (int(time[3:5]) < 0)):
            return False
        return True
    
    return False

def showEvents(events_lst):

    print("")
    print("{:<15} | {:<30} | {:<15} | {:<10}".format("Title", "Description", "Date", "Time"))
    print("-" * 80) 

    if not events_lst:
        print("{:^80}".format("No events..."))

    for event in events_lst:
        event.display_info()
    print()

def sort():
    #sort events by date and time
    events.sort(key=lambda event: (event.date, event.time))
    
def deleteEvent(title):
    global events

    original_count = len(events)
    events = [event for event in events if event.title != title]
    count = original_count - len(events)
   
    if count == 0:
        print("\033[91mEvent does not exist....\033[0m \n")
        return

    print(count, " \033[92mEvent(s) successfully deleted.....\033[0m \n")

def search_withDate(date):
    
    events_with_date = []
    for event in events:
        if event.date == date:
            events_with_date.append(event)

    showEvents(events_with_date)

def search_with_keyword(word):

    events_with_keyword = []

    for event in events:
        if (word.lower() in event.title.lower()) or (word.lower() in event.description.lower()):
            events_with_keyword.append(event)

    showEvents(events_with_keyword)


def main():
    print("\033[35m" + "\033[1m" + "========== Event Scheduler ==========" + "\033[0m")

    while True:
        print("1. Add an event.")
        print("2. Show events. ")
        print("3. Delete event")
        print("4. Search")

        try:
            opt = eval(input(" > "))

            if opt == 1:
                addEvent()
            
            if opt == 2:
                
                sort()
                showEvents(events)

            if opt == 3:
                title = input("Event title to delete or 0 to cancel: ")
                if title == '0':
                    pass
                else:
                    deleteEvent(title)

            if opt == 4:
                print("Search using: \n 1. Date \n 2. Keyword \n Or 0 to cancel")
                sel = input(">> ")

                if sel == '0':
                    pass

                elif sel == '1':
                    date = input("Enter the date: ")
                    search_withDate(date)

                elif sel == '2':
                    keyword = input("Enter keyword: ")
                    search_with_keyword(keyword)


        except Exception as e:
            print("Enter only the number option. \n", e)


if __name__ == "__main__":
    main()