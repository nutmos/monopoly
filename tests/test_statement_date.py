from monopoly.banks.hsbc.credit import HsbcRevolution
from monopoly.banks.ocbc.credit import Ocbc365
from monopoly.banks.statement import Statement
from monopoly.pdf import PdfPage


def test_hsbc_statement_date_extraction(hsbc: HsbcRevolution, statement: Statement):
    page_content = "Statement From 21 JUL 2023 to 20 AUG 2023"

    statement.config.date_pattern = hsbc.statement_config.date_pattern
    statement.config.statement_date_format = hsbc.statement_config.statement_date_format

    statement.pages[0] = PdfPage(pix_map=None, raw_text=page_content, image=None)

    expected_date = "21 Jul 2023"
    statement_date = statement.statement_date

    assert statement_date is not None
    assert (
        statement_date.strftime(statement.config.statement_date_format) == expected_date
    )


def test_ocbc_statement_date_extraction(ocbc: Ocbc365, statement: Statement):
    page_content = "01-08-2023 24-08-2023 S$12,345 S$12,345 S$50.00"

    statement.config.date_pattern = ocbc.statement_config.date_pattern
    statement.config.statement_date_format = ocbc.statement_config.statement_date_format

    statement.pages[0] = PdfPage(pix_map=None, raw_text=page_content, image=None)

    expected_date = "01-08-2023"
    statement_date = statement.statement_date

    assert statement_date is not None
    assert (
        statement_date.strftime(statement.config.statement_date_format) == expected_date
    )