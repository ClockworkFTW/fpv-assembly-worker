import datetime
import psycopg2
from uuid import uuid4
from config import postgres
from vendors import getfpv, pyrodrone, racedayquads


connection = None

try:

    # Connect to PostgreSQL server
    connection = psycopg2.connect(
        database=postgres["database"],
        user=postgres["user"],
        password=postgres["password"],
        host=postgres["host"],
        port=postgres["port"],
    )

    # Get all listings
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM listings")
    rows = cursor.fetchall()

    # Get price for each listing
    for row in rows:

        listing_id = row[0]
        vendor = row[1]
        url = row[2]

        value = None

        if vendor == "getfpv":
            value = getfpv.getPrice(url)

        if vendor == "pyrodrone":
            value = pyrodrone.getPrice(url)

        if vendor == "racedayquads":
            value = racedayquads.getPrice(url)

        price_id = str(uuid4())

        now = datetime.datetime.now()

        created_at = now
        updated_at = now

        # Create price entry
        cursor.execute(
            'INSERT INTO prices ("id", "value", "createdAt", "updatedAt", "listingId") VALUES(%s, %s, %s, %s, %s)',
            (price_id, value, created_at, updated_at, listing_id),
        )

        connection.commit()

    cursor.close()

# Handle error
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# Close connection
finally:
    if connection is not None:
        connection.close()
