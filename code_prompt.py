from prompt import Prompt


class CodePrompt(Prompt):
    def __init__(self, prompt_id, title, category, ai_tool, content, language, favorite=False):
        super().__init__(
            prompt_id,
            title,
            category,
            ai_tool,
            content,
            favorite
        )
        self.__language = language

    def get_language(self):
        return self.__language

    def set_language(self, language):
        self.__language = language

    def display(self):
        super().display()
        print(f"Language   : {self.__language}")
        print("-" * 40)

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "CodePrompt"
        data["language"] = self.__language
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["category"],
            data["ai_tool"],
            data["content"],
            data["language"],
            data.get("favorite", False)
        )