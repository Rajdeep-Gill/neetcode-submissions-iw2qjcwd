class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path + "/"
        dirs = path.split("/")
        print(dirs)
        for d in dirs:
            if d == "/" or d == "" or d == ".":
                continue
            if d == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(d)

        return "/" + "/".join(stack) + "" 