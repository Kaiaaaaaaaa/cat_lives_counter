import sys
import os

default_value = 9

def main():
    if len(sys.argv) < 2:
        print("Usage: python my_script.py [dec|reset]")
        return
    
    command = sys.argv[1].lower()
    file = "Life_counter.txt"

    if not os.path.exists(file):
        current_value = 9
    else:
        with open(file, "r") as f:
            file_content = f.read().strip()
            if file_content.isdigit():
                current_value = int(file_content)
            else:
                current_value = 9

    if command == "dec":
        current_value -= 1
        print("Subtracted one life... rip")
    elif command == "reset":
        current_value = 9
        print("Oki, reset the value to 9, a cat does indeed have 9 lives!")
    else:
        print(f"Unknown command: {command}, use 'dec' or 'reset'")
        return

    with open(file, "w") as f:
        f.write(str(current_value))
        print(f"Wrote to file {file} new value: {current_value}")


if __name__ == "__main__":
    main()