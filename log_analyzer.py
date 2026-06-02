with open("sample.log","r") as file:
    data = file.readlines()

error_count = 0
warning_count = 0
info_count = 0

suspicious_events = []

for line in data:

    if "ERROR" in line:
        error_count += 1
        suspicious_events.append(line)
    
    if "WARNING" in line:
        warning_count += 1

        suspicious_events.append(line)
    
    if "INFO" in line:
        info_count += 1

total_lines = len(data)

print("\n" + "="*30)
print("Log Analysis Report")
print("="*30)

print("Total Lines: ",total_lines)
print("Total Error: ",error_count)
print("Total Warning: ",warning_count)
print("Total Info: ",info_count)

print("\nSuspicious Events: ")
print("-"*30)

for event in suspicious_events:
    print(event)