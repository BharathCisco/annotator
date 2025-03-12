# Annotator Tool

## Types of Annotations

### 1. Static Type Annotations
These are explicitly written in the code and checked before execution.
Tools for static analysis enforce type correctness without running the code.

#### Examples:
- **mypy**: The most widely used static type checker for Python.
- **pyright**: A fast, Microsoft-developed alternative to mypy.
- **Pyre**: A type checker developed by Meta (Facebook).
- **typeguard**: A runtime type checker that raises errors when type violations occur.

### 2. Runtime Type Inference
These tools analyze type usage dynamically during execution.
Useful for legacy codebases with missing annotations.

#### Examples:
- **MonkeyType**: Uses tracing to infer types at runtime.
- **pyannotate**: Automatically suggests annotations based on actual runtime usage.
- **pydantic**: Enforces type validation at runtime for structured data.
- **typeguard**: Checks function argument types at runtime.

## Conclusion
Since we're working on a **Dynamic Annotator**, which needs a balance of static and runtime analysis:

### 1. mypy (Static Type Checking)

🔹 **Why?**
- It verifies type correctness without running the code.
- Detects type mismatches, ensuring safer refactoring and fewer runtime errors.
- Helps catch edge cases that MonkeyType might miss.

🔹 **How it works?**
- Once type annotations are added (manually or using MonkeyType), mypy validates them.
- Flags incorrect type usages, making the code more robust and maintainable.

### 2. MonkeyType (Runtime Type Inference)

🔹 **Why?**
- It dynamically tracks function calls and records actual types used at runtime.
- Useful for legacy codebases where annotations are missing.
- Reduces manual effort in adding type hints.

🔹 **How it works?**
- It runs the application and logs function arguments and return types.
- Generates suggested type annotations based on collected runtime data.
