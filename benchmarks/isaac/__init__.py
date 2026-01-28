"""
Isaac Sim PCA benchmark interfaces.

Note:
- Modules in this package define *interfaces only*.
- Isaac Sim physics-loop instrumentation is NOT yet wired.
- All PCA metrics here must be treated as placeholders.

Attempting to execute Isaac PCA runners will raise NotImplementedError
until the physics loop, sensor hooks, and energy logging are implemented.

This is an intentional design choice to avoid misleading or fabricated metrics.
"""
