import uuid
import datetime
import psycopg2
from config import postgres, uuid_namespace
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
    i = 1

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

        if value is not None:

            date = datetime.datetime.now().strftime("%Y-%m-%d")

            # # ! TESTING
            # date = datetime.datetime.now() + datetime.timedelta(days=2)
            # date = date.strftime("%Y-%m-%d")
            # # ! TESTING

            uuid_name = listing_id + date + vendor

            price_id = str(uuid.uuid5(uuid.UUID(uuid_namespace), uuid_name))

            try:

                # Create price entry
                cursor.execute(
                    'INSERT INTO prices ("id", "value", "date", "listingId") VALUES(%s, %s, %s, %s)',
                    (price_id, value, date, listing_id),
                )

                connection.commit()

            except Exception as e:

                print(e)

        print(f"{i}/{len(rows)} = {value}")

        i += 1

    cursor.close()

# Handle error
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

# Close connection
finally:
    if connection is not None:
        connection.close()
