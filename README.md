# Automated flashcards in Notion
Welcome to the project. It is basically the integration between Python and Notion for creating flashcards. 

## How to start?
1. Get a Notion account (if you do not have one).
2. Navigate to [the integration page](https://www.notion.so/my-integrations).
3. Click `Create new integration` and specify a name. (Note that you will get the `NOTION_TOKEN` from this step).
4. Navigate to the [flashcards template ](https://www.notion.so/templates/vocabulary-tracker-language-learning).
5. Click `Get this template`.
6. Click the hamburger icon to `copy the link to view` at the table in the flashcards template.
7. Get `DATABASE_ID` from the link, given that the Notion's link is of the format `https://www.notion.so/{DATABASE_ID}?v={something_else}`.
8. Preapre `.env` file for your `NOTION_TOKEN` and `DATABASE_ID`.
9. Install [`poetry`](https://python-poetry.org).
10. Clone this repo.
```zsh
git clone https://github.com/pakhapoom/automated-flashcards.git
```
11. Enjoy reading!

# Motivation
## Why Notion?
A friend of mine recommended me to use [Notion](https://www.notion.so) because it is very flexible and we can do everything in there. "**What limits us in the Notion is basically our imagination,**" he said.

Until now, I just have some good quality time to ideate a certain use case. I feel like there are sooooooo many words that I do not know thier meaning(s) when reading a book (my new habit, apparently). I, finally, found [this useful guide](https://www.notion.so/templates/vocabulary-tracker-language-learning) for creating flashcards in Notion. And I have adopted it to help me memorize those new vocabulary.

## Why flashcards?
It is fun for me to do flashcards and it really helped me memorize something as well. So, I think their magic is still working for sure! (It is also unbelievable for me that Notion support spaced-repetition system!)

## Why automated?
I cannot tolerate with those tasks, like looking the meaning and record everything in notion. Besides, there are [some python scripts]((https://www.python-engineer.com/posts/notion-api-python/)) to connect the Notion from Python that were developed by Patrick Loeber. You may see scripts in `notion_automation/utils.py` are quite familiar because I copied everything from there to use as basic operations for the Notion's connection.

Moreover, the translation part is done by using the [Wiktionary API](https://en.wiktionary.org/api/rest_v1/#/Page%20content/get_page_definition__term_). Thank you for your generiousity.
