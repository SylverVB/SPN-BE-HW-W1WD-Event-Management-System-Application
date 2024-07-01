# Mini-Project: Event Management

# Project Requirements:

# 1. Event Creation and Management:
# - Store information about events, including event ID, name, date, time, location, and participant limit.
# - Implement a function to add new events.
# - Implement a function to remove events.
# - Implement a function to search for events by name, date, or location using searching algorithms.

# 2. Participant Management:
# - Maintain a dictionary of participants for each event, with participant ID as the key and participant details (name, contact    information) as the value.
# - Implement a function to register participants for an event, ensuring the participant limit is not exceeded.
# - Implement a function to remove participants from an event.
# - Implement a function to display participant details for a given event.

# 3. Scheduling:
# - Implement a function to display a schedule of all events.
# - Implement a waitlist system using a queue for events that reach participant capacity.
# - When a participant leaves the event, allow the first person in the queue to join the event

# 4. Data Structures and Algorithms:
# - Use a dictionary to store event information, with event ID as the key.
# - Use a dictionary to maintain the participants for each event.
# - Implement binary search for efficient searching within the event list.
# - Implement sorting algorithms to display events in chronological order.

# 5. Additional Features (Optional):
# - Implement a feature to suggest events to participants based on their registration history and interests.
# - Implement a feature to generate a report of all events and participants.


from event import Event
import re


# ====== EVENT MANAGEMENT ======

events = {}

def input_event_details():
    print("Please enter the following information to add an event:\n")
    while True:
        try:
            event_id = int(input("\nEvent ID (for example, 1 or 2): \n"))
            break
        except ValueError:
            print("\nEvent ID must be an integer.")
    
    name = input("\nEvent name: \n")
    
    while True:
        date = input("\nEvent date (YYYY-MM-DD): \n")
        if re.match(r"^\d{4}-\d{2}-\d{2}$", date):
            break
        else:
            print("\nPlease enter a valid date in the format YYYY-MM-DD.")
    
    while True:
        time = input("\nEvent time (HH:MM): \n")
        if re.match(r"^\d{2}:\d{2}$", time):
            break
        else:
            print("\nPlease enter a valid time in the format HH:MM.")
    
    location = input("\nEvent location (e.g., physical address, venue name, or URL): \n")
    
    while True:
        try:
            participant_limit = int(input("\nParticipant limit: \n"))
            break
        except ValueError:
            print("\nParticipant limit must be an integer.")
    # Returning only event details because the actual Event object is created and managed within a standalone function add_event()
    return event_id, name, date, time, location, participant_limit


def input_participant_details():
    print("\nPlease enter the following information to add a participant:")
    while True:
        try:
            participant_id = int(input("\nParticipant ID: \n"))
            break
        except ValueError:
            print("\nParticipant ID must be an integer.")
    name = input("\nParticipant full name: \n").title()
    while not re.match(r"^[A-Za-z]+ [A-Za-z]+$", name):
        name = input("\nPlease enter your first and last name( for example, John Doe): \n").title()
    contact = input("\nParticipant contact information (phone or email): \n")
    while not (re.match(r"^\d{10}$", contact) or re.match(r"[^@]+@[^@]+\.[^@]+", contact)):
        contact = input("\nPlease enter a valid phone number (10 digits) or email address: ")
    # Returning only participant details (ID, name, contact) because the actual Participant object is created and managed within the Event class:
    return participant_id, name, contact

def add_event():
    event_id, name, date, time, location, participant_limit = input_event_details()
    if event_id in events:
        return "\nEvent ID already exists."
    events[event_id] = Event(event_id, name, date, time, location, participant_limit)
    return "\nEvent has been added successfully."

def remove_event(event_id):
    if event_id in events:
        del events[event_id]
        return "\nEvent has been removed successfully."
    return "\nEvent ID has not been found."

# Sorting Algorithms to sort events in chronological order:

# Option 1. Built-in sorted():

# lambda x: x.date creates an anonymous function that takes an object x and returns its date attribute:
# x represents each item in the iterable (in this case, each event in the list of events),
# x.date accesses the date attribute of the event object x,
# key parameter in sorted takes a function that extracts a comparison key from each list element:
sorted_events = sorted(events.values(), key=lambda x: x.date)

# Option 2. Built-in sort():

events_list = list(events.values())
# print(events_list)
events_list.sort(key=lambda x: x.date)

# Option 3. Insertion Sort:

def insertion_sort(events_list):
    for i in range(1, len(events_list)):
        key = events_list[i]
        j = i - 1
        while j >= 0 and key.date < events_list[j].date:
            events_list[j + 1] = events_list[j]
            j -= 1
        events_list[j + 1] = key
    return events_list

# Option 4. Bubble Sort:

def bubble_sort(events_list):
    n = len(events_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if events_list[j].date > events_list[j+1].date:
                events_list[j], events_list[j+1] = events_list[j+1], events_list[j]
    return events_list

# Option 5. Merge Sort:

def merge_sort(events_list):
    if len(events_list) > 1:
        mid = len(events_list) // 2
        left_half = events_list[:mid]
        right_half = events_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].date < right_half[j].date:
                events_list[k] = left_half[i]
                i += 1
            else:
                events_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            events_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            events_list[k] = right_half[j]
            j += 1
            k += 1
    return events_list

def display_sorted_events():
    events_list = list(events.values())
    # Using Bubble Sort, but we can choose any sorting method here:
    sorted_events = bubble_sort(events_list)
    for event in sorted_events:
        # vars(event) returns the __dict__ attribute of the event object, 
        # which is a dictionary containing all the attributes of the event object:
        print(vars(event))

# Searching for events by name, date, or location using searching algorithms:

# Option 1. Linear Search.

def recursive_search_events(events_dict, keyword, index=0, results=None):
    if results is None:
        results = []

    event_keys = list(events_dict.keys())

    if index >= len(event_keys):
        return results

    event_id = event_keys[index]
    event = events_dict[event_id]

    if (keyword.lower() in event.name.lower() or
        keyword.lower() in event.date.lower() or
        keyword.lower() in event.location.lower()):
        results.append(vars(event))

    return recursive_search_events(events_dict, keyword, index + 1, results)

def linear_search_events(keyword):
    return binary_search_events(events, keyword)

# Option 2. Binary Search (default method).

def binary_search_events(events_list, keyword):
    left, right = 0, len(events_list) - 1
    while left <= right:
        mid = (left + right) // 2
        event = events_list[mid]
        if (keyword.lower() in event.name.lower() or
            keyword.lower() in event.date.lower() or
            keyword.lower() in event.location.lower()):
            return vars(event)
        elif keyword < event.date:
            right = mid - 1
        else:
            left = mid + 1
    return None

def search_events(keyword):
    events_list = list(events.values())
    # Using Merge Sort sorting method:
    sorted_events = merge_sort(events_list)
    results = []
    for event in sorted_events:
        if (keyword.lower() in event.name.lower() or
            keyword.lower() in event.date.lower() or
            keyword.lower() in event.location.lower()):
            results.append(
                f"\nEvent ID: {event.event_id}\n"
                f"Name: {event.name}\n"
                f"Date: {event.date}\n"
                f"Time: {event.time}\n"
                f"Location: {event.location}\n"
                f"Participant Limit: {event.participant_limit}\n")
    return results


# ====== BONUS  ======

def suggest_events(participant_id):
    participant_id = int(participant_id)
    interested_events = []
    for event in events.values():
        if participant_id in event.participants:
            interested_events.append(event)
    
    formatted_events = []
    for event in interested_events:
        formatted_event = (
            f"\nEvent ID: {event.event_id}\n"
            f"Name: {event.name}\n"
            f"Date: {event.date}\n"
            f"Time: {event.time}\n"
            f"Location: {event.location}\n"
            f"Participant Limit: {event.participant_limit}\n"
        )
        formatted_events.append(formatted_event)
    
    return formatted_events


def generate_report():
    # Initializing an empty string that will be used to accumulate the report's contents:
    report = ""
    for event_id, event in events.items():
        # Appending the given string to the current value of report:
        report += f"\nEvent ID: {event_id}\n"
        # += ensures that we keep adding more information to report as we loop through events and participants:
        report += f"Event Details: Event ID: {event.event_id}, Name: {event.name}, Date: {event.date}, Time: {event.time}, Location: {event.location}, Participant Limit: {event.participant_limit}\n"
        # Using += ensures that all parts of the report are combined into one final string:
        report += "Participants:\n"
        for p_id, participant in event.participants.items():
            report += f"  Participant ID: {participant.participant_id}, Name: {participant.name}, Contact: {participant.contact}\n"
        report += "Waitlisted Participants:\n"
        for participant in event.waitlist.items:
            report += f"  Participant ID: {participant.participant_id}, Name: {participant.name}, Contact: {participant.contact}\n"
    return report


# ====== PARTICIPANT MANAGEMENT ======

def register_participant(event_id):
    if event_id not in events:
        return "\nEvent ID has not been found."
    participant_id, name, contact = input_participant_details()
    return events[event_id].register_participant(participant_id, name, contact)

def remove_participant(event_id, participant_id):
    if event_id not in events:
        return "\nEvent ID has not been found."
    return events[event_id].remove_participant(participant_id)

def display_participants(event_id):
    if event_id not in events:
        return "\nEvent ID has not been found."
    return events[event_id].display_participants()


# ====== SCHEDULING AND WAITLIST ======

def display_schedule():
    # sorted_events = sorted(events.values(), key=lambda x: x.date)
    events_list = list(events.values())
    # Using Insertion Sort sorting method:
    sorted_events = insertion_sort(events_list)
    for event in sorted_events:
        print(
            f"\nEvent ID: {event.event_id}\n"
            f"Name: {event.name}\n"
            f"Date: {event.date}\n"
            f"Time: {event.time}\n"
            f"Location: {event.location}\n"
            f"Participant Limit: {event.participant_limit}\n"
        )

def handle_waitlist(event_id):
    if event_id in events:
        return events[event_id].handle_waitlist()
    return "\nEvent ID has not been found."


# ====== MAIN FUNCTION ======

def main():
    while True:
        print("\nEvent Management System")
        print("1. Events")
        print("2. Participants")
        print("3. Generate Report")
        print("4. Exit")

        main_choice = input("\nEnter your choice: \n")

        if main_choice == '1':
            while True:
                print("\nEvents Menu")
                print("1. Add Event")
                print("2. Remove Event")
                print("3. Search Events")
                print("4. Display Event Schedule")
                print("5. Suggest Events")
                print("6. Back to Main Menu")

                event_choice = input("\nEnter your choice: \n")

                if event_choice == '1':
                    print(add_event())
                elif event_choice == '2':
                    event_id = int(input("\nEnter event ID to remove: \n"))
                    print(remove_event(event_id))
                elif event_choice == '3':
                    keyword = input("\nEnter keyword to search (event name, date (YYY-MM-DD) or location): \n")
                    results = search_events(keyword)
                    if results:
                        for result in results:
                            print(result)
                    else:
                        print("\nNo matching events found.")
                elif event_choice == '4':
                    display_schedule()
                elif event_choice == '5':
                    participant_id = input("\nEnter participant ID for event suggestions: \n")
                    try:
                        participant_id = int(participant_id)
                        suggestions = suggest_events(participant_id)
                        if suggestions:
                            for suggestion in suggestions:
                                print(suggestion)
                        else:
                            print(f"\nNo participant with ID {participant_id} found.")
                    except ValueError:
                        print("\nInvalid participant ID. Please enter a valid integer.")

                elif event_choice == '6':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        elif main_choice == '2':
            while True:
                print("\nParticipants Menu")
                print("1. Register Participant")
                print("2. Remove Participant")
                print("3. Display Participants")
                print("4. Handle Waitlist")
                print("5. Back to Main Menu")

                participant_choice = input("\nEnter your choice: \n")

                if participant_choice == '1':
                    event_id = int(input("\nEnter event ID to register participant: \n"))
                    print(register_participant(event_id))
                elif participant_choice == '2':
                    event_id = int(input("\nEnter event ID to remove participant: \n"))
                    participant_id = int(input("\nEnter participant ID to remove: \n"))
                    print(remove_participant(event_id, participant_id))
                elif participant_choice == '3':
                    event_id = int(input("\nEnter event ID to display participants: \n"))
                    participants = display_participants(event_id)
                    print(participants)
                elif participant_choice == '4':
                    event_id = int(input("\nEnter event ID to handle waitlist: \n"))
                    print(handle_waitlist(event_id))
                elif participant_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        elif main_choice == '3':
            report = generate_report()
            print(report)

        elif main_choice == '4':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()