import DefaultTheme from 'vitepress/theme'
import Quiz from './components/Quiz.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('Quiz', Quiz)
  }
}
