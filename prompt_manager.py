import json
import os

from prompt import Prompt
from code_prompt import CodePrompt


class PromptManager:
    def __init__(self, filename="prompts.json"):
        self.filename = filename
        self.prompts = []
        self.next_id = 1
        self.load_prompts()

    def generate_id(self):
        current_id = self.next_id
        self.next_id += 1
        return current_id

    def add_prompt(self, prompt):

        for p in self.prompts:
            if p.get_title().lower() == prompt.get_title().lower():
                print("Prompt with this title already exists.")
                return

        self.prompts.append(prompt)
        #self.save_prompts()
        print("Prompt added successfully.")

    def view_prompts(self):

        if not self.prompts:
            print("\nNo prompts found.\n")
            return

        print("\nAll Prompts\n")

        for prompt in self.prompts:
            prompt.display()

    def search_prompt(self, keyword):

        found = False

        for prompt in self.prompts:

            if (
                keyword.lower() in prompt.get_title().lower()
                or keyword.lower() in prompt.get_category().lower()
                or keyword.lower() in prompt.get_ai_tool().lower()
                or keyword.lower() in prompt.get_content().lower()
            ):
                prompt.display()
                found = True

        if not found:
            print("No matching prompt found.")

    def edit_prompt(self, prompt_id):

        for prompt in self.prompts:

            if prompt.get_id() == prompt_id:
                title = input(
                    f"New Title ({prompt.get_title()}): "
                ).strip()
                category = input(
                    f"New Category ({prompt.get_category()}): "
                ).strip()
                ai_tool = input(
                    f"New AI Tool ({prompt.get_ai_tool()}): "
                ).strip()
                content = input(
                    f"New Content ({prompt.get_content()}): "
                ).strip()
                if title:
                    prompt.set_title(title)
                if category:
                    prompt.set_category(category)
                if ai_tool:
                    prompt.set_ai_tool(ai_tool)
                if content:
                    prompt.set_content(content)

                if isinstance(prompt, CodePrompt):

                    language = input(
                        f"New Language ({prompt.get_language()}): "
                    ).strip()

                    if language:
                        prompt.set_language(language)

                #self.save_prompts()

                print("Prompt updated successfully.")
                return

        print("Prompt not found.")

    def delete_prompt(self, prompt_id):

        for prompt in self.prompts:

            if prompt.get_id() == prompt_id:
                self.prompts.remove(prompt)
                self.save_prompts()
                print("Prompt deleted successfully.")
                return

        print("Prompt not found.")

    def toggle_favorite(self, prompt_id):

        for prompt in self.prompts:

            if prompt.get_id() == prompt_id:

                prompt.toggle_favorite()

                self.save_prompts()

                print("Favorite status updated.")
                return

        print("Prompt not found.")

    def show_statistics(self):

        total = len(self.prompts)

        favorites = 0

        categories = {}

        for prompt in self.prompts:

            if prompt.is_favorite():
                favorites += 1

            category = prompt.get_category()

            categories[category] = categories.get(category, 0) + 1

        print("\nStatistics")
        print("-" * 30)
        print(f"Total Prompts     : {total}")
        print(f"Favorite Prompts  : {favorites}")
        print(f"Total Categories  : {len(categories)}")

        print("\nPrompts by Category")

        for category, count in categories.items():
            print(f"{category} : {count}")

    def save_prompts(self):

        data = []

        for prompt in self.prompts:
            data.append(prompt.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_prompts(self):

        if not os.path.exists(self.filename):
            return

        with open(self.filename, "r") as file:

            try:
                data = json.load(file)

                for item in data:

                    if item["type"] == "CodePrompt":
                        prompt = CodePrompt.from_dict(item)

                    else:
                        prompt = Prompt.from_dict(item)

                    self.prompts.append(prompt)

                if self.prompts:
                    self.next_id = (
                        max(prompt.get_id() for prompt in self.prompts) + 1
                    )

            except json.JSONDecodeError:
                self.prompts = []