import random
from rich.console import Console
from rich.panel import Panel
import json

console = Console()

def load_facts(filename="facts.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        console.print("[red]Error:[/] 'facts.json' file not found.")
        return []

def shuffle_facts(facts):
    random.shuffle(facts)
    return facts

def display_fact(fact):
    panel = Panel(
        fact["text"],
        title=f"🧠 Did You Know? [{fact.get('category', 'General')}]",
        subtitle="Press [Enter] to continue or type 'q' to quit",
        style="bold cyan",
        border_style="magenta"
    )
    console.print(panel)

def main():
    facts = load_facts()
    if not facts:
        return

    facts = shuffle_facts(facts)
    index = 0

    console.print("[bold green]🎉 Welcome to the Fun Fact Generator! 🎉[/bold green]\n")

    while index < len(facts):
        display_fact(facts[index])
        user_input = input()
        if user_input.strip().lower() == 'q':
            console.print("\n[bold yellow]👋 Goodbye! Hope you learned something new today![/bold yellow]")
            break
        index += 1

    if index == len(facts):
        console.print("\n[bold blue]You've read all the facts! Restart to enjoy again.[/bold blue]")

if __name__ == "__main__":
    main()

