# Базові типи

Основні типи даних у TypeScript — string, number, boolean, array, tuple, enum та спеціальні типи.

## Примітивні типи

```typescript
// string — рядки
let name: string = "QA Engineer";
let greeting: string = `Hello, ${name}!`;

// number — числа (цілі та дробові)
let age: number = 25;
let price: number = 19.99;
let hex: number = 0xff;

// boolean — логічний тип
let isActive: boolean = true;
let isCompleted: boolean = false;

// null та undefined
let empty: null = null;
let notDefined: undefined = undefined;
```

## Масиви

```typescript
// Два способи оголошення
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Readonly масив
let readonlyItems: readonly number[] = [1, 2, 3];
// readonlyItems.push(4); // Помилка!

// Масив об'єктів
let users: { name: string; age: number }[] = [
    { name: "John", age: 25 },
    { name: "Jane", age: 30 },
];
```

## Tuple (кортеж)

```typescript
// Фіксований масив з відомими типами
let coordinate: [number, number] = [49.84, 24.02];
let record: [string, number, boolean] = ["test", 1, true];

// Деструктуризація
let [x, y] = coordinate;

// Named tuples (для читабельності)
type TestResult = [testName: string, passed: boolean, duration: number];
let result: TestResult = ["test_login", true, 1.5];
```

## Enum

```typescript
// Числовий enum
enum Status {
    Pending,    // 0
    Running,    // 1
    Passed,     // 2
    Failed,     // 3
}

let testStatus: Status = Status.Passed;

// Рядковий enum
enum Browser {
    Chromium = "chromium",
    Firefox = "firefox",
    Webkit = "webkit",
}

function launchBrowser(browser: Browser): void {
    console.log(`Запуск: ${browser}`);
}

launchBrowser(Browser.Firefox); // "Запуск: firefox"

// const enum — інлайниться при компіляції
const enum Environment {
    Dev = "dev",
    Staging = "staging",
    Prod = "prod",
}
```

::: tip Enum vs Union Types
Для простих випадків краще використовувати union types:
```typescript
// Замість enum
type BrowserType = "chromium" | "firefox" | "webkit";

function launch(browser: BrowserType): void {
    console.log(`Запуск: ${browser}`);
}
```
:::

## any, unknown, void, never

```typescript
// any — вимикає перевірку типів (уникайте!)
let data: any = "hello";
data = 42;       // OK
data = true;     // OK
data.anything(); // OK — але може впасти в runtime!

// unknown — безпечна альтернатива any
let value: unknown = "hello";
// value.toUpperCase(); // Помилка! Потрібна перевірка типу
if (typeof value === "string") {
    console.log(value.toUpperCase()); // OK
}

// void — функція нічого не повертає
function logMessage(msg: string): void {
    console.log(msg);
}

// never — функція ніколи не завершується
function throwError(message: string): never {
    throw new Error(message);
}

function infiniteLoop(): never {
    while (true) {
        // ...
    }
}
```

::: warning Уникайте any
Використання `any` зводить нанівець переваги TypeScript. Використовуйте `unknown` для невідомих типів та робіть перевірку типу перед використанням.
:::

## Type Assertions

```typescript
// as синтаксис (рекомендовано)
let someValue: unknown = "Hello World";
let strLength: number = (someValue as string).length;

// Angle bracket синтаксис
let strLength2: number = (<string>someValue).length;

// Практичний приклад
const element = document.getElementById("submit") as HTMLButtonElement;
element.click();
```

## Literal Types

```typescript
// Конкретні значення як типи
let direction: "up" | "down" | "left" | "right" = "up";

type HttpMethod = "GET" | "POST" | "PUT" | "DELETE";
type StatusCode = 200 | 201 | 400 | 404 | 500;

function request(method: HttpMethod, url: string): void {
    console.log(`${method} ${url}`);
}

request("GET", "/api/users");
// request("PATCH", "/api/users"); // Помилка!
```

## Utility Types

```typescript
interface User {
    id: number;
    name: string;
    email: string;
    role: string;
}

// Partial — всі поля опціональні
type UpdateUser = Partial<User>;

// Required — всі поля обов'язкові
type FullUser = Required<User>;

// Pick — вибрати поля
type UserCredentials = Pick<User, "email" | "role">;

// Omit — виключити поля
type PublicUser = Omit<User, "email">;

// Record — словник
type UserRoles = Record<string, string[]>;
const roles: UserRoles = {
    admin: ["read", "write", "delete"],
    viewer: ["read"],
};

// Readonly — всі поля тільки для читання
type ImmutableUser = Readonly<User>;
```

## Корисні посилання

- [TypeScript: Everyday Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
- [TypeScript: Utility Types](https://www.typescriptlang.org/docs/handbook/utility-types.html)
