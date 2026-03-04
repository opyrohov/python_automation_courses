# 01. What is TypeScript

Introduction to TypeScript — typed JavaScript.

## What is TypeScript?

**TypeScript** is a superset of JavaScript that adds static typing.

```
TypeScript = JavaScript + Types
```

## Advantages of TypeScript

| Advantage | Description |
|-----------|-------------|
| Error detection | Errors are caught at development time, not at runtime |
| Autocompletion | IDE knows types and suggests methods and properties |
| Refactoring | Safe renaming and code modification |
| Documentation | Types serve as code documentation |

## JavaScript vs TypeScript

```javascript
// JavaScript - error only at runtime
function greet(name) {
    return "Hello, " + name.toUpperCase();
}

greet(123); // Runtime Error: name.toUpperCase is not a function
```

```typescript
// TypeScript - error immediately in IDE
function greet(name: string): string {
    return "Hello, " + name.toUpperCase();
}

greet(123); // ❌ Compile Error: Argument of type 'number'
            //    is not assignable to parameter of type 'string'
```

## Installation

```bash
# Globally
npm install -g typescript

# In a project
npm install --save-dev typescript

# Check version
tsc --version
```

## First File

```typescript
// hello.ts
const message: string = "Hello, TypeScript!";
console.log(message);
```

```bash
# Compilation
tsc hello.ts

# Result: hello.js
```

## tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"]
}
```

## How TypeScript Works

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│ TypeScript  │ tsc  │ JavaScript  │  →   │  Browser/   │
│   (.ts)     │  →   │   (.js)     │      │   Node.js   │
└─────────────┘      └─────────────┘      └─────────────┘
```

TypeScript compiles to JavaScript, which is then executed.

::: tip Tip
Start with `strict: true` in tsconfig.json — it will help you write higher quality code.
:::
