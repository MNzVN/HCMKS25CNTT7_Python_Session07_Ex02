transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "
transaction = transaction.strip()
parts = transaction.split("|")
student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount_raw = parts[2].strip()
status = parts[3].strip().upper()
amount_numeric = int(amount_raw)
amount_formatted = f"{amount_numeric:,} VND"
print(f"Học viên: {student_name}")
print(f"Khóa học: {course_code}")
print(f"Số tiền: {amount_formatted}")
print(f"Trạng thái: {status}")