# import: standard
from typing import Dict
from typing import List
from typing import Union

# import: internal
from notion_automation.vocab import WordLookup

# import: external
import pytest

BASE_API = "https://en.wiktionary.org/api/rest_v1/page/definition"
MAX_DEFINITIONS = 3
DICT_DATATYPE = Dict[str, Union[str, List[str]]]
OUTPUT_DICT_DATATYPE = Dict[str, Dict[str, List[Dict[str, Dict[str, str]]]]]


@pytest.fixture
def word_lookup():
    return WordLookup()


def test_lookup_word():
    # TODO: implement test with request
    pass


def test_get_pos(word_lookup):
    input_data = {"partOfSpeech": "Noun"}
    result = word_lookup.get_pos(input_data)
    assert result == "Noun"


@pytest.mark.parametrize(
    "html_text, normal_text",
    [
        (
            'A <a rel="mw:WikiLink" href="/wiki/challenge#Noun" title="challenge">challenge</a>, <a rel="mw:WikiLink" href="/wiki/trial" title="trial">trial</a>.',
            "A challenge, trial.",
        ),
        (
            '<span class="usage-label-sense" about="#mwt25" typeof="mw:Transclusion"></span> A <a rel="mw:WikiLink" href="/wiki/Test_match" title="Test match">Test match</a>.',
            "A Test match.",
        ),
    ],
)
def test_clean_text(word_lookup, html_text, normal_text):
    result = word_lookup.clean_text(html_text)
    assert result == normal_text


def test_process_definitions(word_lookup):
    input_data = {
        "definitions": [
            {"definition": "<br> A large body of water.</br>"},
            {"definition": "<em> A vast expanse.</em>"},
            {"definition": "An overwhelming amount."},
            {"definition": "A unit of measure."},
        ]
    }
    expected_defs = [
        "A large body of water.",
        "A vast expanse.",
        "An overwhelming amount.",
    ]

    result = word_lookup.process_definitions(input_data)
    assert result == expected_defs


def test_combine_definitions(word_lookup):
    input_data = [
        "A challenge, trial.",
        "A Test match.",
    ]
    expected = input_data[0] + "\n" + input_data[1]
    assert word_lookup.combine_definitions(input_data, "\n") == expected


def test_get_basic_input_dict(word_lookup):
    data = {
        "vocab": "word_ex",
        "definition": "def_ex",
        "pos": "pos_ex",
        "example": "example_ex",
        "synonym": "synonym_ex",
    }
    result = word_lookup.get_basic_input_dict(**data)
    assert result == data


def test_prepare_input(word_lookup):
    vocab = "example"
    definition = "A representative instance."
    pos = "noun"
    example = "This code provides an example of testing."
    synonym = "instance, illustration"

    expected = {
        "Vocab": {"title": [{"text": {"content": "example"}}]},
        "Definition": {
            "rich_text": [{"text": {"content": "A representative instance."}}]
        },
        "Part of Speech": {"multi_select": [{"name": "noun"}]},
        "Example Sentence": {
            "rich_text": [
                {"text": {"content": "This code provides an example of testing."}}
            ]
        },
        "Similar Words": {"rich_text": [{"text": {"content": "instance, illustration"}}]},
    }

    result = word_lookup.prepare_input(vocab, definition, pos, example, synonym)
    assert result == expected


def get_word_info():
    # TODO: implement test with request
    pass
