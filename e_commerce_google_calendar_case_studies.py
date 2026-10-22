import time
import random


# ==========================================
# CASE STUDY 1: E-COMMERCE PRODUCT SORTING
# (DIVIDE AND CONQUER STRATEGY)
# ==========================================

class Product:
    def __init__(self, product_id, name, price, rating):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.rating = rating

    def __repr__(self):
        return f"[{self.product_id}] {self.name:<22} | Price: ${self.price:<7.2f} | Rating: {self.rating:.1f}/5.0"


def merge_sort(products, key="price", reverse=False):
    """Sorts product list using Merge Sort (Divide & Conquer)."""
    if len(products) <= 1:
        return products

    # Divide step
    mid = len(products) // 2
    left_half = merge_sort(products[:mid], key, reverse)
    right_half = merge_sort(products[mid:], key, reverse)

    # Conquer / Combine step
    return merge(left_half, right_half, key, reverse)


def merge(left, right, key, reverse):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        val_left = getattr(left[i], key)
        val_right = getattr(right[j], key)

        # Reverse check for descending sort (e.g., highest rating first)
        condition = (val_left > val_right) if reverse else (val_left <= val_right)

        if condition:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(products, key="price", reverse=False):
    """Sorts product list using Quick Sort (Divide & Conquer)."""
    if len(products) <= 1:
        return products

    # Divide step using pivot
    pivot = products[len(products) // 2]
    pivot_val = getattr(pivot, key)

    if not reverse:
        left = [x for x in products if getattr(x, key) < pivot_val]
        middle = [x for x in products if getattr(x, key) == pivot_val]
        right = [x for x in products if getattr(x, key) > pivot_val]
    else:
        left = [x for x in products if getattr(x, key) > pivot_val]
        middle = [x for x in products if getattr(x, key) == pivot_val]
        right = [x for x in products if getattr(x, key) < pivot_val]

    # Conquer / Combine step
    return quick_sort(left, key, reverse) + middle + quick_sort(right, key, reverse)


def generate_sample_products():
    names = [
        "Wireless Earbuds", "Gaming Laptop", "Mechanical Keyboard",
        "Smart Watch", "Noise Canceling Headphones", "4K Monitor",
        "Ergonomic Chair", "USB-C Hub", "External SSD 1TB", "Webcam 1080p"
    ]
    return [
        Product(
            product_id=f"P{100 + i}",
            name=names[i],
            price=round(random.uniform(15.0, 1200.0), 2),
            rating=round(random.uniform(3.0, 5.0), 1)
        )
        for i in range(len(names))
    ]


# ==========================================
# CASE STUDY 2: GOOGLE CALENDAR SCHEDULING
# (GREEDY STRATEGY)
# ==========================================

class CalendarEvent:
    def __init__(self, event_id, title, start_time, end_time):
        self.event_id = event_id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"[{self.event_id}] {self.title:<25} | Time: {self.format_time(self.start_time)} - {self.format_time(self.end_time)}"

    @staticmethod
    def format_time(minutes):
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"


def interval_scheduling_greedy(events):
    """Schedules maximum non-overlapping events using Greedy Strategy (Earliest Finish Time First)."""
    if not events:
        return []

    # Greedy Choice Criterion: Sort events by end_time ascending
    sorted_events = sorted(events, key=lambda e: e.end_time)

    scheduled = [sorted_events[0]]
    last_end_time = sorted_events[0].end_time

    for event in sorted_events[1:]:
        # Select event if start_time is greater than or equal to last selected end_time
        if event.start_time >= last_end_time:
            scheduled.append(event)
            last_end_time = event.end_time

    return scheduled


def generate_sample_events():
    return [
        CalendarEvent("E1", "Team Daily Standup", 540, 600),       # 09:00 - 10:00
        CalendarEvent("E2", "Client Project Review", 570, 660),    # 09:30 - 11:00
        CalendarEvent("E3", "Sprint Planning", 600, 690),          # 10:00 - 11:30
        CalendarEvent("E4", "1-on-1 Sync", 660, 720),               # 11:00 - 12:00
        CalendarEvent("E5", "Lunch with Mentor", 720, 780),         # 12:00 - 13:00
        CalendarEvent("E6", "Product Design Workshop", 750, 870),  # 12:30 - 14:30
        CalendarEvent("E7", "Architecture Review", 780, 840),      # 13:00 - 14:00
        CalendarEvent("E8", "Code Refactoring Session", 840, 930), # 14:00 - 15:30
    ]


# ==========================================
# MAIN INTERACTIVE INTERFACE
# ==========================================

def main():
    products = generate_sample_products()
    events = generate_sample_events()

    while True:
        print("\n=======================================================")
        print(" CASE STUDY: ALGORITHM DESIGN STRATEGIES")
        print("=======================================================")
        print("PART 1: E-COMMERCE SORTING (DIVIDE AND CONQUER)")
        print("  1. Display Unsorted Product Catalog")
        print("  2. Sort Products by Price (Ascending - Merge Sort)")
        print("  3. Sort Products by Rating (Descending - Quick Sort)")
        print("\nPART 2: GOOGLE CALENDAR (GREEDY STRATEGY)")
        print("  4. Display All Requested Events")
        print("  5. Optimize Schedule (Maximize Non-Overlapping Events)")
        print("\n  6. Exit")
        print("=======================================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Unsorted Product Catalog ---")
            for p in products:
                print(p)

        elif choice == "2":
            sorted_p = merge_sort(products, key="price", reverse=False)
            print("\n--- Sorted Products by Price (Merge Sort - Low to High) ---")
            for p in sorted_p:
                print(p)

        elif choice == "3":
            sorted_p = quick_sort(products, key="rating", reverse=True)
            print("\n--- Sorted Products by Rating (Quick Sort - High to Low) ---")
            for p in sorted_p:
                print(p)

        elif choice == "4":
            print("\n--- Requested Calendar Events (Including Conflicts) ---")
            for e in events:
                print(e)

        elif choice == "5":
            scheduled = interval_scheduling_greedy(events)
            print("\n--- Optimized Calendar Schedule (Greedy - Max non-overlapping) ---")
            for e in scheduled:
                print(e)
            print(f"\nTotal Scheduled Events: {len(scheduled)} / {len(events)}")

        elif choice == "6":
            print("\nExiting case studies application. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a choice between 1 and 6.")


if __name__ == "__main__":
    main()