
from openupgradelib import openupgrade


def set_company_id_to_1_where_null(env):
    env.cr.execute("""
        select table_name 
        from information_schema.columns 
        where column_name = 'company_id'
        and table_name not in (select table_name from information_schema.views)
        ;
        """)
    table_names = [t[0] for t in env.cr.fetchall()]
    for table_name in table_names:
        sql = "update {} set company_id = 1 where company_id is null;".format(table_name)
        env.cr.execute(sql)



@openupgrade.migrate()
def migrate(env, version):
    set_company_id_to_1_where_null(env)
