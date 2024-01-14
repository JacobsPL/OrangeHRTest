import mysql.connector

class DataFactory:

    def __init__(self, driver):
        super().__init__()  # Call the constructor of the BaseTest class
        self.driver = driver

    def create_connection(host_name, user_name, user_password):
        connection = None

        try:
            connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password
            )

            print("Connection to DB successful")

        except OSError as e:
            print(f"ERROR occured: '{e}' ")

        return connection

    def execute_read_query(connection, query):
        cursor = connection.cursor()

        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

        except OSError as e:
            print(f"ERROR occured: '{e}' ")

    def get_all_users(self):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users"
        users = self.execute_read_query(connection, select_user)
        return users

    def get_user_by_id(self,id):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE id = " + str(id)
        user = self.execute_read_query(connection, select_user)
        return user[0]

    def get_user_by_user_name(self,user_name):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE user_name = " + str(user_name)
        user = self.execute_read_query(connection, select_user)
        return user[0]

    def get_users_by_user_role(self,user_role):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE user_name = " + str(user_role)
        users = self.execute_read_query(connection, select_user)
        users

    def get_users_employee_name(self,employee_name):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE user_name = " + str(employee_name)
        users = self.execute_read_query(connection, select_user)
        return users

    def get_users_status(self,status):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE user_name = " + str(status)
        users = self.execute_read_query(connection, select_user)
        return users

    def get_username_from_record(self, user):
        return(user[0])

    def get_user_role_from_record(self, user):
        return(user[1])

    def get_employee_name_from_record(self, user):
        return(user[2])

    def get_status_from_record(self, user):
        return(user[3])

    def get_password_from_record(self, user):
        return(user[4])

    def get_role_option(self,role):
        if role == "Admin":
            return 1
        else:
            return 2
    def get_status_option(self,status):
        if status == "Enabled":
            return 1
        else:
            return 2