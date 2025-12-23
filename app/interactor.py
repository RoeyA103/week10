import mysql.connector
from mysql.connector import errorcode

def get_cnx() -> None:
    try:
        cnx = mysql.connector.connect(user='root', password='pass',
                                    host='127.0.0.1',
                                    port=3306,
                                    database='contacts_db')
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

        contact = contact.dict()
        
        cursor = self.cnx.cursor()
        try:
            for key ,val in contact.items():
                if val is None: 
                    continue
                sql = f"UPDATE contacts SET `{key}` = %s WHERE id = %s"
                cursor.execute(sql, (val, contact_id))
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
            self.cnx.commit()
            return "The contact was successfully deleted"
        except mysql.connector.Error as err:
            self.cnx.rollback()  
            return err             

        finally:
            cursor.close()
     
