# TypeScript Course

Повний курс з TypeScript — від основ до продвинутих концепцій.

## Огляд курсу

- **10 розділів** з теорією та практикою
- **Інтерактивні квізи** для закріплення
- **Практичні проєкти** для портфоліо

## Структура курсу

| # | Тема | Опис |
|---|------|------|
| 1 | [Що таке TypeScript](/courses/typescript/01-intro) | Вступ, переваги, встановлення |
| 2 | [Базові типи](/courses/typescript/02-basic-types) | string, number, boolean, array |
| 3 | [Функції](/courses/typescript/03-functions) | Типізація параметрів та return |
| 4 | Інтерфейси та типи | interface, type, extends |
| 5 | Класи | ООП в TypeScript |
| 6 | Generics | Узагальнене програмування |
| 7 | Модулі | import, export, namespace |
| 8 | Просунуті типи | Union, intersection, mapped |
| 9 | Декоратори | Метапрограмування |
| 10 | Практика | Фінальний проєкт |

## Навіщо вчити TypeScript?

::: tip Переваги TypeScript
- **Виявлення помилок** на етапі компіляції
- **Автодоповнення** в IDE
- **Самодокументований код**
- **Рефакторинг** без страху
:::

## JavaScript vs TypeScript

```javascript
// JavaScript - помилка лише в runtime
function greet(name) {
    return "Hello, " + name.toUpperCase();
}
greet(123); // Runtime Error!
```

```typescript
// TypeScript - помилка одразу в IDE
function greet(name: string): string {
    return "Hello, " + name.toUpperCase();
}
greet(123); // ❌ Compile Error: Argument of type 'number'
            //    is not assignable to parameter of type 'string'
```
