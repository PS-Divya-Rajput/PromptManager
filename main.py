from prompt import Prompt
from code_prompt import CodePrompt
from prompt_manager import PromptManager


def menu():
    print("         PromptVault")
    print("Choose which operation you want to perform!!")
    print("1. Add Prompt")
    print("2. View Prompts")
    print("3. Search Prompt")
    print("4. Edit Prompt")
    print("5. Delete Prompt")
    print("6. Toggle Favorite")
    print("7. Statistics")
    print("8. Exit")
    print("-" * 40)


def add_prompt(manager):
    print("\nSelect Prompt Type")
    print("1. Normal Prompt")
    print("2. Code Prompt")

    prompt_type = input("Choice: ").strip()

    title = input("Title: ").strip()
    category = input("Category: ").strip()
    ai_tool = input("AI Tool: ").strip()
    content = input("Content: ").strip()

    prompt_id = manager.generate_id()

    if prompt_type == "2":
        language = input("Programming Language: ").strip()

        prompt = CodePrompt(
            prompt_id,
            title,
            category,
            ai_tool,
            content,
            language,
        )

    else:
        prompt = Prompt(
            prompt_id,
            title,
            category,
            ai_tool,
            content,
        )

    manager.add_prompt(prompt)


def main():
    manager = PromptManager()

    while True:
        try:
            menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_prompt(manager)

            elif choice == "2":
                manager.view_prompts()

            elif choice == "3":
                keyword = input("Enter keyword to search: ").strip()
                manager.search_prompt(keyword)

            elif choice == "4":
                prompt_id = int(input("Enter Prompt ID: "))
                manager.edit_prompt(prompt_id)

            elif choice == "5":
                prompt_id = int(input("Enter Prompt ID: "))
                manager.delete_prompt(prompt_id)

            elif choice == "6":
                prompt_id = int(input("Enter Prompt ID: "))
                manager.toggle_favorite(prompt_id)

            elif choice == "7":
                manager.show_statistics()

            elif choice == "8":
                print("\nExiting PromptVault...")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

        except KeyboardInterrupt:
            print("\nProgram interrupted.")
            break


if __name__ == "__main__":
    main()