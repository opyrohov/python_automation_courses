# Basic Types

Fundamental data types in TypeScript — string, number, boolean, array, tuple, enum, and special types.

## Primitive Types

```typescript
// string — strings
let name: string = "QA Engineer";
let greeting: string = `Hello, ${name}!`;

// number — numbers (integer and floating-point)
let age: number = 25;
let price: number = 19.99;
let hex: number = 0xff;

// boolean — logical type
let isActive: boolean = true;
let isCompleted: boolean = false;

// null and undefined
let empty: null = null;
let notDefined: undefined = undefined;
```

## Arrays

```typescript
// Two ways to declare
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Readonly array
let readonlyItems: readonly number[] = [1, 2, 3];
// readonlyItems.push(4); // Error!

// Array of objects
let users: { name: string; age: number }[] = [
    { name: "John", age: 25 },
    { name: "Jane", age: 30 },
];
```

## Tuple

```typescript
// Fixed array with known types
let coordinate: [number, number] = [49.84, 24.02];
let record: [string, number, boolean] = ["test", 1, true];

// Destructuring
let [x, y] = coordinate;

// Named tuples (for readability)
type TestResult = [testName: string, passed: boolean, duration: number];
let result: TestResult = ["test_login", true, 1.5];
```

## Enum

```typescript
// Numeric enum
enum Status {
    Pending,    // 0
    Running,    // 1
    Passed,     // 2
    Failed,     // 3
}

let testStatus: Status = Status.Passed;

// String enum
enum Browser {
    Chromium = "chromium",
    Firefox = "firefox",
    Webkit = "webkit",
}

function launchBrowser(browser: Browser): void {
    console.log(`Launching: ${browser}`);
}

launchBrowser(Browser.Firefox); // "Launching: firefox"

// const enum — inlined at compilation
const enum Environment {
    Dev = "dev",
    Staging = "staging",
    Prod = "prod",
}
```

::: tip Enum vs Union Types
For simple cases, it's better to use union types:
```typescript
// Instead of enum
type BrowserType = "chromium" | "firefox" | "webkit";

function launch(browser: BrowserType): void {
    console.log(`Launching: ${browser}`);
}
```
:::

## any, unknown, void, never

```typescript
// any — disables type checking (avoid!)
let data: any = "hello";
data = 42;       // OK
data = true;     // OK
data.anything(); // OK — but may crash at runtime!

// unknown — safe alternative to any
let value: unknown = "hello";
// value.toUpperCase(); // Error! Type check required
if (typeof value === "string") {
    console.log(value.toUpperCase()); // OK
}

// void — function returns nothing
function logMessage(msg: string): void {
    console.log(msg);
}

// never — function never completes
function throwError(message: string): never {
    throw new Error(message);
}

function infiniteLoop(): never {
    while (true) {
        // ...
    }
}
```

::: warning Avoid any
Using `any` negates the benefits of TypeScript. Use `unknown` for unknown types and perform type checks before usage.
:::

## Type Assertions

```typescript
// as syntax (recommended)
let someValue: unknown = "Hello World";
let strLength: number = (someValue as string).length;

// Angle bracket syntax
let strLength2: number = (<string>someValue).length;

// Practical example
const element = document.getElementById("submit") as HTMLButtonElement;
element.click();
```

## Literal Types

```typescript
// Specific values as types
let direction: "up" | "down" | "left" | "right" = "up";

type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
type StatusCode = 200 | 201 | 400 | 404 | 500;

function request(method: HttpMethod, url: string): void {
    console.log(`${method} ${url}`);
}

request("GET", "/api/users");
// request("PATCH", "/api/users"); // Error!
```

## Utility Types

```typescript
interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

// Partial — all fields optional
type UpdateUser = Partial<User>;

// Required — all fields required
type FullUser = Required<User>;

// Pick — select fields
type UserCredentials = Pick<User, "email" | "role">;

// Omit — exclude fields
type PublicUser = Omit<User, "email">;

// Record — dictionary
type UserRoles = Record<string, string[]>;
const roles: UserRoles = {
    admin: ["read", "write", "delete"],
    viewer: ["read"],
};

// Readonly — all fields read-only
type ImmutableUser = Readonly<User>;
```

## Useful Links

- [TypeScript: Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [TypeScript: Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
