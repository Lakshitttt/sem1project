Parking Lot Management System
A simple command-line based Parking Lot Management System implemented in Python to manage bookings, view current bookings, and track parking lot occupancy and revenue.

Features-
View parking lot layout with available and occupied slots
Book a parking slot by specifying slot ID, vehicle number, and parking duration
Automatic checkout when parking duration expires
Calculate parking fees based on duration with a tiered rate system
View currently active bookings with details and remaining time
Track total revenue collected from parking fees
User-friendly menu-driven interface with clear prompts and validations
Parking Lot Layout
5 rows (A to E), each with 5 slots (1 to 5), for a total of 25 parking slots:
text
[A1][A2][A3][A4][A5]
[B1][B2][B3][B4][B5]
[C1][C2][C3][C4][C5]
[D1][D2][D3][D4][D5]
[E1][E2][E3][E4][E5]
Slots marked with ✓ are available; slots marked with ✗ are occupied.

Usage
Run the program in a terminal or command prompt. The main menu options are:
Book Parking Slot
Enter an available slot ID
Enter vehicle registration number
Enter parking duration (hours, max 24)
You will see booking confirmation with details and fee
View Current Bookings
Displays all slots currently occupied along with vehicle info, booking time, checkout time, and time remaining
Exit the program and display total revenue collected

Parking Fee Calculation
₹5 per hour for the first 3 hours
₹3 per hour for every additional hour beyond 3 hours
Example: 5 hours would cost (3 * 5) + (2 * 3) = ₹21

Requirements
Python 3.x
Standard libraries used: os, time, datetime

Notes
The system automatically checks out vehicles once their parking duration expires, making slots available again.
Booking times and fees are displayed in a user-friendly format.
Appropriate validation ensures valid inputs and prevents double booking.
Use Ctrl+C to safely exit at any time. The program will handle interruptions gracefully.

Author
Lakshit Rajput
License
This project is released under the MIT License.
Thanks for visiting
