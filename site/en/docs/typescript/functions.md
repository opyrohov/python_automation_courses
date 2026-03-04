# Functions

Function typing in TypeScript — parameters, return values, overloads, and arrow functions.

## Basic Typing

```typescript
// Typed parameters and return
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// void — returns nothing
function logMessage(message: string): void {
    console.log(message);
}

// Automatic return type inference
function greet(name: string) {
    return `Hello, ${name}!`; // TypeScript infers: string
}
```

## Optional and Default Parameters

```typescript
// Optional parameters (?)
function createUser(name: string, email?: string): object {
    return { name, email: email ?? "not provided" };
}

createUser("John");                    // OK
createUser("John", "john@test.com");   // OK

// Default values
function launchBrowser(
    browser: string = "chromium",
    headless: boolean = true,
    timeout: number = 30000
): void {
    console.log(`Launching: ${browser}, headless=${headless}`);
}

launchBrowser();                        // chromium, headless=true
launchBrowser("firefox", false);        // firefox, headless=false
```

## Rest Parameters

```typescript
// Arbitrary number of arguments
function sum(...numbers: number[]): number {
    return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3);       // 6
sum(1, 2, 3, 4, 5); // 15

// Combining with regular parameters
function logTestResults(suite: string, ...results: boolean[]): void {
    const passed = results.filter(Boolean).length;
    console.log(`${suite}: ${passed}/${results.length} passed`);
}

logTestResults("Login", true, true, false, true);
// "Login: 3/4 passed"
```

## Function Types

```typescript
// Function type
type MathOperation = (a: number, b: number) => number;

const add: MathOperation = (a, b) => a + b;
const subtract: MathOperation = (a, b) => a - b;

// Function as parameter
function calculate(a: number, b: number, operation: MathOperation): number {
    return operation(a, b);
}

calculate(10, 5, add);      // 15
calculate(10, 5, subtract); // 5

// Callback types
type OnComplete = (success: boolean, message: string) => void;

function runTest(name: string, onComplete: OnComplete): void {
    try {
        // ... test execution
        onComplete(true, `${name} passed`);
    } catch (e) {
        onComplete(false, `${name} failed: ${e}`);
    }
}
```

## Overloads

```typescript
// Different behavior for different types
function format(value: string): string;
function format(value: number): string;
function format(value: Date): string;
function format(value: string | number | Date): string {
    if (typeof value === "string") {
        return value.trim();
    } else if (typeof value === "number") {
        return value.toFixed(2);
    } else {
        return value.toISOString();
    }
}

format("  hello  ");        // "hello"
format(3.14159);            // "3.14"
format(new Date());         // "2024-01-15T..."
```

## Generic Functions

```typescript
// Function works with any type
function first<T>(items: T[]): T | undefined {
    return items[0];
}

first([1, 2, 3]);          // number | undefined
first(["a", "b"]);         // string | undefined

// Multiple generic parameters
function zip<T, U>(a: T[], b: U[]): [T, U][] {
    const length = Math.min(a.length, b.length);
    return Array.from({ length }, (_, i) => [a[i], b[i]]);
}

zip([1, 2, 3], ["a", "b", "c"]);
// [[1, "a"], [2, "b"], [3, "c"]]
```

## Async Functions

```typescript
// Promise typing
async function fetchUser(id: number): Promise<User> {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
    }
    return response.json();
}

// Usage
const user = await fetchUser(1); // User

// Async callback
type AsyncAction = () => Promise<void>;

async function withRetry(action: AsyncAction, retries: number = 3): Promise<void> {
    for (let i = 0; i < retries; i++) {
        try {
            await action();
            return;
        } catch (e) {
            if (i === retries - 1) throw e;
            console.log(`Attempt ${i + 1} failed, retrying...`);
        }
    }
}
```

::: tip Typing for Tests
```typescript
// Typed test function
type TestFn = (page: Page) => Promise<void>;

const testCases: Record<string, TestFn> = {
    "should login": async (page) => {
        await page.goto("/login");
        await page.fill("#email", "user@test.com");
    },
    "should logout": async (page) => {
        await page.click("#logout");
    },
};
```
:::

## Useful Links

- [TypeScript: Functions](https://www.typescriptlang.org/docs/handbook/2/functions.html)
- [TypeScript: Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
