import sys
from taxonomy import Taxonomy

def test_read_edinet_ifrs():
    tax = Taxonomy()
    tax.load('../2023/1g_IFRS_ElementList.xlsx')

def test_read_edinet_jp_gaap():
    tax = Taxonomy()
    tax.load('../2023/1f_AccountList.xlsx')
