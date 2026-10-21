
#!/usr/bin/env python3
import sys
def generate(message):
    source = []
    previous = 0
    for char in message:
        value = ord(char) % 256
        diff = value - previous

        if diff > 0:
            source.extend(["uh"] * diff)
        elif diff < 0:
            source.extend(["hm"] * (-diff))
        source.append("ah")
        previous = value
    return " ".join(source)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <text>", file=sys.stderr)
        sys.exit(1)
    message = " ".join(sys.argv[1:])
    print(generate(message))
if __name__ == "__main__":
    main()
