# AirBnB Clone Project

## Description

This project is a simplified clone of Airbnb. It implements a command-line storage system to manage objects related to Airbnb-like services, including functionalities for creating, updating, storing, and managing various entities such as users, places, states, cities, amenities, and reviews.

### Command Interpreter

The command interpreter is designed to manage the Airbnb objects of our project:

#### How to Start It

1. Clone the repository to your local machine
2. Navigate to the project directory
3. Run the command interpreter in interactive mode using:
   ```bash
   ./console.py

### How to Use It

1. create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
2. show: Prints the string representation of an instance based on the class name and id.
3. all: Prints all string representation of all instances based or not on the class name.
4. destroy: Deletes an instance based on the class name and id.
5. update: Updates an instance based on the class name and id by adding or updating attribute.

### Examples
1. (hbnb) create BaseModel
2. (hbnb) show BaseModel 1234-1234-1234
3. (hbnb) all BaseModel
4. (hbnb) update BaseModel 1234-1234-1234 email "a@example.com"
5. (hbnb) destroy BaseModel 1234-1234-1234
