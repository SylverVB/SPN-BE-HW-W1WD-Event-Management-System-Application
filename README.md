# Event Management System

This project is a command-line application for managing events and participants, built using Python. It allows you to create, manage, and organize events, register participants, and handle waitlists efficiently. The system is designed to demonstrate fundamental concepts of data structures and algorithms.

## Project Structure

- `participant.py`: Defines the `Participant` class, which stores details about participants.
- `queues.py`: Implements a simple queue data structure used for managing waitlists.
- `event.py`: Defines the `Event` class, which stores event details and manages participants and waitlists.
- `main.py`: The main application file, which provides the user interface and integrates all functionalities.

## Features

### 1. Event Creation and Management

- **Add Events**: Create new events with details like ID, name, date, time, location, and participant limit.
- **Remove Events**: Remove events by their ID.
- **Search Events**: Search for events by name, date, or location using binary search.
- **Display Schedule**: Display a sorted schedule of all events.

### 2. Participant Management

- **Register Participants**: Register participants for events, ensuring the participant limit is not exceeded.
- **Remove Participants**: Remove participants from events.
- **Display Participants**: Display details of registered participants and waitlisted participants for a given event.

### 3. Scheduling

- **Waitlist Management**: Automatically manage a waitlist for events that reach participant capacity. When a participant leaves, the first person in the queue is allowed to join the event.

### 4. Data Structures and Algorithms

- **Event Storage**: Events are stored in a dictionary with event ID as the key.
- **Participant Management**: Each event maintains its participants in a dictionary.
- **Searching**: Implemented binary search for efficient searching within the event list.
- **Sorting**: Implemented various sorting algorithms (Bubble Sort, Merge Sort, etc.) to display events in chronological order.

### 5. Additional Features

- **Suggest Events**: Suggest events to participants based on their registration history.
- **Generate Report**: Generate a report of all events and participants.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SylverVB/SPN-BE-HW-W1WD-Event-Management-System-Application.git
    ```
2. Navigate to the project directory:
    ```sh
    cd SPN-BE-HW-W1WD-Event-Management-System-Application
    ```

### Usage

Run the main application:
```sh
python main.py
```

Follow the on-screen prompts to interact with the Event Management System.

## Conclusion

This Event Management System provides a robust and efficient way to manage events and participants. It demonstrates fundamental concepts of data structures and algorithms in a practical application. The project can be further enhanced with additional features like a graphical user interface, database integration, and more complex scheduling algorithms.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This application is the property of Victor Bondaruk. As the owner, [Victor Bondaruk](https://github.com/SylverVB) retains all rights to the application.

## Contributors License Agreement (CLA)
By making a contribution to this project, you agree to the following terms and conditions for your contributions:

1. You grant the owner, Victor Bondaruk, a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable license to use, distribute, and modify your contributions as part of this project.
2. You represent that you are legally entitled to grant the above license.
3. You agree to promptly notify the owner of any facts or circumstances of which you become aware that would make these representations inaccurate in any respect.