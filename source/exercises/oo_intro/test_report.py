"""
test code for the Report class(es)
"""

from report import Row, Report


def populate_report(report):
    """
    utility function to populate a Report with some data

    :param report: the report object to populate

    The Report will be populated in place
    """
    report.add_row(Row("Natasha", "Smith", "WA"))
    report.add_row(Row("Devin", "Lei", "WA"))
    report.add_row(Row("Bob", "Li", "CA"))
    report.add_row(Row("Tracy", "Jones", "OR"))
    report.add_row(Row("Johnny", "Jakes", "WA"))
    report.add_row(Row("Derek", "Wright", "WA"))
    report.add_row(Row("Jordan", "Cooper", "WA"))
    report.add_row(Row("Mike", "Wong", "WA"))


def test_row_init():
    """You can initialize a Row, and it stores the attributes"""

    row1 = Row("Joe", "Camel", "WA")

    assert row1.fname == "Joe"
    assert row1.lname == "Camel"
    assert row1.state == "WA"


def test_row_id_unique():
    """ two Rows should have unique IDs """
    row1 = Row("Joe", "Camel", "WA")
    row2 = Row("Bob", "Camel", "WA")

    assert row1.id != row2.id


def test_report_length():
    report = Report(4)
    populate_report(report)

    # the test data has 8 rows
    assert report.size() == 8

