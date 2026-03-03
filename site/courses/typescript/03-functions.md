# 03. Функції

Типізація функцій в TypeScript.

## Базова типізація

```typescript
// Типізація параметрів та return
function add(a: number, b: number): number {
    return a + b;
}

// Arrow function
const multiply = (a: number, b: number): number => a * b;

// Без повернення (void)
function log(message: string): void {
    console.log(message);
}
```

## Optional параметри

```typescript
// ? робить параметр optional
function greet(name: string, greeting?: string): string {
    return `${greeting || "Hello"}, ${name}!`;
}

greet("Alice");           // "Hello, Alice!"
greet("Bob", "Hi");       // "Hi, Bob!"
```

## Default параметри

```typescript
function greet(name: string, greeting: string = "Hello"): string {
    return `${greeting}, ${name}!`;
}

greet("Alice");           // "Hello, Alice!"
greet("Bob", "Hi");       // "Hi, Bob!"
```

## Rest параметри

```typescript
function sum(...numbers: number[]): number {
    return numbers.reduce((acc, n) => acc + n, 0);
}

sum(1, 2, 3);       // 6
sum(1, 2, 3, 4, 5); // 15
```

## Function Types

```typescript
// Тип функції
type MathOperation = (a: number, b: number) => number;

const add: MathOperation = (a, b) => a + b;
const subtract: MathOperation = (a, b) => a - b;

// Як параметр
function calculate(
    a: number,
    b: number,
    operation: MathOperation
): number {
    return operation(a, b);
}

calculate(10, 5, add);      // 15
calculate(10, 5, subtract); // 5
```

## Overloads

```typescript
// Різні сигнатури для різних типів
function reverse(value: string): string;
function reverse(value: number[]): number[];
function reverse(value: string | number[]): string | number[] {
    if (typeof value === "string") {
        return value.split("").reverse().join("");
    }
    return value.reverse();
}

reverse("hello");   // "olleh"
reverse([1, 2, 3]); // [3, 2, 1]
```

## Generic Functions

```typescript
// Узагальнені функції
function identity<T>(value: T): T {
    return value;
}

identity<string>("hello"); // "hello"
identity<number>(42);      // 42
identity(true);            // boolean (inferred)

// Кілька generic параметрів
function pair<K, V>(key: K, value: V): [K, V] {
    return [key, value];
}

pair("name", "Alice"); // ["name", "Alice"]
pair(1, true);         // [1, true]
```

## Generic Constraints

```typescript
// Обмеження на generic тип
interface HasLength {
    length: number;
}

function logLength<T extends HasLength>(value: T): void {
    console.log(value.length);
}

logLength("hello");     // 5 ✅
logLength([1, 2, 3]);   // 3 ✅
// logLength(123);      // ❌ Error: number doesn't have length
```

## Callback Functions

```typescript
// Типізація callbacks
function fetchData(
    url: string,
    callback: (data: string, error?: Error) => void
): void {
    // ...
    callback("data");
}

fetchData("https://api.example.com", (data, error) => {
    if (error) {
        console.error(error);
    } else {
        console.log(data);
    }
});
```

## This в функціях

```typescript
interface User {
    name: string;
    greet(this: User): void;
}

const user: User = {
    name: "Alice",
    greet() {
        console.log(`Hello, I'm ${this.name}`);
    }
};

user.greet(); // "Hello, I'm Alice"
```

::: tip Порада
Завжди типізуйте параметри функцій. Return type можна опускати, якщо він очевидний з коду.
:::
