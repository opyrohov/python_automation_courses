# Класи

Об'єктно-орієнтоване програмування в TypeScript — модифікатори доступу, абстрактні класи, імплементація інтерфейсів.

## Базовий клас

```typescript
class User {
    name: string;
    email: string;

    constructor(name: string, email: string) {
        this.name = name;
        this.email = email;
    }

    greet(): string {
        return `Привіт, я ${this.name}!`;
    }
}

const user = new User("John", "john@test.com");
console.log(user.greet()); // "Привіт, я John!"
```

## Модифікатори доступу

```typescript
class TestConfig {
    public baseUrl: string;        // Доступний всюди (за замовчуванням)
    protected browser: string;      // Доступний в класі та нащадках
    private apiKey: string;         // Доступний тільки в класі
    readonly environment: string;   // Тільки для читання

    constructor(baseUrl: string, apiKey: string, env: string) {
        this.baseUrl = baseUrl;
        this.browser = "chromium";
        this.apiKey = apiKey;
        this.environment = env;
    }

    // Приватний метод
    private getHeaders(): Record<string, string> {
        return { Authorization: `Bearer ${this.apiKey}` };
    }

    public getConfig(): object {
        return {
            url: this.baseUrl,
            headers: this.getHeaders(),
        };
    }
}

const config = new TestConfig("https://example.com", "secret", "staging");
config.baseUrl;       // OK — public
// config.apiKey;     // Помилка — private
// config.browser;    // Помилка — protected
// config.environment = "prod"; // Помилка — readonly
```

## Скорочений конструктор

```typescript
// Замість довгого оголошення
class User {
    constructor(
        public name: string,
        public email: string,
        private password: string,
        public readonly id: number
    ) {}
    // Поля створюються автоматично!
}

const user = new User("John", "john@test.com", "secret", 1);
console.log(user.name); // "John"
console.log(user.id);   // 1
```

## Getter та Setter

```typescript
class TestTimer {
    private _duration: number = 0;
    private startTime: number = 0;

    get duration(): number {
        return this._duration;
    }

    get durationFormatted(): string {
        return `${this._duration.toFixed(2)}s`;
    }

    set timeout(ms: number) {
        if (ms < 0) throw new Error("Timeout не може бути від'ємним");
        this._duration = ms / 1000;
    }

    start(): void {
        this.startTime = Date.now();
    }

    stop(): void {
        this._duration = (Date.now() - this.startTime) / 1000;
    }
}

const timer = new TestTimer();
timer.start();
// ... виконання тесту
timer.stop();
console.log(timer.durationFormatted); // "1.23s"
```

## Наслідування

```typescript
class BasePage {
    constructor(protected page: any) {}

    async navigate(url: string): Promise<void> {
        await this.page.goto(url);
    }

    async getTitle(): Promise<string> {
        return this.page.title();
    }
}

class LoginPage extends BasePage {
    private readonly selectors = {
        email: "#email",
        password: "#password",
        submit: "#submit-btn",
    };

    async login(email: string, password: string): Promise<void> {
        await this.navigate("/login");
        await this.page.fill(this.selectors.email, email);
        await this.page.fill(this.selectors.password, password);
        await this.page.click(this.selectors.submit);
    }
}

class DashboardPage extends BasePage {
    async getWelcomeMessage(): Promise<string> {
        return this.page.textContent(".welcome-message");
    }
}
```

## Абстрактні класи

```typescript
abstract class BaseTest {
    abstract setup(): Promise<void>;
    abstract execute(): Promise<void>;
    abstract cleanup(): Promise<void>;

    // Конкретний метод
    async run(): Promise<void> {
        try {
            await this.setup();
            await this.execute();
        } finally {
            await this.cleanup();
        }
    }
}

class LoginTest extends BaseTest {
    async setup(): Promise<void> {
        console.log("Підготовка тестових даних");
    }

    async execute(): Promise<void> {
        console.log("Виконання тесту логіну");
    }

    async cleanup(): Promise<void> {
        console.log("Очищення даних");
    }
}

const test = new LoginTest();
await test.run();
// Не можна: const base = new BaseTest(); // Помилка — абстрактний!
```

## implements (імплементація інтерфейсів)

```typescript
interface Loggable {
    log(message: string): void;
}

interface Serializable {
    toJSON(): string;
}

class TestResult implements Loggable, Serializable {
    constructor(
        public testName: string,
        public passed: boolean,
        public duration: number
    ) {}

    log(message: string): void {
        console.log(`[${this.testName}] ${message}`);
    }

    toJSON(): string {
        return JSON.stringify({
            test: this.testName,
            passed: this.passed,
            duration: this.duration,
        });
    }
}
```

## Static члени

```typescript
class BrowserFactory {
    private static instances: Map<string, any> = new Map();

    static async create(browserType: string): Promise<any> {
        if (!this.instances.has(browserType)) {
            // Створити новий браузер
            const browser = await launchBrowser(browserType);
            this.instances.set(browserType, browser);
        }
        return this.instances.get(browserType);
    }

    static async closeAll(): Promise<void> {
        for (const [name, browser] of this.instances) {
            await browser.close();
            console.log(`Браузер ${name} закрито`);
        }
        this.instances.clear();
    }
}

// Використання без створення екземпляра
const chrome = await BrowserFactory.create("chromium");
await BrowserFactory.closeAll();
```

## Корисні посилання

- [TypeScript: Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
- [TypeScript: Abstract Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-classes-and-members)
