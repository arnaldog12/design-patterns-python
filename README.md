# Design Patterns in Python

### Principles

- you **don't need** to use it **always!**
- disconnect **what's equal** from **what changes**
- **develop for an interface** instead of an implementation
- **open to extension, closed to modification**
- they help you **think out of the box!**
- **Hollywood principle**: superclasses must call child classes when need, and not the other way around

### Why to use Design Patterns?

- **good programming principles**: like coupling and cohesion
- **code faster**: you know what/how to do before implementation
- **code reuse**: can be used in multiple projects
- **code standardization**
- encourage more **legible** and **maintainable** code
- provide a **common language** and jargon for programmers

### When to apply? 

| **Pattern** |                        **Use it when you need...**                       |
|:-----------:|:------------------------------------------------------------------------:|
|  Singleton  |               to share attributes across the whole program               |
|   Strategy  |             different implementations for the same interface             |
|   Template  |            a sequence of steps with different implementations            |
|   Adapter   |                   to convert an interface into another                   |
|   Observer  |         to notify subscribers in case of events in the publisher         |
|  Decorator  |             to add responsibilities to an object dynamically             |
|    State    |                    to implement a finite state machine                   |
|  Composite  |                         a tree of similar objects                        |
|   Command   | to encapsulate all the info to perform an action (or schedule/undo them) |
