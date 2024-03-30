import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="4972",
    database="project"
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Function to insert data into the table
def insert_data():
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    roll_no = int(input("Enter Roll No: "))
    phone_no = int(input("Enter Phone No: "))
    email_id = input("Enter Email ID: ")
    gender = input("Enter Gender: ")
    country = input("Enter Country: ")

    # Insert data into the table
    query = "INSERT INTO data1 (Name, Branch, Roll_No, Phone_No, Email_id, Gender, Country) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    values = (name, branch, roll_no, phone_no, email_id, gender, country)
    cursor.execute(query, values)
    connection.commit()
    print("Data inserted successfully")

# Function to update data in the table
def update_data():
    roll_no = int(input("Enter Roll No of the record to update: "))
    phone_no = int(input("Enter new Phone No: "))
    email_id = input("Enter new Email ID: ")

    # Update data in the table
    query = "UPDATE data1 SET Phone_No = %s, Email_id = %s WHERE Roll_No = %s"
    values = (phone_no, email_id, roll_no)
    cursor.execute(query, values)
    connection.commit()
    print("Data updated successfully")

# Main menu
while True:
    print("\nMain Menu:")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_data()
    elif choice == 2:
        update_data()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please enter a valid option.")

# Close the cursor and connection
cursor.close()
connection.close()
