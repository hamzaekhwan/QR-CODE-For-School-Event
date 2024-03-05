Overview
This project is a backend system designed for managing attendance at school events using QR codes. It leverages Django and its REST framework to create a secure and efficient attendance management system. The system generates unique QR codes for each student, allowing them to attend events by simply scanning their QR code.

Features
QR Code Generation: Generates unique QR codes for each student.
Attendance Tracking: Tracks attendance by scanning QR codes.
Arabic Text Support: Supports Arabic text rendering for QR codes.
Data Export: Exports attendance data in various formats.
Technologies Used
Django: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
Django REST Framework: A powerful and flexible toolkit for building Web APIs.
QR Code Generation: Uses the qrcode library for generating QR codes.
Image Manipulation: Utilizes PIL for image manipulation.
Arabic Text Support: Implements arabic_reshaper and bidi for Arabic text support.
Data Export: Uses tablib for data export.
Getting Started
Prerequisites
Python 3.x
Django
Django REST Framework
QR Code library
PIL (Pillow)
Arabic Reshaper
Bidi algorithm
Tablib
Installation
Clone the repository:
git clone https://github.com/hamzaekhwan/qr-code-for-school-event.git
Navigate to the project directory:
cd qr-code-for-school-event
Install the required packages:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Start the development server:
python manage.py runserver
Usage
Generate QR Codes: Use the provided API endpoints to generate QR codes for students.
Track Attendance: Scan the QR codes at the event to track attendance.
Export Attendance Data: Export attendance data in various formats using the provided endpoints.
Contributing
Contributions are welcome. Please feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

This template provides a basic structure for your README file. You can expand on each section to include more detailed information about your project, such as screenshots, code examples, and specific instructions for contributors.
