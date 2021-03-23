import pytest
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):
    # Set up test case data
    PHRASE = 'panda'

    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE


def test_basic_duckduckgo_search_not_case(browser):
    # Set up test case data
    PHRASE = 'panda'
    FAIL_PHRASE = 'bat'

    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert not result_page.phrase_result_count(FAIL_PHRASE) > 0
    assert not result_page.search_input_value() == FAIL_PHRASE


def test_basic_duckduckgo_search_fail_case(browser):
    # Set up test case data
    PHRASE = 'panda'
    FAIL_PHRASE = 'bat'

    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(FAIL_PHRASE) <= 0
    assert result_page.search_input_value() == FAIL_PHRASE


@pytest.mark.parametrize(
    "PASS_PHRASE, FAIL_PHRASE",
    [('kangaroo', 'koala'),
     ('John', 'Paul'),
     ('Lennon', 'Paul'),
     ('Drake', 'Josh'),
     ('selenium', 'bdd'),
     ('bach', 'bhrams'),
     ('duoling', 'language'),
     ('treno', 'trena'),
     ('onça', 'git'),])
def test_multiple_searches(browser, PASS_PHRASE, FAIL_PHRASE):
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PASS_PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0

    assert result_page.phrase_result_count(PASS_PHRASE) > 0
    assert result_page.search_input_value() == PASS_PHRASE


@pytest.mark.parametrize(
    "PASS_PHRASE, FAIL_PHRASE",
    [('kangaroo', 'koala'),
     ('John', 'Paul'),
     ('Lennon', 'Paul'),
     ('Drake', 'Josh'),
     ('selenium', 'bdd'),
     ('bach', 'bhrams'),
     ('duoling', 'language'),
     ('treno', 'trena'),
     ('onça', 'git'), ])
def test_multiple_searches(browser, PASS_PHRASE, FAIL_PHRASE):
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PASS_PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert not result_page.phrase_result_count(FAIL_PHRASE) > 0
    assert not result_page.search_input_value() == FAIL_PHRASE


@pytest.mark.parametrize(
    "PASS_PHRASE, FAIL_PHRASE",
    [('kangaroo', 'koala'),
     ('John', 'Paul'),
     ('Lennon', 'Paul'),
     ('Drake', 'Josh'),
     ('selenium', 'bdd'),
     ('bach', 'bhrams'),
     ('duoling', 'language'),
     ('treno', 'trena'),
     ('onça', 'git'), ])
def test_multiple_searches(browser, PASS_PHRASE, FAIL_PHRASE):
    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PASS_PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(FAIL_PHRASE) <= 0
    assert result_page.search_input_value() == FAIL_PHRASE