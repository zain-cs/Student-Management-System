import re

VALID_DEGREES = ['BSCS', 'BSSE', 'BSIT', 'BBA']
VALID_GRADES = ['A', 'B', 'C', 'D', 'E', 'F']
STUDENT_FILE = 'students.txt'

def is_valid_name(name):
    return bool(name.strip() and re.match(r'^[A-Za-z\s-]+$', name))

def is_valid_roll_no(roll_no):
    return bool(roll_no.strip() and roll_no.isdigit())

def is_valid_degree(degree):
    return degree.strip().upper() in VALID_DEGREES

def is_valid_grade(grade):
    return grade.strip().upper() in VALID_GRADES

def is_roll_no_unique(roll_no):
    try:
        with open(STUDENT_FILE, 'r') as file:
            for line in file:
                fields = line.strip().split(", ")
                if len(fields) >= 3 and fields[2] == roll_no:
                    return False
        return True
    except FileNotFoundError:
        return True

def add_student():
    """Add a new student record."""
    print("\n--- Add New Student ---")
    
    name = input("Enter student name (letters, spaces, or hyphens only): ").strip()
    if not is_valid_name(name):
        print("❌ Error: Invalid name. Use letters, spaces, or hyphens only.")
        return
    
    father_name = input("Enter father's name (letters, spaces, or hyphens only): ").strip()
    if not is_valid_name(father_name):
        print("❌ Error: Invalid father's name. Use letters, spaces, or hyphens only.")
        return
    
    roll_no = input("Enter roll number (numeric only): ").strip()
    if not is_valid_roll_no(roll_no):
        print("❌ Error: Roll number must be numeric only.")
        return
    
    if not is_roll_no_unique(roll_no):
        print("❌ Error: Roll number already exists. Please use a unique roll number.")
        return
    
    degree = input(f"Enter degree ({', '.join(VALID_DEGREES)}): ").strip().upper()
    if not is_valid_degree(degree):
        print(f"❌ Error: Invalid degree. Please choose from: {', '.join(VALID_DEGREES)}")
        return
    
    grade = input(f"Enter grade ({', '.join(VALID_GRADES)}): ").strip().upper()
    if not is_valid_grade(grade):
        print(f"❌ Error: Invalid grade. Please choose from: {', '.join(VALID_GRADES)}")
        return
    
    try:
        with open(STUDENT_FILE, 'a') as file:
            file.write(f"{name}, {father_name}, {roll_no}, {degree}, {grade}\n")
        print("✅ Student record added successfully!")
    except Exception as e:
        print(f"❌ Error saving record: {e}")

def view_students():
    print("\n--- Student Records ---")
    
    try:
        with open(STUDENT_FILE, 'r') as file:
            lines = file.readlines()
            
        if not lines or all(not line.strip() for line in lines):
            print("No records found. Please add students first.")
            return
        
        print(f"{'Name':<20} {'Father Name':<20} {'Roll No':<10} {'Degree':<8} {'Grade':<5}")
        print("-" * 70)
        
        for line in lines:
            if not line.strip():
                continue
            
            parts = line.strip().split(", ")
            if len(parts) != 5:
                print(f"⚠️  Skipping invalid line: {line.strip()}")
                continue
            
            name, father_name, roll_no, degree, grade = parts
            print(f"{name:<20} {father_name:<20} {roll_no:<10} {degree:<8} {grade:<5}")
        
    except FileNotFoundError:
        print("No records found. Please add students first.")

def update_student():
    print("\n--- Update Student ---")
    
    target_roll_no = input("Enter roll number of student to update: ").strip()
    
    try:
        with open(STUDENT_FILE, 'r') as file:
            lines = file.readlines()
        
        new_lines = []
        updated = False
        
        for line in lines:
            parts = line.strip().split(", ")
            
            if len(parts) != 5:
                new_lines.append(line)
                continue
            
            name, father_name, roll_no, degree, grade = parts
            
            if roll_no == target_roll_no:
                print(f"\nCurrent record: {name}, {father_name}, {degree}, {grade}")
                print("Enter updated details:")
                
                new_name = input("Enter updated name: ").strip()
                if not is_valid_name(new_name):
                    print("❌ Error: Invalid name. Update cancelled.")
                    return
                
                new_father_name = input("Enter updated father's name: ").strip()
                if not is_valid_name(new_father_name):
                    print("❌ Error: Invalid father's name. Update cancelled.")
                    return
                
                new_degree = input(f"Enter updated degree ({', '.join(VALID_DEGREES)}): ").strip().upper()
                if not is_valid_degree(new_degree):
                    print(f"❌ Error: Invalid degree. Update cancelled.")
                    return
                
                new_grade = input(f"Enter updated grade ({', '.join(VALID_GRADES)}): ").strip().upper()
                if not is_valid_grade(new_grade):
                    print(f"❌ Error: Invalid grade. Update cancelled.")
                    return
                
                new_line = f"{new_name}, {new_father_name}, {roll_no}, {new_degree}, {new_grade}\n"
                new_lines.append(new_line)
                updated = True
            else:
                new_lines.append(line)
        
        if updated:
            with open(STUDENT_FILE, 'w') as file:
                file.writelines(new_lines)
            print("✅ Student record updated successfully!")
        else:
            print("❌ Roll number not found.")
    
    except FileNotFoundError:
        print("❌ No records found.")

def delete_student():
    print("\n--- Delete Student ---")
    
    target_roll_no = input("Enter roll number of student to delete: ").strip()
    
    try:
        with open(STUDENT_FILE, 'r') as file:
            lines = file.readlines()
        
        new_lines = []
        found = False
        
        for line in lines:
            parts = line.strip().split(", ")
            
            if len(parts) == 5 and parts[2] == target_roll_no:
                found = True
                continue
            
            new_lines.append(line)
        
        if found:
            with open(STUDENT_FILE, 'w') as file:
                file.writelines(new_lines)
            print("✅ Student record deleted successfully!")
        else:
            print("❌ No student found with this roll number.")
    
    except FileNotFoundError:
        print("❌ No records found.")

def main():
    while True:
        print("\n" + "=" * 40)
        print("  STUDENT RECORD MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("-" * 40)
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                add_student()
            elif choice == 2:
                view_students()
            elif choice == 3:
                update_student()
            elif choice == 4:
                delete_student()
            elif choice == 5:
                print("\n👋 Thank you for using the Student Management System!")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 5.")
        
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()