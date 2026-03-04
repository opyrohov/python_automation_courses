# Interfaces

Interfaces in TypeScript — describing data structures, contracts for objects and classes.

## Basic Interface

```typescript
interface User {
    id: number;
    name: string;
    email: string;
}

// Object must match the interface
const user: User = {
    id: 1,
    name: "John Doe",
    email: "john@test.com",
};
```

## Optional and Readonly

```typescript
interface TestConfig {
    baseUrl: string;
    browser: string;
    headless?: boolean;        // Optional field
    timeout?: number;          // Optional field
    readonly apiKey: string;   // Read-only
}

const config: TestConfig = {
    baseUrl: "https://example.com",
    browser: "chromium",
    apiKey: "secret123",
    // headless and timeout — not required
};

// config.apiKey = "new"; // Error! readonly
```

## Nested Interfaces

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

## Extending

```typescript
// Base interface
interface BasePage {
    url: string;
    title: string;
    navigate(): void;
}

// Extension
interface LoginPage extends BasePage {
    emailInput: string;
    passwordInput: string;
    login(email: string, password: string): void;
}

// Multiple extension
interface AdminPage extends BasePage, LoginPage {
    adminPanel: string;
    manageUsers(): void;
}
```

## Index Signatures

```typescript
// Dynamic keys
interface TestData {
    [key: string]: string | number | boolean;
}

const data: TestData = {
    username: "john",
    age: 25,
    isActive: true,
};

// Dictionary with specific value type
interface Headers {
    [header: string]: string;
}

const headers: Headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer token123",
};
```

## Interfaces for Functions

```typescript
// Function interface
interface Validator {
    (value: string): boolean;
}

const isEmail: Validator = (value) => {
    return value.includes("@");
};

// Interface with methods
interface APIClient {
    baseUrl: string;
    get(endpoint: string): Promise<Response>;
    post(endpoint: string, data: unknown): Promise<Response>;
    delete(endpoint: string): Promise<Response>;
}
```

## Interface vs Type

```typescript
// Interface — for objects, classes, extension
interface Animal {
    name: string;
}

interface Dog extends Animal {
    breed: string;
}

// Type — for union, intersection, primitives
type ID = string | number;
type Status = "active" | "inactive";
type Point = { x: number; y: number };

// Intersection (type equivalent of extends)
type AdminUser = User & { permissions: string[] };
```

::: info When to Use Which?
- **Interface** — for describing the shape of objects and classes
- **Type** — for union types, intersections, complex types
- Both can be used for objects, but interface supports extension (`extends`)
:::

## Practical Example: API Responses

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

// Usage
type UserListResponse = APIResponse<PaginatedResponse<UserResponse>>;

async function getUsers(): Promise<UserListResponse> {
    const response = await fetch("/api/users");
    return response.json();
}
```

## Useful Links

- [TypeScript: Interfaces](https://www.typescriptlang.org/docs/handbook/2/objects.html)
- [TypeScript: Type vs Interface](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#differences-between-type-aliases-and-interfaces)
