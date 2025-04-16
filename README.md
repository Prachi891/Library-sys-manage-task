
Library Management System 

This is a simple Library Management System built using Django. The system allows you to manage Authors, Books, and Borrow Records.
Users can add authors, add books, and record borrow transactions through user-friendly forms. Additionally, data can be exported to 
Excel for further processing or record-keeping.

Features:

1.Add Author Form

2.Add Book Form

3.Borrow Book Form

4.Data Pagination

5.Export to Excel functionality (for Authors, Books, and Borrow Records) 

# 
Admin login details
  Username: Prachi
  Email: prachi@gmail.com
  Password: 12345 

  # 
  How to Run:
  
  1.Clone the repository using git clone https://github.com/your-username/your-repo-name.git
  
  2.Install dependencies using pip install -r requirements.txt
  
  3 .Run migrations using:

  python manage.py makemigrations
  python manage.py migrate
   4.Start the server using python manage.py runserver 
   
   Open your browser and go to http://127.0.0.1:8000/admin/ and log in with the provided admin credentials.

Export to Excel: Click on the "Export" button available on each list page (Author, Book, Borrow) to download the data in Excel format.



