import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'QA Learning Hub',
  base: '/python_automation_courses/',

  ignoreDeadLinks: true,

  vite: {
    assetsInclude: ['**/*.html'],
    server: {
      fs: {
        allow: ['..']
      }
    }
  },

  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/python_automation_courses/favicon.svg' }],
    ['meta', { name: 'theme-color', content: '#5d6eff' }],
  ],

  locales: {
    root: {
      label: 'Українська',
      lang: 'uk-UA',
      description: 'Документація та курси для QA-автоматизації',
      themeConfig: {
        nav: [
          { text: 'Головна', link: '/' },
          {
            text: 'Документація',
            items: [
              { text: 'Python', link: '/docs/python/' },
              { text: 'Playwright', link: '/docs/playwright/' },
              { text: 'Pytest', link: '/docs/pytest/' },
              { text: 'TypeScript', link: '/docs/typescript/' },
            ]
          },
          {
            text: 'Курси',
            items: [
              { text: 'Python Automation', link: '/courses/python-automation/' },
              { text: 'TypeScript', link: '/courses/typescript/' },
            ]
          },
          { text: 'Cheatsheets', link: '/cheatsheets/' },
        ],
        sidebar: {
          '/docs/python/': [
            {
              text: 'Python',
              items: [
                { text: 'Вступ', link: '/docs/python/' },
                { text: 'Основи', link: '/docs/python/basics' },
                { text: 'Типи даних', link: '/docs/python/data-types' },
                { text: 'Функції', link: '/docs/python/functions' },
                { text: 'ООП', link: '/docs/python/oop' },
                { text: 'Модулі', link: '/docs/python/modules' },
                { text: 'Обробка помилок', link: '/docs/python/error-handling' },
                { text: 'Best Practices', link: '/docs/python/best-practices' },
              ]
            }
          ],
          '/docs/playwright/': [
            {
              text: 'Playwright',
              items: [
                { text: 'Вступ', link: '/docs/playwright/' },
                { text: 'Налаштування', link: '/docs/playwright/setup' },
                { text: 'Locators', link: '/docs/playwright/locators' },
                { text: 'Actions', link: '/docs/playwright/actions' },
                { text: 'Assertions', link: '/docs/playwright/assertions' },
                { text: 'Waits', link: '/docs/playwright/waits' },
                { text: 'Page Object Model', link: '/docs/playwright/page-object' },
                { text: 'API Testing', link: '/docs/playwright/api-testing' },
                { text: 'Screenshots & Video', link: '/docs/playwright/screenshots-video' },
              ]
            }
          ],
          '/docs/pytest/': [
            {
              text: 'Pytest',
              items: [
                { text: 'Вступ', link: '/docs/pytest/' },
                { text: 'Fixtures', link: '/docs/pytest/fixtures' },
                { text: 'Markers', link: '/docs/pytest/markers' },
                { text: 'Параметризація', link: '/docs/pytest/parametrize' },
                { text: 'Конфігурація', link: '/docs/pytest/configuration' },
                { text: 'Плагіни', link: '/docs/pytest/plugins' },
              ]
            }
          ],
          '/docs/typescript/': [
            {
              text: 'TypeScript',
              items: [
                { text: 'Вступ', link: '/docs/typescript/' },
                { text: 'Базові типи', link: '/docs/typescript/basic-types' },
                { text: 'Функції', link: '/docs/typescript/functions' },
                { text: 'Інтерфейси', link: '/docs/typescript/interfaces' },
                { text: 'Класи', link: '/docs/typescript/classes' },
                { text: 'Generics', link: '/docs/typescript/generics' },
              ]
            }
          ],
          '/courses/python-automation/': [
            {
              text: 'Python Automation',
              items: [
                { text: 'Огляд курсу', link: '/courses/python-automation/' },
              ]
            },
            {
              text: 'Phase 1: Python Basics',
              collapsed: false,
              items: [
                { text: '01. Setup & Basics', link: '/courses/python-automation/01-setup' },
                { text: '02. Strings & Control Flow', link: '/courses/python-automation/02-strings' },
                { text: '03. Loops', link: '/courses/python-automation/03-loops' },
                { text: '04. Lists & Dictionaries', link: '/courses/python-automation/04-lists-dicts' },
                { text: '05. Functions', link: '/courses/python-automation/05-functions' },
                { text: '06. Modules', link: '/courses/python-automation/06-modules' },
                { text: '07. Files & JSON', link: '/courses/python-automation/07-files-json' },
                { text: '08. Error Handling', link: '/courses/python-automation/08-error-handling' },
                { text: '09. Classes Part 1', link: '/courses/python-automation/09-classes-1' },
                { text: '10. Classes Part 2', link: '/courses/python-automation/10-classes-2' },
                { text: '11. Advanced Python', link: '/courses/python-automation/11-advanced-python' },
                { text: '12. Review & Setup', link: '/courses/python-automation/12-review' },
              ]
            },
            {
              text: 'Phase 2: Playwright',
              collapsed: true,
              items: [
                { text: '13. Playwright Setup', link: '/courses/python-automation/13-playwright-setup' },
                { text: '14. Navigation', link: '/courses/python-automation/14-navigation' },
                { text: '15. Locators Part 1', link: '/courses/python-automation/15-locators-1' },
                { text: '16. Locators Part 2', link: '/courses/python-automation/16-locators-2' },
                { text: '17. Form Handling', link: '/courses/python-automation/17-forms' },
                { text: '18. Mouse & Keyboard', link: '/courses/python-automation/18-mouse-keyboard' },
                { text: '19. Wait Strategies', link: '/courses/python-automation/19-waits' },
                { text: '20. Assertions', link: '/courses/python-automation/20-assertions' },
                { text: '21. Multiple Elements', link: '/courses/python-automation/21-multiple-elements' },
              ]
            },
            {
              text: 'Phase 3: Advanced',
              collapsed: true,
              items: [
                { text: '22. Frames & iframes', link: '/courses/python-automation/22-frames' },
                { text: '23. Multiple Pages', link: '/courses/python-automation/23-multiple-pages' },
                { text: '24. Screenshots & Video', link: '/courses/python-automation/24-screenshots-video' },
                { text: '25. Authentication', link: '/courses/python-automation/25-authentication' },
                { text: '26. Cookies & Storage', link: '/courses/python-automation/26-cookies-storage' },
                { text: '27. Network Interception', link: '/courses/python-automation/27-network' },
                { text: '28. API Testing', link: '/courses/python-automation/28-api-testing' },
                { text: '29. Page Object Model 1', link: '/courses/python-automation/29-pom' },
                { text: '30. Page Object Model 2', link: '/courses/python-automation/30-pom-2' },
              ]
            },
            {
              text: 'Phase 4: Pytest',
              collapsed: true,
              items: [
                { text: '31. Pytest Integration', link: '/courses/python-automation/31-pytest' },
                { text: '32. Test Configuration', link: '/courses/python-automation/32-test-config' },
                { text: '33. Test Data Management', link: '/courses/python-automation/33-test-data' },
                { text: '34. Parameterized Testing', link: '/courses/python-automation/34-parametrized' },
                { text: '35. Debugging', link: '/courses/python-automation/35-debugging' },
                { text: '36. Best Practices', link: '/courses/python-automation/36-best-practices' },
              ]
            },
          ],
          '/courses/typescript/': [
            {
              text: 'TypeScript Course',
              items: [
                { text: 'Огляд курсу', link: '/courses/typescript/' },
                { text: '01. Що таке TypeScript', link: '/courses/typescript/01-intro' },
                { text: '02. Базові типи', link: '/courses/typescript/02-basic-types' },
                { text: '03. Функції', link: '/courses/typescript/03-functions' },
              ]
            }
          ],
          '/cheatsheets/': [
            {
              text: 'Cheatsheets',
              items: [
                { text: 'Огляд', link: '/cheatsheets/' },
                { text: 'Python', link: '/cheatsheets/python' },
                { text: 'Pytest', link: '/cheatsheets/pytest' },
                { text: 'Playwright', link: '/cheatsheets/playwright' },
                { text: 'Git', link: '/cheatsheets/git' },
              ]
            }
          ],
        },
        outline: {
          label: 'На цій сторінці'
        },
        docFooter: {
          prev: 'Попередня',
          next: 'Наступна'
        },
        lastUpdated: {
          text: 'Оновлено'
        },
        footer: {
          message: 'QA Learning Hub - Документація та курси для QA-автоматизації',
          copyright: '© 2024'
        },
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      description: 'Documentation and courses for QA automation',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          {
            text: 'Documentation',
            items: [
              { text: 'Python', link: '/en/docs/python/' },
              { text: 'Playwright', link: '/en/docs/playwright/' },
              { text: 'Pytest', link: '/en/docs/pytest/' },
              { text: 'TypeScript', link: '/en/docs/typescript/' },
            ]
          },
          {
            text: 'Courses',
            items: [
              { text: 'Python Automation', link: '/en/courses/python-automation/' },
              { text: 'TypeScript', link: '/en/courses/typescript/' },
            ]
          },
          { text: 'Cheatsheets', link: '/en/cheatsheets/' },
        ],
        sidebar: {
          '/en/docs/python/': [
            {
              text: 'Python',
              items: [
                { text: 'Introduction', link: '/en/docs/python/' },
                { text: 'Basics', link: '/en/docs/python/basics' },
                { text: 'Data Types', link: '/en/docs/python/data-types' },
                { text: 'Functions', link: '/en/docs/python/functions' },
                { text: 'OOP', link: '/en/docs/python/oop' },
                { text: 'Modules', link: '/en/docs/python/modules' },
                { text: 'Error Handling', link: '/en/docs/python/error-handling' },
                { text: 'Best Practices', link: '/en/docs/python/best-practices' },
              ]
            }
          ],
          '/en/docs/playwright/': [
            {
              text: 'Playwright',
              items: [
                { text: 'Introduction', link: '/en/docs/playwright/' },
                { text: 'Setup', link: '/en/docs/playwright/setup' },
                { text: 'Locators', link: '/en/docs/playwright/locators' },
                { text: 'Actions', link: '/en/docs/playwright/actions' },
                { text: 'Assertions', link: '/en/docs/playwright/assertions' },
                { text: 'Waits', link: '/en/docs/playwright/waits' },
                { text: 'Page Object Model', link: '/en/docs/playwright/page-object' },
                { text: 'API Testing', link: '/en/docs/playwright/api-testing' },
                { text: 'Screenshots & Video', link: '/en/docs/playwright/screenshots-video' },
              ]
            }
          ],
          '/en/docs/pytest/': [
            {
              text: 'Pytest',
              items: [
                { text: 'Introduction', link: '/en/docs/pytest/' },
                { text: 'Fixtures', link: '/en/docs/pytest/fixtures' },
                { text: 'Markers', link: '/en/docs/pytest/markers' },
                { text: 'Parameterization', link: '/en/docs/pytest/parametrize' },
                { text: 'Configuration', link: '/en/docs/pytest/configuration' },
                { text: 'Plugins', link: '/en/docs/pytest/plugins' },
              ]
            }
          ],
          '/en/docs/typescript/': [
            {
              text: 'TypeScript',
              items: [
                { text: 'Introduction', link: '/en/docs/typescript/' },
                { text: 'Basic Types', link: '/en/docs/typescript/basic-types' },
                { text: 'Functions', link: '/en/docs/typescript/functions' },
                { text: 'Interfaces', link: '/en/docs/typescript/interfaces' },
                { text: 'Classes', link: '/en/docs/typescript/classes' },
                { text: 'Generics', link: '/en/docs/typescript/generics' },
              ]
            }
          ],
          '/en/courses/python-automation/': [
            {
              text: 'Python Automation',
              items: [
                { text: 'Course Overview', link: '/en/courses/python-automation/' },
              ]
            },
            {
              text: 'Phase 1: Python Basics',
              collapsed: false,
              items: [
                { text: '01. Setup & Basics', link: '/en/courses/python-automation/01-setup' },
                { text: '02. Strings & Control Flow', link: '/en/courses/python-automation/02-strings' },
                { text: '03. Loops', link: '/en/courses/python-automation/03-loops' },
                { text: '04. Lists & Dictionaries', link: '/en/courses/python-automation/04-lists-dicts' },
                { text: '05. Functions', link: '/en/courses/python-automation/05-functions' },
                { text: '06. Modules', link: '/en/courses/python-automation/06-modules' },
                { text: '07. Files & JSON', link: '/en/courses/python-automation/07-files-json' },
                { text: '08. Error Handling', link: '/en/courses/python-automation/08-error-handling' },
                { text: '09. Classes Part 1', link: '/en/courses/python-automation/09-classes-1' },
                { text: '10. Classes Part 2', link: '/en/courses/python-automation/10-classes-2' },
                { text: '11. Advanced Python', link: '/en/courses/python-automation/11-advanced-python' },
                { text: '12. Review & Setup', link: '/en/courses/python-automation/12-review' },
              ]
            },
            {
              text: 'Phase 2: Playwright',
              collapsed: true,
              items: [
                { text: '13. Playwright Setup', link: '/en/courses/python-automation/13-playwright-setup' },
                { text: '14. Navigation', link: '/en/courses/python-automation/14-navigation' },
                { text: '15. Locators Part 1', link: '/en/courses/python-automation/15-locators-1' },
                { text: '16. Locators Part 2', link: '/en/courses/python-automation/16-locators-2' },
                { text: '17. Form Handling', link: '/en/courses/python-automation/17-forms' },
                { text: '18. Mouse & Keyboard', link: '/en/courses/python-automation/18-mouse-keyboard' },
                { text: '19. Wait Strategies', link: '/en/courses/python-automation/19-waits' },
                { text: '20. Assertions', link: '/en/courses/python-automation/20-assertions' },
                { text: '21. Multiple Elements', link: '/en/courses/python-automation/21-multiple-elements' },
              ]
            },
            {
              text: 'Phase 3: Advanced',
              collapsed: true,
              items: [
                { text: '22. Frames & iframes', link: '/en/courses/python-automation/22-frames' },
                { text: '23. Multiple Pages', link: '/en/courses/python-automation/23-multiple-pages' },
                { text: '24. Screenshots & Video', link: '/en/courses/python-automation/24-screenshots-video' },
                { text: '25. Authentication', link: '/en/courses/python-automation/25-authentication' },
                { text: '26. Cookies & Storage', link: '/en/courses/python-automation/26-cookies-storage' },
                { text: '27. Network Interception', link: '/en/courses/python-automation/27-network' },
                { text: '28. API Testing', link: '/en/courses/python-automation/28-api-testing' },
                { text: '29. Page Object Model 1', link: '/en/courses/python-automation/29-pom' },
                { text: '30. Page Object Model 2', link: '/en/courses/python-automation/30-pom-2' },
              ]
            },
            {
              text: 'Phase 4: Pytest',
              collapsed: true,
              items: [
                { text: '31. Pytest Integration', link: '/en/courses/python-automation/31-pytest' },
                { text: '32. Test Configuration', link: '/en/courses/python-automation/32-test-config' },
                { text: '33. Test Data Management', link: '/en/courses/python-automation/33-test-data' },
                { text: '34. Parameterized Testing', link: '/en/courses/python-automation/34-parametrized' },
                { text: '35. Debugging', link: '/en/courses/python-automation/35-debugging' },
                { text: '36. Best Practices', link: '/en/courses/python-automation/36-best-practices' },
              ]
            },
          ],
          '/en/courses/typescript/': [
            {
              text: 'TypeScript Course',
              items: [
                { text: 'Course Overview', link: '/en/courses/typescript/' },
                { text: '01. What is TypeScript', link: '/en/courses/typescript/01-intro' },
                { text: '02. Basic Types', link: '/en/courses/typescript/02-basic-types' },
                { text: '03. Functions', link: '/en/courses/typescript/03-functions' },
              ]
            }
          ],
          '/en/cheatsheets/': [
            {
              text: 'Cheatsheets',
              items: [
                { text: 'Overview', link: '/en/cheatsheets/' },
                { text: 'Python', link: '/en/cheatsheets/python' },
                { text: 'Pytest', link: '/en/cheatsheets/pytest' },
                { text: 'Playwright', link: '/en/cheatsheets/playwright' },
                { text: 'Git', link: '/en/cheatsheets/git' },
              ]
            }
          ],
        },
        outline: {
          label: 'On this page'
        },
        docFooter: {
          prev: 'Previous',
          next: 'Next'
        },
        lastUpdated: {
          text: 'Last updated'
        },
        footer: {
          message: 'QA Learning Hub - Documentation and courses for QA automation',
          copyright: '© 2024'
        },
      }
    }
  },

  themeConfig: {
    logo: '/logo.svg',

    socialLinks: [
      { icon: 'github', link: 'https://github.com/opyrohov/python_automation_courses' }
    ],

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: 'Пошук',
                buttonAriaLabel: 'Пошук'
              },
              modal: {
                noResultsText: 'Нічого не знайдено',
                resetButtonTitle: 'Очистити',
                footer: {
                  selectText: 'вибрати',
                  navigateText: 'навігація',
                  closeText: 'закрити'
                }
              }
            }
          },
          en: {
            translations: {
              button: {
                buttonText: 'Search',
                buttonAriaLabel: 'Search'
              },
              modal: {
                noResultsText: 'No results found',
                resetButtonTitle: 'Clear',
                footer: {
                  selectText: 'select',
                  navigateText: 'navigate',
                  closeText: 'close'
                }
              }
            }
          }
        }
      }
    },
  }
})
