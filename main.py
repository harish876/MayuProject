
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()


def display_landing_page():
    # Title and team members info
    landing_text = Text()
    landing_text.append("Hospital Management System\n\n", style="bold")
    landing_text.append("Team Members:\n\n", style="bold cyan")
    landing_text.append("1. Dr. Alice Smith - Lead Developer\n", style="white")
    landing_text.append("2. John Doe - Backend Engineer\n", style="white")
    landing_text.append("3. Jane Roe - Frontend Designer\n", style="white")
    landing_text.append("4. Emily Davis - Project Manager\n", style="white")

    # Create a panel for the landing page
    landing_panel = Panel(
        landing_text,
        title="Welcome",
        title_align="center",
        border_style="bold magenta",
        padding=(1, 2),
        expand=True,
        subtitle_align='center'
    )

    # Display the panel
    console.print(landing_panel)

    # Prompt to proceed
    console.print(
        "\n[bold green]Press Enter to proceed to the main menu...[/bold green]")
    console.input()  # Wait for user input


def display_main_menu():
    # Create a table for the menu
    console.clear()
    table = Table(title="[bold]Hospital Management System",
                  title_justify="center", padding=(1, 2))
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")

    table.add_row("1", "Select a Hospital To Visit")
    table.add_row("2", "Select a Department To Visit")
    table.add_row("0", "Exit")

    # Center the table in the terminal
    console.print(Panel(table, title="Main Menu", subtitle="Select an option",
                  title_align="center", subtitle_align="center", padding=(1, 1), border_style="bold green"))


def main():
    display_landing_page()
    display_main_menu()
    choice = console.input(
        "[bold green]Enter your choice:[/bold green] ").strip()

    # Handle user choice
    if choice == "0":
        console.print("Exiting...", style="bold red")
    elif choice == "1":
        console.print("Managing Patients...")
    elif choice == "2":
        console.print("Scheduling Appointments...")
    elif choice == "3":
        console.print("Handling Billing...")
    elif choice == "4":
        console.print("Generating Reports...")
    else:
        console.print("[bold red]Invalid option. Please try again.[/bold red]")


if __name__ == "__main__":
    main()
