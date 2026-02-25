class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)
        while i < n:
            if path[i] == '/':
                i += 1
                continue
            j = i
            while j < n and path[j] != '/':
                j += 1
            part = path[i:j]
            if part == '..':
                if stack:
                    stack.pop()
            elif part != '.':
                stack.append(part)
            i = j
        return '/' + '/'.join(stack)