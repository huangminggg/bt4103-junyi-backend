from internal.db.db import db_instance


def create_group(name):
    pic = 'e0309575@u.nus.edu'
    query = f'''
    INSERT INTO groups 
    (name, created_by, created_at, updated_by, updated_at) 
    VALUES 
    ({name}, {pic}, NOW(), {pic}, NOW())
    '''
    res = db_instance.exec_transaction(query)
    return res


def get_group(id):
    res = db_instance.fetch_row("SELECT * FROM groups WHERE id = %s AND deleted_at IS NULL", (id,))
    return res


def get_groups():
    res = db_instance.fetch_rows("SELECT * FROM groups WHERE deleted_at IS NULL")
    return res
