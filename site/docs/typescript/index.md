# TypeScript

Документація з TypeScript — типізованого JavaScript для надійного коду.

## Розділи

- [Базові типи](/docs/typescript/basic-types) - string, number, boolean, array
- [Функції](/docs/typescript/functions) - Типізація параметрів та повернення
- [Інтерфейси](/docs/typescript/interfaces) - Опис структур даних
- [Класи](/docs/typescript/classes) - ООП в TypeScript
- [Generics](/docs/typescript/generics) - Узагальнене програмування

## Що таке TypeScript?

TypeScript — це надбудова над JavaScript, що додає статичну типізацію.

| Характеристика | JavaScript | TypeScript |
|---------------|------------|------------|
| Типізація | Динамічна | Статична |
| Помилки | Runtime | Compile-time |
| IDE підтримка | Базова | Повна |

## Швидкий старт

```typescript
// Базові типи
let name: string = "Tester";
let age: number = 25;
let isActive: boolean = true;

// Масиви
let numbers: number[] = [1, 2, 3];
let names: Array<string> = ["Alice", "Bob"];

// Функції
function greet(name: string): string {
    return `Hello, ${name}!`;
}

// Інтерфейси
interface User {
    id: number;
    name: string;
    email?: string; // optional
}

const user: User = {
    id: 1,
    name: "John"
};
```

## Корисні посилання

- [Офіційна документація TypeScript](https://www.typescriptlang.org/docs/)
- [TypeScript Playground](https://www.typescriptlang.org/play)
