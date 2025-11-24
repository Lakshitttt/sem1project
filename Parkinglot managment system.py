import os
import time
from datetime import datetime, timedelta

parking_lot = [
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
    print("=" * 60)
    print("🚗  PARKING LOT MANAGEMENT SYSTEM  🚗".center(60))
    print("=" * 60)
    print()


def parkinglotscreen():
    print("\n📍 PARKING LOT LAYOUT:")
    print("-" * 60)
    
    for row in parking_lot:
        row_display = []
        for slot in row:
            if slot in bookings:
                if datetime.now() >= bookings[slot]['checkout_time']:
                    auto_checkout(slot)
                    row_display.append(f"[{slot}✓]")  
                else:
                    row_display.append(f"[{slot}✗]")  
            else:
                row_display.append(f"[{slot}✓]")
        
        print("    ".join(row_display))
    
    print("-" * 60)
    print("Legend: ✓ = Available  |  ✗ = Occupied")
    print()


def blankslots():
    available = []
    
    for row in parking_lot:
        for slot in row:
            if slot not in bookings:
                available.append(slot)
            elif datetime.now() >= bookings[slot]['checkout_time']:
                auto_checkout(slot)
                available.append(slot)
    
    return available


def get_occupied_slots():
    occupied = []
    
    for slot in bookings:
        if datetime.now() < bookings[slot]['checkout_time']:
            occupied.append(slot)
    
    return occupied


def showavailableslots():
    available = blankslots()
    
    if available:
        print(f"\n✅ AVAILABLE SLOTS ({len(available)}/25):")
        print("-" * 60)
        
        for i in range(0, len(available), 5):
            print("  ".join(available[i:i+5]))
        print()
    else:
        print("\n❌ No slots available! Parking lot is full.\n")
    
    return available


def calculate_fee(duration):
    if duration <= 3:
        return duration * 5
    else:
        return (3 * 5) + ((duration - 3) * 3)


def auto_checkout(slot_id):
    global total_revenue
    
    if slot_id in bookings:
        booking = bookings[slot_id]
        duration = booking['duration']
        fee = calculate_fee(duration)
        
        total_revenue += fee
        
        del bookings[slot_id]
        
        print(f"✅ Auto-checkout: Slot {slot_id} | Vehicle {booking['vehicle']} | Fee: ${fee:.2f}")


def bookingslot():
    blankscreen()
    print_header()
    parkinglotscreen()
    
    available = showavailableslots()
    
    if not available:
        input("\nPress Enter to return to main menu...")
        return
    
    print("\n📝 BOOK A PARKING SLOT")
    print("-" * 60)
    
    while True:
        slot_id = input("Enter slot ID (e.g., A1, B3): ").strip().upper()
        
        if not slot_id:
            print("❌ Slot ID cannot be empty!")
            continue
        
        if slot_id not in available:
            if any(slot_id in row for row in parking_lot):
                print(f"❌ Slot {slot_id} is already occupied!")
            else:
                print(f"❌ Invalid slot ID! Choose from available slots.")
            continue
        
        break
    
    while True:
        vehicle = input("Enter vehicle number: ").strip().upper()
        if vehicle:
            break
        print("❌ Vehicle number cannot be empty!")
    
    while True:
        try:
            duration = float(input("Enter parking duration (in hours): "))
            if duration <= 0:
                print("❌ Duration must be greater than 0!")
                continue
            if duration > 24:
                print("❌ Maximum parking duration is 24 hours!")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!")
    
    booked_at = datetime.now()
    checkout_time = booked_at + timedelta(hours=duration)
    
    fee = calculate_fee(duration)
    
    bookings[slot_id] = {
        'vehicle': vehicle,
        'booked_at': booked_at,
        'checkout_time': checkout_time,
        'duration': duration
    }
    
    blankscreen()
    print_header()
    print("\n✅ BOOKING SUCCESSFUL!")
    print("=" * 60)
    print(f"Slot ID:           {slot_id}")
    print(f"Vehicle Number:    {vehicle}")
    print(f"Booked At:         {booked_at.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"Checkout Time:     {checkout_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
    print(f"Duration:          {duration} hours")
    print(f"Parking Fee:       ${fee:.2f}")
    print("=" * 60)
    print("\n💡 Your slot will automatically become available after checkout time.")
    
    input("\nPress Enter to return to main menu...")


def view_current_bookings():
    blankscreen()
    print_header()
    
    occupied = get_occupied_slots()
    
    print("\n🅿️  CURRENT BOOKINGS")
    print("=" * 60)
    
    if not occupied:
        print("No active bookings at the moment.")
    else:
        print(f"Total Occupied Slots: {len(occupied)}/25\n")
        
        for slot in occupied:
            booking = bookings[slot]
            vehicle = booking['vehicle']
            booked_at = booking['booked_at']
            checkout_time = booking['checkout_time']
            
            time_remaining = checkout_time - datetime.now()
            hours_remaining = time_remaining.total_seconds() / 3600
            
            print(f"Slot {slot}:")
            print(f"  Vehicle: {vehicle}")
            print(f"  Booked At: {booked_at.strftime('%I:%M %p')}")
            print(f"  Checkout At: {checkout_time.strftime('%I:%M %p')}")
            print(f"  Time Remaining: {hours_remaining:.2f} hours")
            print()
    
    print("=" * 60)
    input("\nPress Enter to return to main menu...")


def main_menu():
    while True:
        blankscreen()
        print_header()
        parkinglotscreen()
        
        available = len(blankslots())
        occupied = len(get_occupied_slots())
        
        print(f"Available: {available}/25  |  Occupied: {occupied}/25  |  Total Revenue: ${total_revenue:.2f}")
        print("\n📋 MAIN MENU")
        print("=" * 60)
        print("1. Book a Parking Slot")
        print("2. View Current Bookings")
        print("3. Exit")
        print("=" * 60)
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            bookingslot()
        elif choice == '2':
            view_current_bookings()
        elif choice == '3':
            blankscreen()
            print_header()
            print("\n👋 Thank you for using Parking Lot Management System!")
            print(f"💰 Total Revenue Collected: ${total_revenue:.2f}")
            print("=" * 60)
            print()
            break
        else:
            print("\n❌ Invalid choice! Please enter a number between 1-3.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        blankscreen()
        print("\n\n👋 Application closed. Goodbye!\n")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        input("\nPress Enter to exit...")
        