# 🎓 Student Record Management System

A comprehensive command-line student management system built with Python. This application enables educational institutions to efficiently manage student records with full CRUD operations, input validation, and persistent storage.

## ✨ Features

- **Add Students**: Register new students with complete validation
- **View Records**: Display all student records in a well-formatted table
- **Update Records**: Modify existing student information
- **Delete Records**: Remove students from the system
- **Input Validation**: Comprehensive validation for all user inputs
- **Unique Roll Numbers**: Automatic checking to prevent duplicate roll numbers
- **Persistent Storage**: All data stored in text file for persistence
- **User-Friendly Interface**: Clean CLI with emoji indicators and clear messages

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/zain-cs/Student-Management-System.git
cd student-management-system
```

2. Run the program:
```bash
python student_management.py
```

## 📖 Usage

When you run the program, you'll see an interactive menu:

```
========================================
  STUDENT RECORD MANAGEMENT SYSTEM
========================================
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Exit
----------------------------------------
```

### Adding a Student

Choose option 1 and provide the following information:
- **Student Name**: Letters, spaces, and hyphens only
- **Father's Name**: Letters, spaces, and hyphens only
- **Roll Number**: Unique numeric identifier
- **Degree Program**: Choose from BSCS, BSSE, BSIT, BBA
- **Grade**: A, B, C, D, E, or F

**Example:**
```
Enter student name: Ali Hassan
Enter father's name: Hassan Ahmed
Enter roll number: 12345
Enter degree (BSCS, BSSE, BSIT, BBA): BSCS
Enter grade (A, B, C, D, E, F): A
```

### Viewing Students

Choose option 2 to display all student records in a formatted table:

```
Name                 Father Name          Roll No    Degree   Grade
----------------------------------------------------------------------
Ali Hassan           Hassan Ahmed         12345      BSCS     A
Sara Khan            Khan Ahmed           12346      BSSE     B
```

### Updating a Student

Choose option 3, enter the roll number, and provide updated information. All fields are validated before saving.

### Deleting a Student

Choose option 4 and enter the roll number of the student you want to remove from the system.

## 🔧 Input Validation

The system includes comprehensive validation:

- ✅ **Names**: Only letters, spaces, and hyphens allowed
- ✅ **Roll Numbers**: Numeric values only, must be unique
- ✅ **Degree Programs**: Must be one of: BSCS, BSSE, BSIT, BBA
- ✅ **Grades**: Must be one of: A, B, C, D, E, F
- ✅ **Menu Input**: Validates numeric choices between 1-5

## 📁 Data Storage

All student records are stored in `students.txt` in the following format:
```
Name, Father Name, Roll Number, Degree, Grade
```

**Example:**
```
Ali Hassan, Hassan Ahmed, 12345, BSCS, A
Sara Khan, Khan Ahmed, 12346, BSSE, B
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Libraries Used**: 
  - `re` (Regular expressions for input validation)
- **File Handling**: Text file-based storage system
- **Architecture**: Modular function-based design with comprehensive error handling

## 🎯 Code Structure

```
student_management.py
├── Configuration
│   ├── VALID_DEGREES        # List of accepted degree programs
│   ├── VALID_GRADES         # List of accepted grades
│   └── STUDENT_FILE         # Data file path
├── Validation Functions
│   ├── is_valid_name()      # Validates names
│   ├── is_valid_roll_no()   # Validates roll numbers
│   ├── is_valid_degree()    # Validates degree programs
│   ├── is_valid_grade()     # Validates grades
│   └── is_roll_no_unique()  # Checks for duplicate roll numbers
├── CRUD Operations
│   ├── add_student()        # Adds new student records
│   ├── view_students()      # Displays all students
│   ├── update_student()     # Updates existing records
│   └── delete_student()     # Deletes student records
└── main()                   # Main program loop
```

## 💡 Key Features Explained

### Smart Validation
- All inputs are validated before processing
- Case-insensitive degree and grade inputs (automatically converted to uppercase)
- Real-time feedback with emoji indicators (✅ ❌ ⚠️)

### Error Handling
- Handles missing files gracefully
- Validates data format and structure
- Provides clear error messages
- Transaction safety (changes only saved if validation passes)

### User Experience
- Clean, organized interface
- Consistent formatting
- Helpful prompts and messages
- Safe exit option

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] Add search functionality (by name, roll number, degree)
- [ ] Generate student reports and statistics
- [ ] Export data to CSV/Excel
- [ ] Add student attendance tracking
- [ ] Implement GPA calculation
- [ ] Add course enrollment management
- [ ] Create GUI interface
- [ ] Implement database storage (SQLite/MySQL)
- [ ] Add user authentication for admin access
- [ ] Generate student ID cards

## 🎓 Supported Degree Programs

- **BSCS** - Bachelor of Science in Computer Science
- **BSSE** - Bachelor of Science in Software Engineering
- **BSIT** - Bachelor of Science in Information Technology
- **BBA** - Bachelor of Business Administration

## 📊 Grade System

- **A** - Excellent
- **B** - Very Good
- **C** - Good
- **D** - Satisfactory
- **E** - Pass
- **F** - Fail

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Zain**
- GitHub: [@zain-cs](https://github.com/zain-cs)

## 🙏 Acknowledgments

- Thanks to the Python community for excellent documentation
- Inspired by the need for simple educational management solutions
- Built for learning and practical application

---

⭐ **If you find this project useful, please consider giving it a star!**

📧 **For questions or suggestions, feel free to open an issue or reach out!**
