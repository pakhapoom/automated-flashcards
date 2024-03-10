# import: standard
import re
from typing import Dict
from typing import List
from typing import Union

# import: external
import requests

BASE_API = "https://en.wiktionary.org/api/rest_v1/page/definition"
MAX_DEFINITIONS = 3
DICT_DATATYPE = Dict[str, Union[str, List[str]]]
OUTPUT_DICT_DATATYPE = Dict[str, Dict[str, List[Dict[str, Dict[str, str]]]]]


class WordLookup:
    @staticmethod
    def lookup_word(word) -> DICT_DATATYPE:
        resp = requests.get(f"{BASE_API}/{word}")

        # select the first english definition only.
        description = resp.json()["en"][0]

        return description

    @staticmethod
    def get_pos(description: DICT_DATATYPE) -> str:
        return description["partOfSpeech"]

    @staticmethod
    def clean_text(text: str) -> str:
        # remove html tags.
        clean_text = re.sub(r"<.*?>", "", text)

        # remove leading and trailing spaces.
        clean_text = clean_text.strip()
        return clean_text

    def process_definitions(self, description: DICT_DATATYPE) -> List[str]:
        definitions = description["definitions"]

        # limit the maximum number of definitions.
        if len(definitions) > MAX_DEFINITIONS:
            definitions = definitions[:MAX_DEFINITIONS]

        # clean each definition.
        new_defs = [
            self.clean_text(definition["definition"]) for definition in definitions
        ]

        return new_defs

    @staticmethod
    def combine_definitions(
        definitions: List[str],
        separator: str = "\n",
    ) -> str:
        return f"{separator}".join(definitions)

    @staticmethod
    def get_basic_input_dict(
        vocab: str,
        definition: str,
        pos: str,
        example: str = "",
        synonym: str = "",
    ) -> Dict[str, str]:

        # TODO: implement the processes to get `example` and `synonym`.

        return {
            "vocab": vocab,
            "definition": definition,
            "pos": pos,
            "example": example,
            "synonym": synonym,
        }

    @staticmethod
    def prepare_input(
        vocab: str,
        definition: str,
        pos: str,
        example: str,
        synonym: str,
    ) -> OUTPUT_DICT_DATATYPE:
        data = {
            "Vocab": {"title": [{"text": {"content": vocab}}]},
            "Definition": {"rich_text": [{"text": {"content": definition}}]},
            "Part of Speech": {"multi_select": [{"name": pos}]},
            "Example Sentence": {"rich_text": [{"text": {"content": example}}]},
            "Similar Words": {"rich_text": [{"text": {"content": synonym}}]},
        }

        return data

    def get_word_info(self, word: str) -> OUTPUT_DICT_DATATYPE:
        description = self.lookup_word(word)
        pos = self.get_pos(description)
        definitions = self.process_definitions(description)
        definitions_str = self.combine_definitions(definitions)

        # TODO: implement the processes to get `example` and `synonym`.
        input_dict = self.get_basic_input_dict(
            vocab=word,
            definition=definitions_str,
            pos=pos,
        )
        input_dict = self.prepare_input(**input_dict)

        return input_dict
