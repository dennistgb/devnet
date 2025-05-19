# Write your Python script here
def calculate_area(length, width):
    
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        print("hi") 
        return length * width
    else:
        print("uhoh")
        # Return error message for invalid input
        return "Invalid input"

# Example usage (for testing, not required in the final script)
print(calculate_area(10, 5))
# print(calculate_area(2.5, 4))
# print(calculate_area("abc", 5))