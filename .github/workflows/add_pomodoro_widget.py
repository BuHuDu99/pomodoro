import os
from notion_client import Client

# Authenticate using your Notion API key
notion = Client(auth=os.environ["NOTION_API_KEY"])

# Set the ID of the database where you want to add the Pomodoro widget
database_id = os.environ["DATABASE_ID"]

# Create a new page in the database
new_page = {
    "Name": {
        "title": [
            {
                "text": {
                    "content": "Pomodoro Widget"
                }
            }
        ]
    },
    "Pomodoro": {
        "type": "embed",
        "embed": {
            "url": "https://pomofocus.io/embed/",
            "height": 600,
            "full_width": True
        }
    }
}
created_page = notion.pages.create(parent={"database_id": database_id}, properties=new_page)

print("Pomodoro widget added
