from database.connect import connect_to_database


async def url_for_new_ad(id_user: int) -> list:
    conn = await connect_to_database()

    result = await conn.fetch("SELECT url FROM users_data WHERE id_user = $1", id_user)

    await conn.close()

    return result


async def read_data_for_old_users() -> list:
    conn = await connect_to_database()

    result = await conn.fetch("SELECT id_user, id_ad, url FROM users_data WHERE url IS NOT NULL")

    await conn.close()

    return result

