class Prompt:
    def __init__(self, prompt_id, title, category, ai_tool, content, favorite=False):
        self.__id = prompt_id
        self.__title = title
        self.__category = category
        self.__ai_tool = ai_tool
        self.__content = content
        self.__favorite = favorite

    # Getters
    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_category(self):
        return self.__category

    def get_ai_tool(self):
        return self.__ai_tool

    def get_content(self):
        return self.__content

    def is_favorite(self):
        return self.__favorite

    # Setters
    def set_title(self, title):
        self.__title = title

    def set_category(self, category):
        self.__category = category

    def set_ai_tool(self, ai_tool):
        self.__ai_tool = ai_tool

    def set_content(self, content):
        self.__content = content

    def toggle_favorite(self):
        self.__favorite = not self.__favorite

    def display(self):
        print("-" * 40)
        print(f"ID         : {self.__id}")
        print(f"Title      : {self.__title}")
        print(f"Category   : {self.__category}")
        print(f"AI Tool    : {self.__ai_tool}")
        print(f"Content    : {self.__content}")
        print(f"Favorite   : {'Yes' if self.__favorite else 'No'}")
        print("-" * 40)

    def to_dict(self):
        return {
            "type": "Prompt",
            "id": self.__id,
            "title": self.__title,
            "category": self.__category,
            "ai_tool": self.__ai_tool,
            "content": self.__content,
            "favorite": self.__favorite
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["category"],
            data["ai_tool"],
            data["content"],
            data.get("favorite", False)
        )