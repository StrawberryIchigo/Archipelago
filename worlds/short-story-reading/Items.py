from typing import NamedTuple
from BaseClasses import ItemClassification

class ItemData(NamedTuple):
    code: int
    classification: ItemClassification
    link: str = None

story_sources = {
    "Short Stories You Own": ItemData(1, ItemClassification.progression),
    "Short Stories in Your Library": ItemData(2, ItemClassification.progression),
    "Project Gutenberg": ItemData(3, ItemClassification.progression,
                                  "https://www.gutenberg.org/"),
    "Uncanny Magazine": ItemData(4, ItemClassification.progression,
                                 "https://www.uncannymagazine.com/"),
    "Strange Horizons": ItemData(5, ItemClassification.progression,
                                 "http://strangehorizons.com/"),
    "Reactor": ItemData(6, ItemClassification.progression,
                        "https://reactormag.com/"),
    "Clarkesworld Magazine": ItemData(7, ItemClassification.progression,
                             "https://clarkesworldmagazine.com/"),
    "Lightspeed Magazine": ItemData(8, ItemClassification.progression,
                                    "https://www.lightspeedmagazine.com/"),
    "Escape Pod": ItemData(9, ItemClassification.progression,
                           "https://escapepod.org/"),
}