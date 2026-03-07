import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host = os.getenv('DB_HOST', 'localhost')
        self.port = int(os.getenv('DB_PORT', 3306))
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', 'password')
        self.database = os.getenv('DB_NAME', 'tweet_generator')
        self.conn = None
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                autocommit=True
            )
            print(f"✅ Connected to database: {self.database}")
        except Exception as e:
            print(f"⚠️  Database connection failed: {e}")
            print(f"   Database will be optional (tweets can be generated without storage)")
            raise

    def save_campaign(self, brand_name, response, input_data):
        try:
            if not self.conn:
                return None
            cursor = self.conn.cursor()
            import json
            query = """
            INSERT INTO campaigns (brand_name, response, input_data)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (brand_name, response, json.dumps(input_data)))
            self.conn.commit()
            campaign_id = cursor.lastrowid
            cursor.close()
            return campaign_id
        except Exception as e:
            print(f"Error saving campaign: {e}")
            return None

    def get_campaign(self, campaign_id):
        try:
            if not self.conn:
                return None
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM campaigns WHERE id = %s"
            cursor.execute(query, (campaign_id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print(f"Error fetching campaign: {e}")
            return None

    def get_all_campaigns(self):
        try:
            if not self.conn:
                return []
            cursor = self.conn.cursor(dictionary=True)
            query = "SELECT * FROM campaigns ORDER BY created_at DESC LIMIT 50"
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print(f"Error fetching campaigns: {e}")
            return []

    def close(self):
        if self.conn:
            self.conn.close()
