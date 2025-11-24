import os
import time
from datetime import datetime, timedelta

p_lot = [
    ['A1', 'A2', 'A3', 'A4', 'A5'],
    ['B1', 'B2', 'B3', 'B4', 'B5'],
    ['C1', 'C2', 'C3', 'C4', 'C5'],
    ['D1', 'D2', 'D3', 'D4', 'D5'],
    ['E1', 'E2', 'E3', 'E4', 'E5']
]

bookings = {}

total_revenue = 0.0


def blankscreen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("🚗  PARKING LOT MANAGEMENT SYSTEM  🚗".center(60))
    print()


def parkinglotscreen():
    print("\n PARKING LOT LAYOUT:")
    print("-" * 60)
    
    for row in p_lot:
        row_display = []
        for sloot in row:
            if sloot in bookings:
                if datetime.now() >= bookings[sloot]['checkout_time']:
                    auto_checkout(sloot)
                    row_display.append(f"[{sloot}✓]")  
                else:
                    row_display.append(f"[{sloot}✗]")  
            else:
                row_display.append(f"[{sloot}✓]")
        
        print("    ".join(row_display))
    
    print("Legend: ✓ = Available  |  ✗ = Occupied")
    print()


def blanksloots():
    available = []
    
    for row in p_lot:
        for sloot in row:
            if sloot not in bookings:
                available.append(sloot)
            elif datetime.now() >= bookings[sloot]['checkout_time']:
                auto_checkout(sloot)
                available.append(sloot)
    
    return available


def get_occupied_sloots():
    occupied = []
    
    for sloot in bookings:
        if datetime.now() < bookings[sloot]['checkout_time']:
            occupied.append(sloot)
    
    return occupied


def showavailablesloots():
    available = blanksloots()
    
    if available:
        print(f"\n AVAILABLE slootS ({len(available)}/25):")
        print("-" * 60)
        
        for i in range(0, len(available), 5):
            print("  ".join(available[i:i+5]))
        print()
    else:
        print("\n Parking lot is full,better luck next time bae\n")
    
    return available


def calculate_fee(duration):
    if duration <= 3:
        return duration * 5
    else:
        return (3 * 5) + ((duration - 3) * 3)


def auto_checkout(sloot_id):
    global total_revenue
    
    if sloot_id in bookings:
        booking = bookings[sloot_id]
        duration = booking['duration']
        fee = calculate_fee(duration)
        
        total_revenue += fee
        
        del bookings[sloot_id]
        
        print(f" Auto-checkout: sloot {sloot_id} | vehicel {booking['vehicel']} | Fee: ${fee:.2f}")


def bookingsloot():
    blankscreen()
    print_header()
    parkinglotscreen()
    
    available = showavailablesloots()
    
    if not available:
        input("\nPress Enter to return to main menu")
        return
    
    print("\nBOOK A PARKING slot")
    print("-" * 60)
    
    while True:
        sloot_id = input("Enter slot ID (e.g., A1, B3): ").strip().upper()
        
        if not sloot_id:
            print(" sloot ID cannot be empty!")
            continue
        
        if sloot_id not in available:
            if any(sloot_id in row for row in p_lot):
                print(f"sloot {sloot_id} is already occupied!")
            else:
                print(f" Invalid sloot ID! Choose from available sloots.")
            continue
        
        break
    
    while True:
        vehicel = input("Enter vehicel number: ").strip().upper()
        if vehicel:
            break
        print(" vehicel number cannot be empty,dumbooo!")
    
    while True:
        try:
            duration = float(input("Enter parking duration (in hours): "))
            if duration <= 0:
                print(" Duration must be greater than 0 you fool!")
                continue
            if duration > 24:
                print(" Maximum parking duration is 24 hours, babe!")
                continue
            break
        except ValueError:
            print(" Please enter a valid number!")
    
    booked_at = datetime.now()
    checkout_time = booked_at + timedelta(hours=duration)
    
    fee = calculate_fee(duration)
    
    bookings[sloot_id] = {
        'vehicel': vehicel,
        'booked_at': booked_at,
        'checkout_time': checkout_time,
        'duration': duration
    }
    
    blankscreen()
    print_header()
    print("\n BOOKING SUCCESSFUL!")
    print("=" * 60)
    print(f"sloot ID:           {sloot_id}")
    print(f"vehicel Number:    {vehicel}")
    print(f"Booked At:         {booked_at.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"Checkout Time:     {checkout_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"Duration:          {duration} hours")
    print(f"Parking Fee:       ${fee:.2f}")
    print("=" * 60)
    print("\n sloot will automatically become available after checkout")
    
    input("\nPress Enter to return to main menu...")


def view_current_bookings():
    blankscreen()
    print_header()
    
    occupied = get_occupied_sloots()
    
    print("\n  CURRENT BOOKINGS")    
    if not occupied:
        print("No active bookings at moment.")
    else:
        print(f"Total Occupied sloots: {len(occupied)}/25\n")
        
        for sloot in occupied:
            booking = bookings[sloot]
            vehicel = booking['vehicel']
            booked_at = booking['booked_at']
            checkout_time = booking['checkout_time']
            
            time_remaining = checkout_time - datetime.now()
            hours_remaining = time_remaining.total_seconds() / 3600
            
            print(f"sloot {sloot}:")
            print(f"  vehicel: {vehicel}")
            print(f"  Bookeed At: {booked_at.strftime('%I:%M %p')}")
            print(f"  Checkoutt At: {checkout_time.strftime('%I:%M %p')}")
            print(f"  Time Remainingg: {hours_remaining:.2f} hours")
            print()
    
    input("\nPress enter to return to main menu ")


def main_menu():
    while True:
        blankscreen()
        print_header()
        parkinglotscreen()
        
        available = len(blanksloots())
        occupied = len(get_occupied_sloots())
        
        print(f"Available: {available}/25  |  Occupied: {occupied}/25  |  Total Revenue: ${total_revenue:.2f}")
        print("\n MAIN MENU")
        print("=" * 60)
        print("1. Book a parking sloot")
        print("2. View Current Bookings")
        print("3. Exit")
        print("=" * 60)
        
        choce = input("\nEnter your choce (1-3): ").strip()
        
        if choce == '1':
            bookingsloot()
        elif choce == '2':
            view_current_bookings()
        elif choce == '3':
            blankscreen()
            print_header()
            print("\n Thank you for using Parking Lot Management System!, visit us soon\n")
            print(f" Total Revenue Collected: rupee {total_revenue:.2f}")
            print("=" * 60)
            print()
            break
        else:
            print("\n Invaalid choce! Please enter a number between 1-3.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        blankscreen()
        print("\n\n Application closed. Goodbye!\n")
    except Exception as e:
        print(f"\n An error occurred: {e}")
        input("\nPress Enter to exit...")
        