import mysql.connector
from AdminCreateUserPage import AdminCreateUserPage
from time import sleep

class DataFactory:

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

    def create_initial_users(self):
        create_user_page = AdminCreateUserPage
        users = self.get_all_users()
        create_user_page.loginAndGoToCreateUserPage()

        for i in users:
            create_user_page.getUserRoleDropDown().click()
            if self.get_user_role_from_record(i)=="Admin":
                create_user_page.get_dropdown_option(1).click()
            else:
                create_user_page.get_dropdown_option(2).click()

            create_user_page.getStatusDropDown().click()
            if self.get_status_from_record(i) == "Enabled":
                create_user_page.get_dropdown_option(1).click()
            else:
                create_user_page.get_dropdown_option(2).click()

            employee_name = self.get_employee_name_from_record(i)
            create_user_page.get_employee_name().send_keys(i)
            sleep(1)
            create_user_page.get_dropdown_option(0).click()

            user_name = self.get_user_name_from_record(i)
            create_user_page.get_username_input().sent_keys(user_name)

            password = self.get_password_from_record(i)
            create_user_page.get_password_input().sent_keys(password)
            create_user_page.get_confirm_password_input().sent_keys(password)

    def get_all_users(self):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users"
        users = self.execute_read_query(connection, select_user)
        return users

    def get_user_by_id(self,id):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE id = " + str(id)
        user = self.execute_read_query(connection, select_user)
        return user

    def get_user_by_user_name(self,user_name):
        connection = self.create_connection("localhost", "root", "haslo")
        select_user = "SELECT * FROM OrangeHR.users WHERE user_name = " + str(user_name)
        user = self.execute_read_query(connection, select_user)
        return user

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

    def get_user_name_from_record(self, user):
        print(user[0][0])

    def get_user_role_from_record(self, user):
        print(user[0][1])

    def get_employee_name_from_record(self, user):
        print(user[0][2])

    def get_status_from_record(self, user):
        print(user[0][3])

    def get_password_from_record(self, user):
        print(user[0][4])




# data_factory = DataFactory
# connection = data_factory.create_connection("localhost", "root", "haslo")
# select_users = "SELECT * FROM OrangeHR.users WHERE id = 1"
# polisy = data_factory.execute_read_query(connection, select_users)
# print(polisy)

deta = DataFactory
deta.get_user_role_from_record(deta,deta.get_user_by_id(deta,1))