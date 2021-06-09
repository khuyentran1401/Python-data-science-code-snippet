# pip install notion

from notion.client import NotionClient
from notion.block import NumberedListBlock

client = NotionClient("<token_v2>")

page = client.get_block("https://www.notion.so/Error-shooting-How-to-3c1904c9869b47118b8656df8b2f8d11")

print(page.title)
# Error shooting / How to

page.title = "How to / Error shooting"

print(page.title)
# How to / Error shooting

for child in page.children:
    print(child.title)

"""
Linux
Changes to the system
Hydra
Python
WordPress
"""

new = page.children.add_new(
    NumberedListBlock, title='Item 1'
)

for child in page.children:
    print(child.title)

"""
Linux
Changes to the system
Hydra
Python
WordPress
Item 1
"""



