import functools
import os

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask import current_app
from flask.cli import with_appcontext

from markupsafe import escape


import sqlite3
import pandas

bp = Blueprint('reporting', __name__, url_prefix='/reporting')

TEST_DATABASE_NAME='dmdma_test_db.sqlite'

def beautify_html_table(html_table : str, table_id :str = 'exportMe', center_headings : bool = True):
    """Apply common formatting to the pandas created HTML,including an ID for javascript manipulation """

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html_table, "html.parser")
    soup.find('table')['id'] = table_id
    soup.find('table')['class'] = 'table table-striped table-hover table-sm'
    soup.find('thead')['class'] = 'thead-dark'

    soup.find('tr')['style'] = None

    if center_headings:
        for si in soup.find_all('th'):
            si['class'] = 'text-center'

    #html_output = soup.prettify()
    html_output = str(soup)
    return html_output

@with_appcontext
@bp.route('/')
def home():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    return render_template('reporting/home.html')

@with_appcontext
@bp.route('/reset_db')
def reset_db():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    TEST_DATABASE = os.path.join(current_app.instance_path, TEST_DATABASE_NAME)

    db = sqlite3.connect(
            TEST_DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    with current_app.open_resource('data/reporting/testing_schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    show_tables_sql = "SELECT name FROM sqlite_master WHERE type='table';"

    pandas_result_set = pandas.read_sql_query(show_tables_sql, db)
    pandas_resultset_html = pandas_result_set.to_html(index = False)

    beautiful_html_table = beautify_html_table(pandas_resultset_html)

    if db is not None:
        db.close

    return render_template('reporting/reset_db.html', table=beautiful_html_table)

@with_appcontext
@bp.route('/pivot_sample')
def pivot_sample():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    TEST_DATABASE = os.path.join(current_app.instance_path, TEST_DATABASE_NAME)

    db = sqlite3.connect(
            TEST_DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    get_data_sql = "SELECT * FROM testing;"
    pandas_result_set = pandas.read_sql_query(get_data_sql, db)

    beautiful_html_table = beautify_html_table(pandas_result_set.to_html(index = False))

    pandas_resultset_json = pandas_result_set.to_json(orient = 'records')

    if db is not None:
        db.close

    return render_template('reporting/pivot.html', table=beautiful_html_table, json_data=pandas_resultset_json)

@with_appcontext
@bp.route('/dynamic_sample_1')
def dynamic_sample_1():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    TEST_DATABASE = os.path.join(current_app.instance_path, TEST_DATABASE_NAME)

    db = sqlite3.connect(
            TEST_DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    from . import item

    get_data_sql = "SELECT * FROM testing;"

    report_part_1 = item.item(title='Testing report 1')
    report_part_1.htmlTableID = 'rep_1'
    report_part_1.introText = '<p>This goes before the table</p>'
    report_part_1.introTextIsHTML = True
    report_part_1.outroText = 'This goes after the table'
    report_part_1.dataFrame = pandas.read_sql_query(get_data_sql, db)
    report_part_1.htmlTable = beautify_html_table(report_part_1.dataFrame.to_html(index = False),
                                                  table_id = report_part_1.htmlTableID
                                                  )


    get_data_sql = "SELECT * FROM testing_2;"

    report_part_2 = item.item(title='Testing report 2',
                                    dataFrame = pandas.read_sql_query(get_data_sql, db),
                                    )
    report_part_2.htmlTable = beautify_html_table(report_part_2.dataFrame.to_html(index = False),
                                                  table_id = report_part_2.htmlTableID
                                                  )


    report_page_title = 'Testing Reports'
    reporting_table_sets = [report_part_1,
                            report_part_2
                           ]

    return render_template('reporting/reporting_items.html',
                           report_page_title = report_page_title,
                           reporting_table_sets = reporting_table_sets
                           )

@with_appcontext
@bp.route('/dynamic_sample_2')
def dynamic_sample_2():
    # Redirect to login if no user logged in
    # ToDo: Add logic to see if user has access to application
    if g.user is None:
        return redirect(url_for('auth.login'))

    TEST_DATABASE = os.path.join(current_app.instance_path, TEST_DATABASE_NAME)

    db = sqlite3.connect(
            TEST_DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )

    from . import item

    get_data_sql = "SELECT value_2, SUM(metric_1) AS metric_1_sum FROM testing GROUP BY value_2;"

    report_part_1 = item.item(title='Aggregate Report',
                                    dataFrame = pandas.read_sql_query(get_data_sql, db),
                                    )
    report_part_1.convertToBeautifulHTML()


    report_page_title = 'Testing Reports 2'
    reporting_table_sets = [report_part_1
                           ]

    return render_template('reporting/reporting_items.html',
                           report_page_title = report_page_title,
                           reporting_table_sets = reporting_table_sets
                           )

if __name__ == '__main__':
    pass