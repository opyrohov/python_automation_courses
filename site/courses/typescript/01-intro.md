# 01. Що таке TypeScript

Вступ до TypeScript — типізованого JavaScript.

## Що таке TypeScript?

**TypeScript** — це надбудова над JavaScript, яка додає статичну типізацію.

```
TypeScript = JavaScript + Types
```

## Переваги TypeScript

| Перевага | Опис |
|----------|------|
| Виявлення помилок | Помилки виявляються під час написання коду, а не в runtime |
| Автодоповнення | IDE знає типи і підказує методи та властивості |
| Рефакторинг | Безпечне перейменування та зміна коду |
| Документація | Типи служать документацією до коду |

## JavaScript vs TypeScript

```javascript
// JavaScript - помилка тільки в runtime
function greet(name) {
    return "Hello, " + name.toUpperCase();
}

greet(123); // Runtime Error: name.toUpperCase is not a function
```

```typescript
// TypeScript - помилка одразу в IDE
function greet(name: string): string {
    return "Hello, " + name.toUpperCase();
}

greet(123); // ❌ Compile Error: Argument of type 'number'
            //    is not assignable to parameter of type 'string'
```

## Встановлення

```bash
# Глобально
npm install -g typescript

# В проект
npm install --save-dev typescript

# Перевірка версії
tsc --version
```

## Перший файл

```typescript
// hello.ts
const message: string = "Hello, TypeScript!";
console.log(message);
```

```bash
# Компіляція
tsc hello.ts

# Результат: hello.js
```

## tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"]
}
```

## Як працює TypeScript

```
┌─────────────┐      ┌─────────────┐      ┌─────────────┐
│ TypeScript  │ tsc  │ JavaScript  │  →   │  Browser/   │
│   (.ts)     │  →   │   (.js)     │      │   Node.js   │
└─────────────┘      └─────────────┘      └─────────────┘
```

TypeScript компілюється в JavaScript, який потім виконується.

::: tip Порада
Почніть з `strict: true` в tsconfig.json — це допоможе писати якісніший код.
:::
