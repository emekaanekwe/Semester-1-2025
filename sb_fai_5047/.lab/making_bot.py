class vscode_run:
    def __init__(self, agent: str, busy: bool, copies: int):
        self.a = agent
        self.b = busy
        self.c = copies

tri = vscode_run("wyatt", True, 1)

print(tri.a, tri.c)

