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

1. **Use MonkeyType**
   - It records function call arguments and return types dynamically.
   - You can then apply its suggested annotations to the source code.

2. **Integrate mypy for static checking**
   - After applying inferred annotations, `mypy` ensures correctness.

