from participant import Participant
from queues import Queue

class Event:
    def __init__(self, event_id, name, date, time, location, participant_limit):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.participant_limit = participant_limit
        self.participants = {}
        self.waitlist = Queue()

    def register_participant(self, participant_id, name, contact):
        if participant_id in self.participants or participant_id in [p.participant_id for p in self.waitlist.items]:
            return "\nParticipant ID is already registered."
        if len(self.participants) < self.participant_limit:
            self.participants[participant_id] = Participant(participant_id, name, contact)
            return "\nParticipant has been registered successfully."
        else:
            self.waitlist.enqueue(Participant(participant_id, name, contact))
            return "\nEvent is full. Participant has been added to waitlist."

    def remove_participant(self, participant_id):
        if participant_id in self.participants:
            del self.participants[participant_id]
            # self.handle_waitlist()
            return "\nParticipant has been removed successfully."
        return "\nParticipant ID has not been found."

    def display_participants(self):
        participants = "\nRegistered Participants:\n"
        for p_id, p in self.participants.items():
            participants += f"\nParticipant ID: {p.participant_id}, Name: {p.name}, Contact: {p.contact}\n"
        
        waitlist = "\nWaitlisted Participants:\n"
        for p in self.waitlist.items:
            waitlist += f"\nParticipant ID: {p.participant_id}, Name: {p.name}, Contact: {p.contact}\n"
        
        return participants + waitlist

    def handle_waitlist(self):
        if not self.waitlist.is_empty() and len(self.participants) < self.participant_limit:
            next_participant = self.waitlist.dequeue()
            self.participants[next_participant.participant_id] = next_participant
            return "\nWaitlisted participant has been added as a participant to the event."
        return "\nNo participants in waitlist or event is full."