# TypeScript

Documentation on TypeScript — typed JavaScript for reliable code.

## Sections

- [Basic Types](/en/docs/typescript/basic-types) - string, number, boolean, array
- [Functions](/en/docs/typescript/functions) - Parameter and return type annotations
- [Interfaces](/en/docs/typescript/interfaces) - Describing data structures
- [Classes](/en/docs/typescript/classes) - OOP in TypeScript
- [Generics](/en/docs/typescript/generics) - Generic programming

## What is TypeScript?

TypeScript is a superset of JavaScript that adds static typing.

| Characteristic | JavaScript | TypeScript |
|---------------|------------|------------|
| Typing | Dynamic | Static |
| Errors | Runtime | Compile-time |
| IDE support | Basic | Full |

## Quick Start

```typescript
// Basic types
let name: string = "Tester";
let age: number = 25;
let isActive: boolean = true;

// Arrays
let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Functions
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Interfaces
interface User {
    id: number;
    name: string;
    email?: string; // optional
}

const user: User = {
    id: 1,
    name: "John"
};
```

## Useful Links

- [Official TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
