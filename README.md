# mindfuck

Small [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter

### Introduction

[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) is an esoteric programming language with the goal of implementing it with the smallest possible compiler.

### Usage

```sh
➜ python mindfuck.py [FILE]
```

You can also use it as a module.

```python
import mindfuck

code = """
  ++++++++++[>+++++++>++++++++++>+++>+<<<<-]
  >++.>+.+++++++..+++.>++.<<+++++++++++++++.
  >.+++.------.--------.>+.>.
"""

mindfuck.eval(code)
```
