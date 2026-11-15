#!/usr/bin/env python3
import sys, subprocess

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(1)
    # Handle 'bash -c "command"'
    if args[0] == '-c':
        # join the remaining args into a single string
        cmd = ' '.join(args[1:])
        result = subprocess.run(['sh', '-c', cmd])
        sys.exit(result.returncode)
    # Otherwise, try to exec the command directly
    try:
        result = subprocess.run(args)
        sys.exit(result.returncode)
    except FileNotFoundError:
        print(f"bash: {args[0]}: command not found", file=sys.stderr)
        sys.exit(127)

if __name__ == "__main__":
    main()

