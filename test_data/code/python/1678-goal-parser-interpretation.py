class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                result += command[i]
                i += 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+3] == "(al)":
                result += "al"
                i += 3
        return result