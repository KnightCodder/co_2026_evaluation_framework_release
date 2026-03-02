class AssemblerError(Exception):
    def __init__(self, message, line_no=None):
        if line_no is not None:
            super().__init__(f"Error at line {line_no}: {message}")
        else:
            super().__init__(f"Error: {message}")
