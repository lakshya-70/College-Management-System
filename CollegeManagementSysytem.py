# 16th github project --> College Management System
print("---------College Management System----------")
students = {}
fees = {}
marks = {}
attendance = {}


def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"


def add_student():
    roll = input("Enter Roll Number: ").strip()
    if roll in students:
        print("❌ Student already exists!")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    gender = input("Enter Gender (M/F/O): ").strip()
    course = input("Enter Course: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()

    students[roll] = {
        "name": name, "age": age, "gender": gender,
        "course": course, "phone": phone, "email": email
    }

    total_fee = float(input("Enter Total Fee: "))
    fees[roll] = {
        "total_fee": total_fee,
        "paid_fee": 0.0,
        "fine": 0.0
    }

    marks[roll] = {}
    attendance[roll] = {"present": 0, "absent": 0, "total": 0}

    print("✅ Student " + name + " added successfully!")


def view_student():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    s = students[roll]
    print("\n========== STUDENT PROFILE ==========")
    print("Roll No   : " + roll)
    print("Name      : " + s["name"])
    print("Age       : " + s["age"])
    print("Gender    : " + s["gender"])
    print("Course    : " + s["course"])
    print("Phone     : " + s["phone"])
    print("Email     : " + s["email"])

    x = fees[roll]
    due = x["total_fee"] + x["fine"] - x["paid_fee"]
    print("\n---------- FEES ----------")
    print("Total Fee : ₹" + str(x["total_fee"]))
    print("Fine      : ₹" + str(x["fine"]))
    print("Paid Fee  : ₹" + str(x["paid_fee"]))
    print("Due       : ₹" + str(due))
    if due == 0:
        print("Fee Status: ✅ Clear")
    else:
        print("Fee Status: ⚠️ Pending")

    if len(marks[roll]) > 0:
        print("\n---------- MARKS ----------")
        total = 0
        count = 0
        for subject in marks[roll]:
            m = marks[roll][subject]
            print(subject.ljust(15) + ": " + str(m) + " (" + get_grade(m) + ")")
            total = total + m
            count = count + 1
        avg = total / count
        print("Average   : " + str(round(avg, 2)))
        print("Grade     : " + get_grade(avg))

    a = attendance[roll]
    if a["total"] > 0:
        pct = (a["present"] / a["total"]) * 100
        print("\n---------- ATTENDANCE ----------")
        print("Present   : " + str(a["present"]))
        print("Absent    : " + str(a["absent"]))
        print("Total     : " + str(a["total"]))
        print("Percent   : " + str(round(pct, 2)) + "%")

    print("=====================================")


def view_all():
    if len(students) == 0:
        print("📭 No students found!")
        return

    print("\n" + "=" * 100)
    print("Roll     Name            Course       Phone          Total    Paid     Due")
    print("=" * 100)
    for roll in students:
        s = students[roll]
        x = fees[roll]
        due = x["total_fee"] + x["fine"] - x["paid_fee"]
        print(roll.ljust(9) +
              s["name"].ljust(16) +
              s["course"].ljust(13) +
              s["phone"].ljust(15) +
              str(x["total_fee"]).ljust(9) +
              str(x["paid_fee"]).ljust(9) +
              str(due))
    print("=" * 100)


def search_student():
    keyword = input("Enter name to search: ").strip().lower()
    found = 0
    print("\n--- Search Results ---")
    for roll in students:
        if keyword in students[roll]["name"].lower():
            s = students[roll]
            print(roll + " - " + s["name"] + " - " + s["course"]
                  + " - " + s["phone"])
            found = found + 1
    if found == 0:
        print("❌ No matching students found.")


def update_student():
    roll = input("Enter Roll Number to update: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    s = students[roll]
    print("(Leave blank to keep current value)")

    new = input("Name (" + s["name"] + "): ").strip()
    if new != "":
        s["name"] = new

    new = input("Age (" + s["age"] + "): ").strip()
    if new != "":
        s["age"] = new

    new = input("Gender (" + s["gender"] + "): ").strip()
    if new != "":
        s["gender"] = new

    new = input("Course (" + s["course"] + "): ").strip()
    if new != "":
        s["course"] = new

    new = input("Phone (" + s["phone"] + "): ").strip()
    if new != "":
        s["phone"] = new

    new = input("Email (" + s["email"] + "): ").strip()
    if new != "":
        s["email"] = new

    print("✅ Student updated successfully!")


def delete_student():
    roll = input("Enter Roll Number to delete: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    name = students[roll]["name"]
    confirm = input("Delete " + name + "? (y/n): ").strip().lower()
    if confirm != "y":
        print("❌ Cancelled.")
        return

    del students[roll]
    if roll in fees:
        del fees[roll]
    if roll in marks:
        del marks[roll]
    if roll in attendance:
        del attendance[roll]

    print("🗑️ Student " + name + " and all related records deleted!")


def pay_fees():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    x = fees[roll]
    due = x["total_fee"] + x["fine"] - x["paid_fee"]
    print("\nStudent : " + students[roll]["name"])
    print("Total   : ₹" + str(x["total_fee"]))
    print("Fine    : ₹" + str(x["fine"]))
    print("Paid    : ₹" + str(x["paid_fee"]))
    print("Due     : ₹" + str(due))

    if due <= 0:
        print("🎉 No dues pending!")
        return

    amount = float(input("Enter Amount to Pay: "))
    if amount <= 0:
        print("❌ Invalid amount!")
        return
    if amount > due:
        print("❌ Amount exceeds due (₹" + str(due) + ")")
        return

    x["paid_fee"] = x["paid_fee"] + amount
    print("✅ Payment of ₹" + str(amount) + " successful!")
    print("   Remaining Due: ₹" + str(x["total_fee"] + x["fine"] - x["paid_fee"]))


def add_fine():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    x = fees[roll]
    print("Student: " + students[roll]["name"]
          + " | Current Fine: ₹" + str(x["fine"]))

    amount = float(input("Enter Fine Amount: "))
    if amount <= 0:
        print("❌ Invalid amount!")
        return

    reason = input("Reason (e.g. Late Fee): ").strip()
    x["fine"] = x["fine"] + amount
    print("⚠️ Fine of ₹" + str(amount) + " added for: " + reason)
    print("   Total Fine: ₹" + str(x["fine"]))


def clear_fine():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    x = fees[roll]
    if x["fine"] == 0:
        print("✅ No fine to clear!")
        return

    print("Current Fine: ₹" + str(x["fine"]))
    confirm = input("Clear fine? (y/n): ").strip().lower()
    if confirm == "y":
        x["fine"] = 0.0
        print("✅ Fine cleared for " + students[roll]["name"])


def add_marks():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    subject = input("Enter Subject: ").strip()
    m = float(input("Enter Marks (0-100): "))

    if m < 0 or m > 100:
        print("❌ Marks must be between 0 and 100!")
        return

    marks[roll][subject] = m
    print("✅ Marks added: " + subject + " = " + str(m))


def view_marks():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    if len(marks[roll]) == 0:
        print("📭 No marks recorded for " + students[roll]["name"])
        return

    print("\n--- Marks for " + students[roll]["name"] + " ---")
    total = 0
    count = 0
    for subject in marks[roll]:
        m = marks[roll][subject]
        print(subject.ljust(15) + ": " + str(m) + "  (" + get_grade(m) + ")")
        total = total + m
        count = count + 1

    avg = total / count
    print("-" * 30)
    print("Total   : " + str(total))
    print("Average : " + str(round(avg, 2)))
    print("Grade   : " + get_grade(avg))


def mark_attendance():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    a = attendance[roll]
    print("Mark today's attendance for " + students[roll]["name"])
    print("1. Present")
    print("2. Absent")
    choice = input("Choice (1/2): ").strip()

    if choice == "1":
        a["present"] = a["present"] + 1
        a["total"] = a["total"] + 1
        print("✅ Marked Present")
    elif choice == "2":
        a["absent"] = a["absent"] + 1
        a["total"] = a["total"] + 1
        print("⚠️ Marked Absent")
    else:
        print("❌ Invalid choice!")


def view_attendance():
    roll = input("Enter Roll Number: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return

    a = attendance[roll]
    if a["total"] == 0:
        print("📭 No attendance recorded for " + students[roll]["name"])
        return

    pct = (a["present"] / a["total"]) * 100
    print("\n--- Attendance for " + students[roll]["name"] + " ---")
    print("Present : " + str(a["present"]))
    print("Absent  : " + str(a["absent"]))
    print("Total   : " + str(a["total"]))
    print("Percent : " + str(round(pct, 2)) + "%")
    if pct >= 75:
        print("Status  : ✅ Good")
    else:
        print("Status  : ⚠️ Low (below 75%)")


def dashboard():
    total_collected = 0.0
    total_due = 0.0
    total_fine = 0.0

    for roll in fees:
        x = fees[roll]
        total_collected = total_collected + x["paid_fee"]
        total_due = total_due + (x["total_fee"] + x["fine"] - x["paid_fee"])
        total_fine = total_fine + x["fine"]

    print("\n========== DASHBOARD ==========")
    print("Total Students    : " + str(len(students)))
    print("Total Collected   : ₹" + str(total_collected))
    print("Total Due         : ₹" + str(total_due))
    print("Total Fine Issued : ₹" + str(total_fine))
    print("===============================")


def top_performers():
    if len(marks) == 0:
        print("📭 No marks recorded yet!")
        return

    ranking = []
    for roll in marks:
        if len(marks[roll]) == 0:
            continue
        total = 0
        for subject in marks[roll]:
            total = total + marks[roll][subject]
        avg = total / len(marks[roll])
        ranking.append((roll, students[roll]["name"], avg))

    if len(ranking) == 0:
        print("📭 No marks to rank!")
        return

    for i in range(len(ranking)):
        for j in range(len(ranking) - 1 - i):
            if ranking[j][2] < ranking[j + 1][2]:
                temp = ranking[j]
                ranking[j] = ranking[j + 1]
                ranking[j + 1] = temp

    print("\n========== TOP PERFORMERS ==========")
    rank = 1
    for r in ranking:
        print(str(rank) + ". " + r[1] + " (Roll " + r[0] + ") - Avg: "
              + str(round(r[2], 2)) + " - Grade: " + get_grade(r[2]))
        rank = rank + 1


def main():
    while True:
        print("\n========= STUDENT MANAGEMENT SYSTEM =========")
        print("1.  Add Student")
        print("2.  View Student Profile")
        print("3.  View All Students")
        print("4.  Search Student by Name")
        print("5.  Update Student")
        print("6.  Delete Student")
        print("7.  Pay Fees")
        print("8.  Add Fine")
        print("9.  Clear Fine")
        print("10. Add Marks")
        print("11. View Marks & Grade")
        print("12. Mark Attendance")
        print("13. View Attendance")
        print("14. Dashboard Summary")
        print("15. Top Performers")
        print("16. Exit")
        print("=============================================")

        choice = input("Enter your choice (1-16): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_student()
        elif choice == "3":
            view_all()
        elif choice == "4":
            search_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            delete_student()
        elif choice == "7":
            pay_fees()
        elif choice == "8":
            add_fine()
        elif choice == "9":
            clear_fine()
        elif choice == "10":
            add_marks()
        elif choice == "11":
            view_marks()
        elif choice == "12":
            mark_attendance()
        elif choice == "13":
            view_attendance()
        elif choice == "14":
            dashboard()
        elif choice == "15":
            top_performers()
        elif choice == "16":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Try again.")


main()