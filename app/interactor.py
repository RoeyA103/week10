import mysql.connector
from mysql.connector import errorcode
import os
from schemas import *


def get_cnx():
    try:
        cnx = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=3306,
    )
        return cnx

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)


class DataInteractor:
    def __init__(self):
        self.cnx = get_cnx()

    def get_contacts(self)-> list:
        cursor = self.cnx.cursor(dictionary=True)

        result = cursor.execute("select * from contacts")

        rows = cursor.fetchall()

        cursor.close()    

        return rows
    
  

    def create_new_contact(self, contact) -> str:
        cursor = self.cnx.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO contacts (first_name, last_name, phone_number)
                VALUES (%s, %s, %s)
                """,
                (contact.first_name, contact.last_name, contact.phone_number)
            )
            self.cnx.commit()

            new_id = cursor.lastrowid

            return { "message":"The contact was successfully updated" , "id":new_id}
        except mysql.connector.Error as err:
            self.cnx.rollback()  
            return err             

        finally:
            cursor.close()

    def update_contact(self,contact_id:int,contact:ContactUpdate)->str:

        contact = contact.model_dump()
        
        cursor = self.cnx.cursor()
        try:
            fields = []
            values = []

            for key, val in contact.items():
                if val is not None:
                    fields.append(f"`{key}` = %s")
                    values.append(val)

            if not fields:
                return "Nothing to update"

            sql = f"""
                UPDATE contacts
                SET {', '.join(fields)}
                WHERE id = %s
            """

            values.append(contact_id)
            cursor.execute(sql, tuple(values))

            if cursor.rowcount == 0:
                self.cnx.rollback()
                return "No contact found with this ID"

            self.cnx.commit()
            return "The contact was successfully updated"

        except mysql.connector.Error as err:
            self.cnx.rollback()
            return err

        finally:
            cursor.close()



    def del_contact(self,contact_id:int)->str:
        cursor = self.cnx.cursor()
        try:
            sql = "DELETE FROM contacts WHERE id = %s"
            cursor.execute(sql,(contact_id,))

            if cursor.rowcount == 0:
                self.cnx.rollback()
                return "No contact found with this ID"
            
            self.cnx.commit()
            return "The contact was successfully deleted"
        
        except mysql.connector.Error as err:
            self.cnx.rollback()  
            return err             

        finally:
            cursor.close()
     
