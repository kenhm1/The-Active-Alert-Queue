# Initialize an empty list
alert_queue = []

# Main menu loop
while True:
    print("\n===== SOC Alert Queue System =====")
    print("1. Log New Alert")
    print("2. View Active Queue")
    print("3. Resolve Oldest Alert")
    print("4. Exit System")

    choice = input("Please select an option (1-4): ")

    # Option 1: Log a new alert
    if choice == "1":
        threat = input("Enter threat description: ")
        alert_queue.append(threat)
        print("Alert logged successfully!")

    # Option 2: View active alerts
    elif choice == "2":
        print("--- Current Pending Alerts ---")

        for alert in alert_queue:
            print(alert)

    # Option 3: Resolve the oldest alert
    elif choice == "3":
        if len(alert_queue) > 0:
            resolved_threat = alert_queue.pop(0)
            print(f"Resolved and cleared: {resolved_threat}")
        else:
            print("No alerts are pending resolution.")

    # Option 4: Exit the system
    elif choice == "4":
        print("Exiting SOC Alert Queue System.")
        break

    # Handle invalid choices
    else:
        print("Invalid selection. Please choose 1-4.")
