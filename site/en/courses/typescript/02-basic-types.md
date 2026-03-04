# 02. Basic Types

Core data types in TypeScript.

## Primitive Types

```typescript
// string
let name: string = "Alice";
let greeting: string = `Hello, ${name}!`;

// number
let age: number = 25;
let price: number = 19.99;
let hex: number = 0xff;

// boolean
let isActive: boolean = true;
let isDone: boolean = false;
```

## Arrays

```typescript
// Two ways to declare
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Readonly array
let readonlyArr: readonly number[] = [1, 2, 3];
// readonlyArr.push(4); // ❌ Error
```

## Tuple

```typescript
// Fixed length and types
let point: [number, number] = [10, 20];
let user: [string, number] = ["Alice", 25];

// Access by index
let x = point[0]; // number
let y = point[1]; // number
```

## Enum

```typescript
// Numeric enum
enum Direction {
    Up,     // 0
    Down,   // 1
    Left,   // 2
    Right   // 3
}

let move: Direction = Direction.Up;

// String enum
enum Status {
    Active = "ACTIVE",
    Inactive = "INACTIVE",
    Pending = "PENDING"
}
```

## Any and Unknown

```typescript
// any - any type (avoid it!)
let anything: any = 42;
anything = "string";
anything = true;

// unknown - a safer alternative
let value: unknown = "hello";

// Requires a check before use
if (typeof value === "string") {
    console.log(value.toUpperCase());
}
```

## Void, Null, Undefined

```typescript
// void - function returns nothing
function log(message: string): void {
    console.log(message);
}

// null and undefined
let u: undefined = undefined;
let n: null = null;
```

## Never

```typescript
// never - function never completes
function throwError(message: string): never {
    throw new Error(message);
}

function infiniteLoop(): never {
    while (true) {}
}
```

## Type Assertions

```typescript
// When you know the type better than TypeScript
let value: unknown = "hello world";

// Method 1: as
let length1 = (value as string).length;

// Method 2: angle bracket (doesn't work in JSX)
let length2 = (<string>value).length;
```

## Union Types

```typescript
// Can be one of several types
let id: string | number;
id = "abc";
id = 123;

// In functions
function printId(id: string | number): void {
    if (typeof id === "string") {
        console.log(id.toUpperCase());
    } else {
        console.log(id);
    }
}
```

## Literal Types

```typescript
// Specific values as types
let direction: "left" | "right" | "up" | "down";
direction = "left";  // ✅
// direction = "forward"; // ❌ Error

// With numbers
let dice: 1 | 2 | 3 | 4 | 5 | 6;
dice = 3; // ✅
```

## Type Inference

```typescript
// TypeScript infers types automatically
let name = "Alice";        // string
let age = 25;              // number
let isActive = true;       // boolean
let numbers = [1, 2, 3];   // number[]

// Explicit declaration is not needed
```

::: tip When to specify types explicitly?
- Function parameters
- Return values of public functions
- When inference doesn't work correctly
:::
