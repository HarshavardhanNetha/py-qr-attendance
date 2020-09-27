# Attendance Made Easy | Python | QR | py-qr-attendance
## Aim: This project aims to use technology to the fullest to make it ease and to reduce the errors in the process of "Attendance".

### Technologies Used: Python, openCV, QR(Quick Response Code), Google Sheets and Google Drive APIs

Step 1: We generate QR codes using the Excel sheet (from local storage, which has ID and email of candidate), which decodes to be their ID.
The generated QR codes will be mailed to the respective candidate.

Step 2: We run our 2nd program to take input via camera (opencv), and ask the students to show their qr codes to the camera. When a valid input is detected, a beeb sound comes, in the backend, we append the data we get into a temporary list.

Step 3: After all students show their codes, we process the list and add attendance to an online spreadsheet.

Note: This repo may not contain all required files like JSON file which we use to interact with google spreadsheet in step 3.

Feel free to reach me at linkedin.com/in/harsha-netha for any queries.

### References
QR: https://note.nkmk.me/en/python-pillow-qrcode/
open pyxl: https://www.youtube.com/watch?v=AOTCpZbC80Y
Sending Mail: https://www.youtube.com/watch?v=bXRYJEKjqIM
OpenCV: https://www.youtube.com/watch?v=SrZuwM705yE
		https://www.youtube.com/watch?v=-4MPtERPq2E

Spread Sheets: https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
Google APIs: https://console.developers.google.com/apis
Gspread Module: https://gspread.readthedocs.io/en/latest/user-guide.html
