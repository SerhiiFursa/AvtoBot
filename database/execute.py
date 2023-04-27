from database.connect import connect_to_database


async def insert_update_data(data: list = None):
    conn = await connect_to_database()

    query = '''
            INSERT INTO users_data (
            id_user, mark, model, transmission, year_min, year_max, mileage_min, mileage_max, price_min, price_max, url
            )
            VALUES (
            $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11
            )
            ON CONFLICT (id_user) DO UPDATE SET mark = $2, model = $3, transmission = $4, year_min = $5, year_max = $6, 
            mileage_min = $7, mileage_max = $8, price_min = $9, price_max = $10, url = $11
        '''

    id_user = data[0]
    mark = data[1]
    model = data[2]
    transmission = data[3]
    year_min = data[4]
    year_max = data[5]
    mileage_min = data[6]
    mileage_max = data[7]
    price_min = data[8]
    price_max = data[9]
    url = data[10]

    await conn.execute(
        query, id_user, mark, model, transmission, year_min, year_max,
        mileage_min, mileage_max, price_min, price_max, url
    )
    await conn.close()


async def update_id_ad(data: list = None):
    conn = await connect_to_database()

    id_user = data[0]
    id_ad = data[1]

    await conn.execute(
        "UPDATE users_data SET id_ad = CAST($1 AS bigint) WHERE id_user = CAST($2 AS bigint)",
        id_ad,
        id_user
    )
    await conn.close()


async def clear_cell(id_user):
    conn = await connect_to_database()

    await conn.execute("UPDATE users_data SET url = NULL WHERE id_user = $1", id_user)
    await conn.close()

