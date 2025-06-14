import pandas as pd
import os

# ----------------------------------------
# Inventory System Info
inventory_name = "PopStar"
owner_name = "Aisyah Dewi"
file_path = "cargo_inventory.csv"
# ----------------------------------------

# Create sample data if file doesn't exist
def create_sample_data():
    data = {
        "ItemID": [101, 102, 103, 104, 105],
        "ItemType": ["Furniture", "Electronic", "Plastic", "Electronics", "Textiles"],
        "Destination": ["Surabaya", "Surabaya", "Surabaya", "Gresik", "Sidoarjo"],
        "Weight(kg)": [15, 80, 10, 22, 35],
        "Priority": ["High", "Low", "Medium", "High", "Medium"]
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Cargo file '{file_path}' created.")

# Load cargo data from CSV
def load_data():
    if not os.path.exists(file_path):
        create_sample_data()
    try:
        df = pd.read_csv(file_path)
        print("Cargo data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Display full table
def display_data(df, title="Current Inventory:"):
    print("\n" + title)
    print(df.to_string(index=False))

# Display summary (only Destination & ItemType)
def display_summary(df, title="Filtered Cargo Summary (Destination & ItemType):"):
    print("\n" + title)
    print(df[["Destination", "ItemType"]].to_string(index=False))

# Filter by destination
def filter_data(df, by="Destination", keyword="Surabaya"):
    return df[df[by].str.contains(keyword, case=False, na=False)]

# Sort by priority level
def sort_by_priority(df):
    priority_map = {"High": 1, "Medium": 2, "Low": 3}
    df["PriorityValue"] = df["Priority"].map(priority_map)
    sorted_df = df.sort_values(by="PriorityValue").drop(columns="PriorityValue")
    return sorted_df

# Export result
def export_data(df, filename="sorted_inventory.csv"):
    df.to_csv(filename, index=False)
    print(f"Sorted data exported to '{filename}'")

# Main application
if __name__ == "__main__":
    print("Welcome to", inventory_name)
    print("Managed by:", owner_name)
    print("=" * 40)

    df = load_data()

    if df is not None:
        display_data(df, title="Original Cargo Inventory")

        keyword = input("\nEnter destination to filter (e.g., Surabaya): ").strip()
        filtered_df = filter_data(df, by="Destination", keyword=keyword)

        if filtered_df.empty:
            print(f"No cargo found for destination: {keyword}")
        else:
            sorted_df = sort_by_priority(filtered_df)
            display_summary(sorted_df, title=f"Sorted Cargo Summary for '{keyword}'")
            export_data(sorted_df)

