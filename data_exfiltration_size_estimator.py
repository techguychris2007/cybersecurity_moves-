bandwidth = float(input("Enter the bandwidth in KB/s:"))
hours = float(input("Enter the time window in hours: "))
time_in_seconds = hours * 3600
total_kb =bandwidth * time_in_seconds
total_mb = total_kb / 1024
print("\n=== Estimated data exfiltration Estimate ===")
print(f"TOTAL_KB: {round(total_kb, 2)} KB")
print(f"TOTAL_MB: {round(total_mb, 2)} MB")
if total_mb < 100:
    print("Estimated exfiltration size: low")
elif total_mb < 1024:
    print("Estimated exfiltration size: moderate")
else:
    print("Estimated exfiltration size: high")
