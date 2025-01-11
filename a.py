from linebot import LineBotApi

line_bot_api = LineBotApi("your_line_channel_access_token")
print("LINE Bot SDK installed and ready!")


import pymysql

try:
    # Update with your database credentials
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="teaching_assistant",
    )
    print("Database connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")
finally:
    connection.close()
