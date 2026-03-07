import os
from dotenv import load_dotenv

load_dotenv()

def setup_database():
    try:
        import mysql.connector
        
        # Connect without database
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=int(os.getenv('DB_PORT', 3306)),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', 'password')
        )
        cursor = conn.cursor()
        
        # Create database
        db_name = os.getenv('DB_NAME', 'tweet_generator')
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        
        # Create campaigns table
        create_table = """
        CREATE TABLE IF NOT EXISTS campaigns (
            id INT AUTO_INCREMENT PRIMARY KEY,
            brand_name VARCHAR(255) NOT NULL,
            response LONGTEXT,
            input_data JSON,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table)
        conn.commit()
        
        print("✅ Database setup complete")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"❌ Database setup error: {e}")

if __name__ == '__main__':
    setup_database()
