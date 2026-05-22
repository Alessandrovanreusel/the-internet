class BasePage:
    def __init__(self, page):
        self.page = page
    
    def visit(self, path:str):
        self.page.goto(path)