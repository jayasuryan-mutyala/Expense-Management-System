import mysql.connector
from contextlib import contextmanager 
from backend.logging_setup import setup_logger
import logging 
import os 
from dotenv import load_dotenv

# os.path.abspath(__file__): returns the full path of the files location in directory
# not os.getcwd() will return root directory so we can't use it

logger = setup_logger(name="db_helper",
                      log_file_name='server.log',
                      level=logging.DEBUG)

load_dotenv()


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )

    cursor = connection.cursor(dictionary=True)
    yield cursor 

    if commit:
        connection.commit()
    print("Closing server")

    cursor.close()
    connection.close()    

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses")
        expenses = cursor.fetchall()

        # for expense in expenses:
        #     print(expense)
        return expenses
            
def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date=%s",(expense_date,))
        expenses = cursor.fetchall()

        # for expense in expenses:
        #     print(expense)
        return expenses
    
def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expenses called with date:{expense_date}, amount:{amount}, category:{category}, notes:{notes}")
    
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("insert into expenses (expense_date,amount,category,notes) values (%s, %s, %s, %s)",
                       (expense_date,amount,category,notes))
        
def delete_expense(expense_date):
    logger.info(f"delete_expense for date:{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date=%s",(expense_date,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch_expense_summary called with start date:{start_date} end date:{end_date}")
    
    with get_db_cursor() as cursor:
        cursor.execute("""
        select category,sum(amount) as total 
        from expenses where expense_date
        between %s and %s
        group by category;""",
        (start_date,end_date))
    
        summary = cursor.fetchall()
    return summary

def fetch_total_monthly_expense():
    logger.info(f"fetching total monthly expenses")
    
    query = """
    SELECT 
        DATE_FORMAT(expense_date, '%M %Y') AS month,
        SUM(amount) AS total_expense
    FROM expenses
    GROUP BY 
        YEAR(expense_date),
        MONTH(expense_date),
        DATE_FORMAT(expense_date, '%M %Y')
    ORDER BY 
    YEAR(expense_date),
    MONTH(expense_date);
    """
    
    with get_db_cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()

    return result

def fetch_categories():
    logger.info(f"Fetching all categories")

    query = """
        SELECT DISTINCT category as category FROM expenses
        ORDER BY category
    """
    with get_db_cursor() as cursor:

        cursor.execute(query)
        results = cursor.fetchall()

    return results

def fetch_expense_by_category(category):
    logger.info(f"Fetching total expenses by category:{category}")

    query = """
        SELECT category,SUM(amount) as total_expense 
        FROM expenses WHERE category = %s
        GROUP BY category;
    """

    with get_db_cursor() as cursor:
        cursor.execute(query,(category,))
        result = cursor.fetchall()

    return result

def fetch_total_expense_by_category():
    query = """
        SELECT category,SUM(amount) as total_expense
        FROM expenses GROUP BY category
        ORDER BY total_expense DESC
    """

    with get_db_cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    
    return results

if __name__ == "__main__":
    test = fetch_categories()
    print(test)