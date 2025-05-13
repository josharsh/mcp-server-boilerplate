from app.base.base_tool import BaseTool

class SimpleCalc(BaseTool):
    async def run(self, num1: float = 0, operator: str = "add", num2: float = 0):
        self.logger.info("SimpleCalc called")

        if operator == "add":
            result = num1 + num2
        elif operator == "subtract":
            result = num1 - num2
        elif operator == "multiply":
            result = num1 * num2
        elif operator == "divide":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        else:
            result = "Error: Invalid operation"
        
        # Return a response
        response = {"input": f"Received {num1} {operator} {num2}",
                  "result": result}
        return response