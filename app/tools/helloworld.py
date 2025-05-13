from app.base.base_tool import BaseTool

class HelloTool(BaseTool):
    async def run(self, name: str):
        self.logger.info("HelloTool called")
        return {"message": f"Hello, {name}!"}