from openpyxl import Workbook, load_workbook

workbook = Workbook()

sheet = workbook.active
sheet.title = "Students"

sheet.append(["USN", "Name", "Marks"])
sheet.append(["01", "A", 95])
sheet.append(["02", "B", 60])

workbook.save("students.xlsx")

print("Spreadsheet created")

workbook = load_workbook("students.xlsx")
sheet = workbook["Students"]

print("\nStudent Details:")

for row in sheet.iter_rows(values_only=True):
    print(row)

sheet["C2"] = 92

workbook.save("students.xlsx")

print("\nA's marks updated to 92")