import pandas as pd

def rent_calculator():
    total_rent = float(input("Enter the total monthly rent: "))
    num_roommates = int(input("Enter the number of roommates: "))
    utilities = float(input("Enter total utility costs (e.g., electricity, water): "))

    roommate_details = []
    for i in range(num_roommates):
        name = input(f"Enter the name of roommate {i + 1}: ")
        contribution = float(input(f"Enter the percentage of rent roommate {i + 1} will pay (e.g., 40 for 70%): "))
        roommate_details.append({'Name': name, 'Contribution (%)': contribution})

    print("\n--- Rent Breakdown ---")
    breakdown = []
    for roommate in roommate_details:
        share = ((roommate['Contribution (%)'] / 100) * total_rent) + (utilities / num_roommates)
        breakdown.append({'Name': roommate['Name'], 'Rent + Utilities': share})

    df = pd.DataFrame(breakdown)
    print(df)
    df.to_csv('rent_breakdown.csv', index=False)
    print("Rent breakdown saved to 'rent_breakdown.csv'.")

rent_calculator()