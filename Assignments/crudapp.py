import streamlit as st
import mysql.connector
import pandas as pd

# Database connection configuration
db_config = {
    'user': 'root',
    'password': 'root123',
    'host': 'localhost',
    'database': 'student_records',
}

# Create a connection to the database
cnx = mysql.connector.connect(**db_config)

# --- HEADER ---
st.title("🎓 Student Management System")
st.markdown("---")

# --- CREATE ---
def create_record():
    st.subheader("Add a New Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    major = st.text_input("Major")

    if st.button("Add Student"):
        if name and major:
            query = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
            values = (name, age, major)
            cursor = cnx.cursor()
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            st.success("Student added!!")
        else:
            st.warning("Please fill all fields")

# --- READ ---
def read_records():
    st.subheader("📊 Student Database")
    query = "SELECT * FROM students"
    data = pd.read_sql(query, cnx)
    st.dataframe(data)

# --- UPDATE ---
def update_record():
    st.subheader("✏️ Update Student")

    cursor = cnx.cursor()
    cursor.execute("SELECT id, name FROM students")
    records = cursor.fetchall()
    cursor.close()

    record_dict = {f"{id} - {name}": id for id, name in records}
    selected = st.selectbox("Select student", list(record_dict.keys()))

    if selected:
        record_id = record_dict[selected]

        cursor = cnx.cursor()
        cursor.execute("SELECT name, age, major FROM students WHERE id = %s", (record_id,))
        result = cursor.fetchone()
        cursor.close()

        name, age, major = result

        new_name = st.text_input("Name", value=name)
        new_age = st.number_input("Age", value=age)
        new_major = st.text_input("Major", value=major)

        if st.button("Update Student"):
            query = "UPDATE students SET name=%s, age=%s, major=%s WHERE id=%s"
            cursor = cnx.cursor()
            cursor.execute(query, (new_name, new_age, new_major, record_id))
            cnx.commit()
            cursor.close()
            st.success("✅ Student updated!")

# --- DELETE ---
def delete_record():
    st.subheader("🗑️ Delete Student")

    cursor = cnx.cursor()
    cursor.execute("SELECT id, name FROM students")
    records = cursor.fetchall()
    cursor.close()

    record_dict = {f"{id} - {name}": id for id, name in records}
    selected = st.selectbox("Select student to delete", list(record_dict.keys()))

    if selected:
        record_id = record_dict[selected]

        if st.button("Delete Student"):
            cursor = cnx.cursor()
            cursor.execute("DELETE FROM students WHERE id = %s", (record_id,))
            cnx.commit()
            cursor.close()
            st.warning("Deleted!")

# --- MAIN APP ---
def main():
    st.title("📌 Navigation")

    menu = ["Create", "Read", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        create_record()
    elif choice == "Read":
        read_records()
    elif choice == "Update":
        update_record()
    elif choice == "Delete":
        delete_record()

if __name__ == "__main__":
    main()

def get_data():
    query = "SELECT * FROM students;"
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = cursor.column_names
    cursor.close()
    return pd.DataFrame(result, columns=columns)

st.title("MySQL Data Viewer")

# Retrieve data from the database
data = get_data()

# Display data in a table
st.subheader("Data from MySQL Database")
st.dataframe(data)

# Close the database connection when the script ends
cnx.close()