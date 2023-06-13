import { defineStore } from 'pinia';


//예시코드임 나중에 수정
// store를 여러개 만들어도됨
export const useStore = defineStore('app', {
  state() {
    return {
      count: 0,
      name: 'John',
      isLoggedIn: false,
    };
  },
  getter:{
    getCount(state){
        return state.count
    }

  },
  actions: {
    increment() {
      this.count++;
    },
    decrement() {
      this.count--;
    },
    updateName(newName) {
      this.name = newName;
    },
    login() {
      this.isLoggedIn = true;
    },
    logout() {
      this.isLoggedIn = false;
    },
  },
});




//  공식문서 예제파일
export const useTodos = defineStore('todos', {
    state: () => ({
      /** @type {{ text: string, id: number, isFinished: boolean }[]} */
      todos: [],
      /** @type {'all' | 'finished' | 'unfinished'} */
      filter: 'all',
      // type will be automatically inferred to number
      nextId: 0,
    }),
    getters: {
      finishedTodos(state) {
        // autocompletion! ✨
        return state.todos.filter((todo) => todo.isFinished)
      },
      unfinishedTodos(state) {
        return state.todos.filter((todo) => !todo.isFinished)
      },
      /**
       * @returns {{ text: string, id: number, isFinished: boolean }[]}
       */
      filteredTodos(state) {
        if (this.filter === 'finished') {
          // call other getters with autocompletion ✨
          return this.finishedTodos
        } else if (this.filter === 'unfinished') {
          return this.unfinishedTodos
        }
        return this.todos
      },
    },
    actions: {
      // any amount of arguments, return a promise or not
      addTodo(text) {
        // you can directly mutate the state
        this.todos.push({ text, id: this.nextId++, isFinished: false })
      },
    },
  })