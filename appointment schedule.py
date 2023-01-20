#list of appointments
appointmentList = []

#function for date input
def input_date():
    date = input("Please enter the date of your new appointment, eg - 25/9/2023: ")
    return date

#function for start time input
def input_start_time():
    start_time = input("Please enter the start time of your new appointment, eg - 11: ")
    return start_time

#function for end time input
def input_end_time():
    end_time = input("Please enter the end time of your new appointment e.g - 12: ")
    return end_time

#function for subject input
def input_subject():
    subject = input("Please enter the subject of your new appointment: ")
    return subject

#function for venue input
def input_venue():
    venue = input("Please enter the venue of your new appointment: ")
    return venue

#function for priority
def input_priority():
    priority = input("Please enter the priority of your new appointment, eg - high, medium, or low: ")
    return priority

#function for validation of date
def isValidDate(date):
    try:
        day, month, year = date.split("/")
        day, month, year = int(day), int(month), int(year)
        #if statement for year greater than 999 and less than 2024 and 12 months
        if year < 2024 and year > 999 and month >= 1 and month <= 12:
            daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
            if month == 2:
                if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                    daysInMonth[1] = 29
            if day >= 1 and day <= daysInMonth[month-1]:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False

#function for validation of time
def isValidTime(hour):
    try:
        hour = int(hour)
        #time is considered between 8 and 18 only
        if hour >=8 and hour <=18:
            return True
    except ValueError:
        return False

#function for the validation of concurrent appointment in the same date
def isConcurrentAppointment(appointment, appointmentList):
    for existingAppointment in appointmentList:
        #taking index position for the time in the appointment
        existingStartTime, existingEndTime = existingAppointment[1], existingAppointment[2]
        newStartTime, newEndTime = appointment[1], appointment[2]
        existingDate, newDate = existingAppointment[0], appointment[0]
        if existingDate == newDate:
            #if statement for the concurrent appointment
            if (newStartTime > existingStartTime) and (newStartTime < existingEndTime):
                #Error!!! Appointment is concurrent with an existing appointment
                return True
            elif (newEndTime > existingStartTime) and (newEndTime < existingEndTime):
                #Error!!! Appointment is concurrent with an existing appointment.
                return True
            elif (newStartTime < existingStartTime) and (newEndTime > existingEndTime):
                #Error!!!! Appointment is concurrent with an existing appointment.
                return True
            elif ((newStartTime >= existingEndTime) and (newEndTime >= existingEndTime)) or ((newStartTime <= existingStartTime) and (newEndTime <= existingStartTime)):
                return False
    #Appointment is not concurrent with any existing appointments and appends to the existing ones
    return False

#function to add the appointments records
def addRecord():
    while True:
        # Collect data for appointment records
        date = input_date()
        start_time = input_start_time()
        end_time = input_end_time()
        subject = input_subject()
        venue = input_venue()
        priority = input_priority()
        #record = f"{date}, {start_time}, {end_time}, {subject}, {venue}, {priority}"
        #display the list of appointments if date = END
        if date == "END":
            showRecords(appointmentList)
            break
        # Validate date using isValidDate() function
        if not isValidDate(date):
            print("Error: Invalid date format. Please enter a date in the format 'dd/mm/yyyy'.")
            continue
        # Validate time using isValidTime() function
        if not isValidTime(start_time) or not isValidTime(end_time):
            print("Error: Invalid time format. Please enter a time in the format 'hh' and between 8-18.")
            continue
        elif int(start_time) >= int(end_time) :
            print("Invalid Input", "Start time should be less than end time")
            continue
        # Validate subject and venue strings
        if len(subject) == 0 or len(subject) > 25 or len(venue) == 0 or len(venue) > 25:
            print("Error: Invalid subject or venue. Please enter a non-empty string within 25 characters.")
            continue
        #validate the concurrent appointment
        appointment = [date, start_time, end_time, subject, venue, priority]
        if not isConcurrentAppointment(appointment, appointmentList):
            #append the list
            appointmentList.append(appointment)
            print("Appointment added!!!")
        else:
            print("ERROR!!!!!!!")
        # Validate priority
        if priority.upper() not in ["LOW", "MEDIUM", "HIGH"]:
            print("Error: Invalid priority. Please enter either 'Low', 'Medium', or 'High'.")
            continue

#function to display the appointment list recorded
def showRecords(appointmentList):
    headers = ["Date", "Start Time", "End Time", "Subject", "Venue", "Priority"]
    #determine the max length in header
    maxLengths = [len(header) for header in headers]

    # Find the maximum length for each column
    for appointment in appointmentList:
        for i, value in enumerate(appointment):
            maxLengths[i] = max(maxLengths[i], len(str(value)))

    # Print the headers
    for i, header in enumerate(headers):
        print(header.ljust(maxLengths[i]), end=" | ")
    print()

    # Print the separator line
    for length in maxLengths:
        print("-" * length, end="-+-")
    print()

    # Print the records
    for appointment in appointmentList:
        for i, value in enumerate(appointment):
            print(str(value).ljust(maxLengths[i]), end=" | ")
        print()

#function to search the element and display the searched record
def searchRecord(appointmentList):
    while True:
        # Collect search keywords
        keyword = input("Please enter the keyword for searching (or 'END' to stop): ").lower()
        #if keyword is end stop searching
        if keyword == "end":
            break
        foundRecords = []
        for appointment in appointmentList:
            for value in appointment:
                if keyword in str(value).lower():
                    foundRecords.append(appointment)
                    break
        #to get the searched record
        if len(foundRecords) > 0:
            foundRecords.sort(key=lambda x: x[0])
            headers = ["Date", "Start Time", "End Time", "Subject", "Venue", "Priority"]
            maxLengths = [len(header) for header in headers]
            for appointment in foundRecords:
                for i, value in enumerate(appointment):
                    maxLengths[i] = max(maxLengths[i], len(str(value)))
            # Print the headers
            for i, header in enumerate(headers):
                print(header.ljust(maxLengths[i]), end=" | ")
            print()
            # Print the separator line
            for length in maxLengths:
                print("-" * length, end="-+-")
            print()
            # Print the found records
            for appointment in foundRecords:
                for i, value in enumerate(appointment):
                    print(str(value).ljust(maxLengths[i]), end=" | ")
                print()
        else:
            print("No records found!!!")

#function to tally the appointments based on the priority
def tallyAppointments(appointmentList):
    while True:
        user_input = input("Do you want to tally the appointments by priority (YES/NO)? ").lower()
        if user_input == "yes":
            high_count = 0
            medium_count = 0
            low_count = 0
            #calculate count
            for appointment in appointmentList:
                if appointment[5].lower() == "high":
                    high_count += 1
                elif appointment[5].lower() == "medium":
                    medium_count += 1
                elif appointment[5].lower() == "low":
                    low_count += 1
            print("Summary by priority:")
            headers = ["Priority", "Count"]
            #generate the table format
            maxLengths = [len(header) for header in headers]
            for i, header in enumerate(headers):
                print(header.ljust(maxLengths[i]), end=" | ")
            print()
            for length in maxLengths:
                print("-" * length, end="-+-")
            print()
            rows = [["High", high_count], ["Medium", medium_count], ["Low", low_count]]
            for row in rows:
                for i, value in enumerate(row):
                    print(str(value).ljust(maxLengths[i]), end=" | ")
                print()
            break
        #stop displaying the tally appointments
        elif user_input == "no":
            break
        else:
            print("Invalid input. Please enter 'YES' or 'NO'.")

#main function
def main():
    choice = 0
    #while loop for menu options
    while True:
        print("\nAppointment Scheduler \n")
        print("1. Add records to the appointment. \n2. Search in the appointment list. \n3. Tally appointments. \n4. Exit")
        choice = int(input("Enter your choice: "))
        #call the function addRecord() to add data in the appointment list
        if choice == 1:
            addRecord()
        #call searchRecord() to search the element in the appointment
        elif choice == 2:
            searchRecord(appointmentList)
        #tally the appointments based on count of priority
        elif choice == 3:
            tallyAppointments(appointmentList)

        elif choice == 4:
            break
        else:
            print("Invalid Option Provided")
#calling main function
main()