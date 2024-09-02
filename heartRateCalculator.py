def is_valid_heart_rate(heartRate):
    # Flag to detect the peak has been found
    peak_found = False
    
    for i in range(1, len(heartRate)):
        if heartRate[i] == heartRate[i - 1]:
            return False
        elif heartRate[i] > heartRate[i - 1]:
            if peak_found:
                return False
        elif heartRate[i] < heartRate[i - 1]:
            peak_found = True
    
    # Return True if there was an increase followed by a decrease
    return peak_found

# Test cases
heartRate1 = [70, 85, 100, 95, 90, 80]
heartRate2 = [60, 65, 70, 75, 80, 80, 75]

print(is_valid_heart_rate(heartRate1))  # Output: True
print(is_valid_heart_rate(heartRate2))  # Output: False
