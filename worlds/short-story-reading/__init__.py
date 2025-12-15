from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

class ShortStoryReadingWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide for setting up the Short Story Reading Challenge in a Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["StrawberryIchigo"]
    )]

    theme = "stone"

class ShortStoryReadingWorld(World):
    """
    Encourage yourself to read more short fiction!
    Collect sources of freely-available short stories, and read them to fulfil randomised prompts.
    """

    game = "Short Story Reading Challenge"
    webWorld = ShortStoryReadingWebWorld()