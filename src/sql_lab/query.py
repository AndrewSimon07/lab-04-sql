import logging
import os

import mysql.connector


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DB_HOST = os.getenv("DBHOST")
DB_NAME = os.getenv("DBNAME")
DB_USER = os.getenv("DBUSER")
DB_PASSWORD = os.getenv("DBPASS")

db = mysql.connector.connect(user=DB_USER, host=DB_HOST, password=DB_PASSWORD, database=DB_NAME)
cur = db.cursor()

def get_data_by_group(value):
    """Return mock rows whose group matches value"""
    query = "SELECT * FROM mock WHERE `group` = %s;"
    try:
        cur.execute(query, (value,))
        results = cur.fetchall()
        output = []
        for r in results:
            output.append(r)
        logger.info("Returned Rows Sucessfully")
        return output
    except mysql.connector.Error as e:
        logger.error("MySQL Error: %s", str(e))
        return None

def plot_counts(groupby):
    """Return counts of rows grouped by column."""
    query = f"SELECT `{groupby}`, COUNT(*) FROM mock GROUP BY `{groupby}`;"

    try:
        cur.execute(query)
        results = cur.fetchall()
        logger.info("Retrieved counts grouped by %s", groupby)
        return results

    except mysql.connector.Error as e:
        logger.error("MySQL Error: %s", str(e))
        return None

def main():
    """Actually run functions with examples"""
    print(get_data_by_group("apples"))
    print(plot_counts("color"))
    logger.info("Info gathered successfully")

if __name__ == "__main__":
    main()
