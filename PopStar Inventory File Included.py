import pandas as pd

# ----------------------------------------
# Inventory System Info
inventory_name = "PopStar"
owner_name = "Aisyah Dewi"
# ----------------------------------------

# Load cargo data from CSV
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("\nCargo data loaded successfully!")
        return df
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return None

# Display all data
def display_data(df):
    print("\nCurrent Inventory Data:")
    print(df.to_string(index=False))

# Filter by destination or type
def filter_data(df, by="Destination", keyword="Jakarta"):
    filtered_df = df[df[by].str.contains(keyword, case=False, na=False)]
    return filtered_df

# Sort by priority (High > Medium > Low)
def sort_by_priority(df):
    priority_map = {"High": 1, "Medium": 2, "Low": 3}
    df["PriorityValue"] = df["Priority"].map(priority_map)
    sorted_df = df.sort_values(by="PriorityValue").drop(columns="PriorityValue")
    return sorted_df

# Export to CSV
def export_data(df, filename="sorted_inventory.csv"):
    df.to_csv(filename, index=False)
    print(f"Data exported to {filename}")

# Main function
if __name__ == "__main__":
    print("Welcome to", inventory_name)
    print("👩‍💼 Managed by:", owner_name)
    print("====================================")

    file_path = "cargo_inventory.csv"  # Update with your file path
    df = load_data(file_path)

    if df is not None:
        display_data(df)

        # Example filter and sort
        keyword = input("\n🔎 Enter destination to filter (e.g., Jakarta): ")
        filtered_df = filter_data(df, by="Destination", keyword=keyword)
        sorted_df = sort_by_priority(filtered_df)

        display_data(sorted_df)
        export_data(sorted_df)
