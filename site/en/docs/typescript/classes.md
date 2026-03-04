# Classes

Object-oriented programming in TypeScript — access modifiers, abstract classes, interface implementation.

## Basic Class

```typescript
class User {
    name: string;
    email: string;

    constructor(name: string, email: string) {
        this.name = name;
        this.email = email;
    }

    greet(): string {
        return `Hello, I'm ${this.name}!`;
    }
}

const user = new User("John", "john@test.com");
console.log(user.greet()); // "Hello, I'm John!"
```

## Access Modifiers

```typescript
class TestConfig {
    public baseUrl: string;        // Accessible everywhere (default)
    protected browser: string;      // Accessible in the class and subclasses
    private apiKey: string;         // Accessible only in the class
    readonly environment: string;   // Read-only

    constructor(baseUrl: string, apiKey: string, env: string) {
        this.baseUrl = baseUrl;
        this.browser = "chromium";
        this.apiKey = apiKey;
        this.environment = env;
    }

    // Private method
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
// config.apiKey;     // Error — private
// config.browser;    // Error — protected
// config.environment = "prod"; // Error — readonly
```

## Shorthand Constructor

```typescript
// Instead of verbose declaration
class User {
    constructor(
        public name: string,
        public email: string,
        private password: string,
        public readonly id: number
    ) {}
    // Fields are created automatically!
}

const user = new User("John", "john@test.com", "secret", 1);
console.log(user.name); // "John"
console.log(user.id);   // 1
```

## Getter and Setter

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
        if (ms < 0) throw new Error("Timeout cannot be negative");
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
// ... test execution
timer.stop();
console.log(timer.durationFormatted); // "1.23s"
```

## Inheritance

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

## Abstract Classes

```typescript
abstract class BaseTest {
    abstract setup(): Promise<void>;
    abstract execute(): Promise<void>;
    abstract cleanup(): Promise<void>;

    // Concrete method
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
        console.log("Preparing test data");
    }

    async execute(): Promise<void> {
        console.log("Executing login test");
    }

    async cleanup(): Promise<void> {
        console.log("Cleaning up data");
    }
}

const test = new LoginTest();
await test.run();
// Cannot: const base = new BaseTest(); // Error — abstract!
```

## implements (Interface Implementation)

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

## Static Members

```typescript
class BrowserFactory {
    private static instances: Map<string, any> = new Map();

    static async create(browserType: string): Promise<any> {
        if (!this.instances.has(browserType)) {
            // Create new browser
            const browser = await launchBrowser(browserType);
            this.instances.set(browserType, browser);
        }
        return this.instances.get(browserType);
    }

    static async closeAll(): Promise<void> {
        for (const [name, browser] of this.instances) {
            await browser.close();
            console.log(`Browser ${name} closed`);
        }
        this.instances.clear();
    }
}

// Usage without creating an instance
const chrome = await BrowserFactory.create("chromium");
await BrowserFactory.closeAll();
```

## Useful Links

- [TypeScript: Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html)
- [TypeScript: Abstract Classes](https://www.typescriptlang.org/docs/handbook/2/classes.html#abstract-classes-and-members)
