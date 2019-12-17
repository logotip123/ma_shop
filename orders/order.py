"""Order CRD realisation"""

import datetime
import psycopg2
from products import products
from errors import errors


def create(conn, id_product, id_user):
    """
    Add order to orders table
    :param conn: connection
    :param id_product: id of product
    :param id_user: id of user
    :return: None
    """
    with conn.cursor() as cursor:
        price = products.get_product_price(conn, id_product)
        current_date = datetime.date.today()
        cursor.execute(f"""insert into orders
            (id, id_product, price, date) values ('{id_user}', '{id_product}','{price}','{current_date}')""")
        conn.commit()


def get(conn, id_order):
    """
    Get order from orders table
    :param conn:
    :param id_order:
    :return:
    """
    with conn.cursor() as cursor:
        cursor.execute(f"""select id, id_user, id_product, price, date 
                                from orders where id='{id_order}'""")
        try:
            return cursor.fecthone()
        except TypeError:
            raise errors.StoreError


def delete_order(conn, id_order):
    """
    Delete order
    :param conn: connection
    :param id_order: id of order
    :return:
    """
    with conn.cursor() as cursor:
        row_count = cursor.rowcount
        if row_count < 0:
            raise errors.StoreError
        else:
            cursor.execute(f"delete from orders where id='{id_order}'")