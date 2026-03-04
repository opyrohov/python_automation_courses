# Generics

Generic programming in TypeScript — creating flexible, type-safe components.

## Basic Generics

```typescript
// Function without generics — works with only one type
function getFirst(items: number[]): number {
    return items[0];
}

// Generic function — works with any type
function getFirst<T>(items: T[]): T {
    return items[0];
}

// Usage
const firstNumber = getFirst<number>([1, 2, 3]);     // number
const firstString = getFirst<string>(["a", "b"]);     // string
const firstAuto = getFirst([true, false]);             // boolean (type inference)
```

## Generic Functions

```typescript
// Swapping values
function swap<T>(a: T, b: T): [T, T] {
    return [b, a];
}

const [x, y] = swap<number>(1, 2);  // [2, 1]
const [a, b] = swap("hello", "world"); // ["world", "hello"]

// Multiple type parameters
function map<T, U>(items: T[], transform: (item: T) => U): U[] {
    return items.map(transform);
}

const lengths = map(["hello", "world"], (s) => s.length);
// number[] → [5, 5]
```

## Generic Interfaces

```typescript
// API response
interface APIResponse<T> {
    status: number;
    data: T;
    error?: string;
    timestamp: Date;
}

interface User {
    id: number;
    name: string;
    email: string;
}

interface Product {
    id: number;
    title: string;
    price: number;
}

// Typed responses
type UserResponse = APIResponse<User>;
type ProductListResponse = APIResponse<Product[]>;

async function fetchUser(id: number): Promise<UserResponse> {
    const res = await fetch(`/api/users/${id}`);
    return res.json();
}
```

```typescript
// Pagination
interface PaginatedList<T> {
    items: T[];
    total: number;
    page: number;
    perPage: number;
    hasNext: boolean;
}

function createPage<T>(
    items: T[],
    total: number,
    page: number
): PaginatedList<T> {
    return {
        items,
        total,
        page,
        perPage: items.length,
        hasNext: page * items.length < total,
    };
}
```

## Generic Classes

```typescript
class DataStore<T> {
    private items: T[] = [];

    add(item: T): void {
        this.items.push(item);
    }

    getById(index: number): T | undefined {
        return this.items[index];
    }

    getAll(): T[] {
        return [...this.items];
    }

    filter(predicate: (item: T) => boolean): T[] {
        return this.items.filter(predicate);
    }
}

// Typed store
const userStore = new DataStore<User>();
userStore.add({ id: 1, name: "John", email: "john@test.com" });
userStore.add({ id: 2, name: "Jane", email: "jane@test.com" });

const johns = userStore.filter((u) => u.name === "John");
```

## Constraints

```typescript
// extends — type constraint
interface HasId {
    id: number;
}

function findById<T extends HasId>(items: T[], id: number): T | undefined {
    return items.find((item) => item.id === id);
}

const users: User[] = [
    { id: 1, name: "John", email: "john@test.com" },
    { id: 2, name: "Jane", email: "jane@test.com" },
];

const user = findById(users, 1); // User | undefined
// findById([1, 2, 3], 1); // Error! number doesn't have an id field
```

### keyof Constraint

```typescript
// Accessing object properties
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

const user = { name: "John", age: 25, email: "john@test.com" };
const name = getProperty(user, "name");  // string
const age = getProperty(user, "age");    // number
// getProperty(user, "phone"); // Error! "phone" doesn't exist
```

## Default Types

```typescript
interface RequestOptions<T = Record<string, unknown>> {
    url: string;
    method: string;
    body?: T;
    headers?: Record<string, string>;
}

// Without specifying type — default is used
const getRequest: RequestOptions = {
    url: "/api/users",
    method: "GET",
};

// With specific type
interface CreateUserPayload {
    name: string;
    email: string;
}

const postRequest: RequestOptions<CreateUserPayload> = {
    url: "/api/users",
    method: "POST",
    body: { name: "John", email: "john@test.com" },
};
```

## Practical Example: Test Fixtures

```typescript
// Generic test data factory
class TestFixture<T> {
    private defaults: T;
    private overrides: Partial<T>[] = [];

    constructor(defaults: T) {
        this.defaults = defaults;
    }

    with(overrides: Partial<T>): TestFixture<T> {
        this.overrides.push(overrides);
        return this;
    }

    build(): T {
        let result = { ...this.defaults };
        for (const override of this.overrides) {
            result = { ...result, ...override };
        }
        this.overrides = [];
        return result;
    }

    buildMany(count: number): T[] {
        return Array.from({ length: count }, (_, i) =>
            this.with({ id: i + 1 } as Partial<T>).build()
        );
    }
}

// Usage
const userFixture = new TestFixture<User>({
    id: 0,
    name: "Default User",
    email: "default@test.com",
});

const admin = userFixture
    .with({ name: "Admin", email: "admin@test.com" })
    .build();

const testUsers = userFixture.buildMany(5);
```

::: tip Generics for Clean Code
Generics help avoid code duplication while maintaining type safety. Use them when the logic is the same for different types.
:::

## Useful Links

- [TypeScript: Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)
- [TypeScript: Generic Constraints](https://www.typescriptlang.org/docs/handbook/2/generics.html#generic-constraints)
