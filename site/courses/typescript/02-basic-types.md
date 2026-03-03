# 02. Базові типи

Основні типи даних в TypeScript.

## Примітивні типи

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

## Масиви

```typescript
// Два способи оголошення
let numbers: number[] = [1, 2, 3, 4, 5];
let names: Array<string> = ["Alice", "Bob", "Charlie"];

// Readonly масив
let readonlyArr: readonly number[] = [1, 2, 3];
// readonlyArr.push(4); // ❌ Error
```

## Tuple

```typescript
// Фіксована довжина та типи
let point: [number, number] = [10, 20];
let user: [string, number] = ["Alice", 25];

// Доступ за індексом
let x = point[0]; // number
let y = point[1]; // number
```

## Enum

```typescript
// Числовий enum
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

## Any та Unknown

```typescript
// any - будь-який тип (уникайте!)
let anything: any = 42;
anything = "string";
anything = true;

// unknown - безпечніша альтернатива
let value: unknown = "hello";

// Потрібна перевірка перед використанням
if (typeof value === "string") {
    console.log(value.toUpperCase());
}
```

## Void, Null, Undefined

```typescript
// void - функція нічого не повертає
function log(message: string): void {
    console.log(message);
}

// null та undefined
let u: undefined = undefined;
let n: null = null;
```

## Never

```typescript
// never - функція ніколи не завершується
function throwError(message: string): never {
    throw new Error(message);
}

function infiniteLoop(): never {
    while (true) {}
}
```

## Type Assertions

```typescript
// Коли ви знаєте тип краще за TypeScript
let value: unknown = "hello world";

// Спосіб 1: as
let length1 = (value as string).length;

// Спосіб 2: angle bracket (не працює в JSX)
let length2 = (<string>value).length;
```

## Union Types

```typescript
// Може бути одним з кількох типів
let id: string | number;
id = "abc";
id = 123;

// У функціях
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
// Конкретні значення як типи
let direction: "left" | "right" | "up" | "down";
direction = "left";  // ✅
// direction = "forward"; // ❌ Error

// З числами
let dice: 1 | 2 | 3 | 4 | 5 | 6;
dice = 3; // ✅
```

## Type Inference

```typescript
// TypeScript виводить типи автоматично
let name = "Alice";        // string
let age = 25;              // number
let isActive = true;       // boolean
let numbers = [1, 2, 3];   // number[]

// Явне оголошення не потрібне
```

::: tip Коли вказувати типи явно?
- Параметри функцій
- Повернені значення публічних функцій
- Коли inference не працює правильно
:::
