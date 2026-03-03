# Інтерфейси

Інтерфейси в TypeScript — опис структур даних, контракти для об'єктів та класів.

## Базовий інтерфейс

```typescript
interface User {
    id: number;
    name: string;
    email: string;
}

// Об'єкт повинен відповідати інтерфейсу
const user: User = {
    id: 1,
    name: "John Doe",
    email: "john@test.com",
};
```

## Optional та Readonly

```typescript
interface TestConfig {
    baseUrl: string;
    browser: string;
    headless?: boolean;        // Опціональне поле
    timeout?: number;          // Опціональне поле
    readonly apiKey: string;   // Тільки для читання
}

const config: TestConfig = {
    baseUrl: "https://example.com",
    browser: "chromium",
    apiKey: "secret123",
    // headless та timeout — не обов'язкові
};

// config.apiKey = "new"; // Помилка! readonly
```

## Вкладені інтерфейси

```typescript
interface Address {
    street: string;
    city: string;
    country: string;
    zip?: string;
}

interface Company {
    name: string;
    address: Address;
}

interface Employee {
    id: number;
    name: string;
    company: Company;
    skills: string[];
}

const employee: Employee = {
    id: 1,
    name: "John",
    company: {
        name: "TechCorp",
        address: {
            street: "Main St 1",
            city: "Kyiv",
            country: "Ukraine",
        },
    },
    skills: ["TypeScript", "Playwright"],
};
```

## Extending (розширення)

```typescript
// Базовий інтерфейс
interface BasePage {
    url: string;
    title: string;
    navigate(): void;
}

// Розширення
interface LoginPage extends BasePage {
    emailInput: string;
    passwordInput: string;
    login(email: string, password: string): void;
}

// Множинне розширення
interface AdminPage extends BasePage, LoginPage {
    adminPanel: string;
    manageUsers(): void;
}
```

## Index Signatures

```typescript
// Динамічні ключі
interface TestData {
    [key: string]: string | number | boolean;
}

const data: TestData = {
    username: "john",
    age: 25,
    isActive: true,
};

// Словник з конкретним типом значення
interface Headers {
    [header: string]: string;
}

const headers: Headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
};
```

## Інтерфейси для функцій

```typescript
// Інтерфейс функції
interface Validator {
    (value: string): boolean;
}

const isEmail: Validator = (value) => {
    return value.includes("@");
};

// Інтерфейс з методами
interface APIClient {
    baseUrl: string;
    get(endpoint: string): Promise<Response>;
    post(endpoint: string, data: unknown): Promise<Response>;
    delete(endpoint: string): Promise<Response>;
}
```

## Interface vs Type

```typescript
// Interface — для об'єктів, класів, розширення
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}

// Type — для union, intersection, примітивів
type ID = string | number;
type Status = "active" | "inactive";
type Point = { x: number; y: number };

// Intersection (аналог extends для type)
type AdminUser = User & { permissions: string[] };
```

::: info Коли що використовувати?
- **Interface** — для опису форми об'єктів та класів
- **Type** — для union types, intersection, складних типів
- Обидва можна використовувати для об'єктів, але interface підтримує розширення (`extends`)
:::

## Практичний приклад: API відповіді

```typescript
interface APIResponse<T> {
    status: number;
    data: T;
    message?: string;
    timestamp: string;
}

interface UserResponse {
    id: number;
    name: string;
    email: string;
}

interface PaginatedResponse<T> {
    items: T[];
    total: number;
    page: number;
    perPage: number;
}

// Використання
type UserListResponse = APIResponse<PaginatedResponse<UserResponse>>;

async function getUsers(): Promise<UserListResponse> {
    const response = await fetch("/api/users");
    return response.json();
}
```

## Корисні посилання

- [TypeScript: Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)
- [TypeScript: Type vs Interface](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)
