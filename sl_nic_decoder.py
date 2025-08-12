"""
This script calculates the birth date from a National Identity Card (NIC) number in Sri Lanka.
It extracts the year, month, and day from the NIC number and determines the gender based on the NIC format.
It also accounts for leap years when calculating the date.

Author: Randika Nonis
Date: 2025/08/12
"""


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


print("*" * 50)
print("")
nic = input("Enter your NIC number:")

nic_length = len(nic)

if not (nic_length == 10 or nic_length == 12):
    print("Invalid NIC number format. Please enter a valid NIC number.")
    exit()


year = int(nic[0:2]) + 1900
days = int(nic[2:5])

if nic_length == 12:
    year = int(nic[0:4])
    days = int(nic[4:7])

birth_day = int(0)
gender = "Male"

if days > 500:
    days -= 500
    gender = "Female"

month = 0
monthly_day_counts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_monthly_day_counts = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_names = {1: "January", 2: "February", 3: "March", 4: "April",
                5: "May", 6: "June", 7: "July", 8: "August",
                9: "September", 10: "October", 11: "November", 12: "December"}

full_day_count = leap_year_monthly_day_counts if is_leap_year(
    year) else monthly_day_counts

for day_count in full_day_count:
    month += 1
    birth_day = days
    days = days - day_count

    if days < 0:
        break

print(
    f"Your birth date is {year}-{months_names[month]}-{birth_day:02d}. Your gender is {gender}.")
print("")
print("*" * 50)
print("Thank you for using the NIC Birth Date Calculator!")
