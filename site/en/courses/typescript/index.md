# TypeScript Course

Complete TypeScript course — from basics to advanced concepts.

## Course Overview

- **10 sections** with theory and practice
- **Interactive quizzes** for reinforcement
- **Practical projects** for your portfolio

## Course Structure

| # | Topic | Description |
|---|-------|-------------|
| 1 | [What is TypeScript](/en/courses/typescript/01-intro) | Introduction, advantages, installation |
| 2 | [Basic Types](/en/courses/typescript/02-basic-types) | string, number, boolean, array |
| 3 | [Functions](/en/courses/typescript/03-functions) | Typing parameters and return values |
| 4 | Interfaces and Types | interface, type, extends |
| 5 | Classes | OOP in TypeScript |
| 6 | Generics | Generic programming |
| 7 | Modules | import, export, namespace |
| 8 | Advanced Types | Union, intersection, mapped |
| 9 | Decorators | Metaprogramming |
| 10 | Practice | Final project |

## Why learn TypeScript?

::: tip TypeScript Advantages
- **Error detection** at compile time
- **Autocompletion** in IDE
- **Self-documenting code**
- **Refactoring** without fear
:::

## JavaScript vs TypeScript

```javascript
// JavaScript - error only at runtime
function greet(name) {
    return "Hello, " + name.toUpperCase();
}
greet(123); // Runtime Error!
```

```typescript
// TypeScript - error immediately in IDE
function greet(name: string): string {
    return "Hello, " + name.toUpperCase();
}
greet(123); // ❌ Compile Error: Argument of type 'number'
            //    is not assignable to parameter of type 'string'
```
