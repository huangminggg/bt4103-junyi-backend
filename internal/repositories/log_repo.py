from internal.db.db import db_instance


def get_logs_by_user(user_list):
    res = db_instance.fetch_rows(f"SELECT * FROM logs WHERE ucid in ({user_list})")
    return res


def get_logs_by_module(module_list):
    module_list = ', '.join([f"({i})" for i in module_list])
    query = f"""
                SELECT l.id, l.upid, u.cluster, l.ucid, l.uuid, l.attempt_timestamp, l.problem_number, l.exercise_problem_repeat_session, l.is_correct, 
                        l.total_sec_taken, l.total_attempt_cnt, l.used_hint_cnt, l.is_hint_used, l.is_downgrade, l.is_upgrade, l.user_level
                FROM logs l
                LEFT JOIN contents c 
                ON l.ucid = c.id
                LEFT JOIN algorithm_cache u
                ON l.uuid = u.uuid
                WHERE 
                c.level3_id IN ({module_list})
                ORDER BY l.attempt_timestamp
            """
    res = db_instance.fetch_rows(query)
    return res
