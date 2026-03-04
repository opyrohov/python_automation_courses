<script setup lang="ts">
import { ref, computed } from 'vue'

interface Question {
  question: string
  options: string[]
  correct: number
  explanation: string
}

const props = defineProps<{
  questions: Question[]
}>()

const current = ref(0)
const selected = ref<number | null>(null)
const answered = ref(false)
const score = ref(0)
const finished = ref(false)

const total = computed(() => props.questions.length)
const q = computed(() => props.questions[current.value])
const progress = computed(() => ((current.value + 1) / total.value) * 100)

function select(index: number) {
  if (answered.value) return
  selected.value = index
  answered.value = true
  if (index === q.value.correct) {
    score.value++
  }
}

function next() {
  if (current.value + 1 < total.value) {
    current.value++
    selected.value = null
    answered.value = false
  } else {
    finished.value = true
  }
}

function restart() {
  current.value = 0
  selected.value = null
  answered.value = false
  score.value = 0
  finished.value = false
}

function optionClass(index: number) {
  if (!answered.value) return ''
  if (index === q.value.correct) return 'correct'
  if (index === selected.value) return 'incorrect'
  return ''
}

const emoji = computed(() => {
  const pct = score.value / total.value
  if (pct === 1) return '🏆'
  if (pct >= 0.8) return '🎉'
  if (pct >= 0.5) return '👍'
  return '💪'
})
</script>

<template>
  <div class="quiz">
    <!-- Results screen -->
    <div v-if="finished" class="quiz-result">
      <div class="result-emoji">{{ emoji }}</div>
      <div class="result-score">{{ score }} / {{ total }}</div>
      <div class="result-text" v-if="score === total">
        Excellent! Perfect score!
      </div>
      <div class="result-text" v-else-if="score >= total * 0.8">
        Great job! Almost perfect!
      </div>
      <div class="result-text" v-else-if="score >= total * 0.5">
        Good effort! Review the topics you missed.
      </div>
      <div class="result-text" v-else>
        Keep learning! Review the material and try again.
      </div>
      <button class="quiz-btn" @click="restart">
        🔄 Try again
      </button>
    </div>

    <!-- Question screen -->
    <div v-else>
      <div class="quiz-header">
        <span class="quiz-counter">{{ current + 1 }} / {{ total }}</span>
        <div class="quiz-progress">
          <div class="quiz-progress-bar" :style="{ width: progress + '%' }"></div>
        </div>
      </div>

      <div class="quiz-question">{{ q.question }}</div>

      <div class="quiz-options">
        <button
          v-for="(option, i) in q.options"
          :key="i"
          class="quiz-option"
          :class="optionClass(i)"
          :disabled="answered"
          @click="select(i)"
        >
          {{ option }}
        </button>
      </div>

      <div v-if="answered" class="quiz-explanation">
        <strong>{{ selected === q.correct ? '✅' : '❌' }}</strong>
        {{ q.explanation }}
      </div>

      <button v-if="answered" class="quiz-btn" @click="next">
        {{ current + 1 < total ? 'Next →' : 'Results →' }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.quiz {
  margin: 1.5rem 0;
  padding: 1.5rem;
  border: 1px solid var(--vp-c-divider);
  border-radius: 12px;
  background: var(--vp-c-bg-soft);
}

.quiz-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 1.25rem;
}

.quiz-counter {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--vp-c-text-2);
  white-space: nowrap;
}

.quiz-progress {
  flex: 1;
  height: 6px;
  background: var(--vp-c-divider);
  border-radius: 3px;
  overflow: hidden;
}

.quiz-progress-bar {
  height: 100%;
  background: var(--vp-c-brand-1);
  border-radius: 3px;
  transition: width 0.3s ease;
}

.quiz-question {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 1rem;
  line-height: 1.5;
  color: var(--vp-c-text-1);
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 1rem;
}

.quiz-option {
  padding: 12px 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  font-size: 0.95rem;
  text-align: left;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
}

.quiz-option:not(:disabled):hover {
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.quiz-option:disabled {
  cursor: default;
}

.quiz-option.correct {
  border-color: var(--vp-c-green-1, #10b981);
  background: var(--vp-c-green-soft, rgba(16, 185, 129, 0.1));
  color: var(--vp-c-green-1, #10b981);
  font-weight: 600;
}

.quiz-option.incorrect {
  border-color: var(--vp-c-red-1, #ef4444);
  background: var(--vp-c-red-soft, rgba(239, 68, 68, 0.1));
  color: var(--vp-c-red-1, #ef4444);
}

.quiz-explanation {
  padding: 12px 16px;
  border-radius: 8px;
  background: var(--vp-c-default-soft);
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 1rem;
  color: var(--vp-c-text-2);
}

.quiz-btn {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 10px 24px;
  border: none;
  border-radius: 8px;
  background: var(--vp-c-brand-1);
  color: #fff;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: background 0.2s;
}

.quiz-btn:hover {
  background: var(--vp-c-brand-2);
}

.quiz-result {
  text-align: center;
  padding: 2rem 1rem;
}

.result-emoji {
  font-size: 3rem;
  margin-bottom: 0.5rem;
}

.result-score {
  font-size: 2rem;
  font-weight: 700;
  color: var(--vp-c-brand-1);
  margin-bottom: 0.5rem;
}

.result-text {
  font-size: 1rem;
  color: var(--vp-c-text-2);
  margin-bottom: 1.5rem;
}
</style>
