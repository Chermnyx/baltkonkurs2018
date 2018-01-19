<template>
  <div>
    <div class="login-form">

      <div class="input-field col s12">
        <h4 class="center-align">Введите данные пациента</h4>
      </div>
    </div>

    <div class="input-field col s12">
      <input id="firstName" v-model="store.registrationForm.firstName" type="text" class="reg-form">
      <label for="firstName">Имя</label>
    </div>

    <div class="input-field col s12">
      <input id="lastName" v-model="store.registrationForm.lastName" class="reg-form" type="text">
      <label for="lastName">Фамилия</label>
    </div>
    <span>Пол</span>
    <p>
      <input name="sex" v-model="store.registrationForm.sex" type="radio" value="male" id="Male" />
      <label class="reg-form" for="Male">Мужчина</label>
    </p>
    <p>
      <input name="sex" v-model="store.registrationForm.sex" type="radio" value="female" id="Female" />
      <label class='reg-form' for="Female">Женщина</label>
    </p>
    Согласие на обработку персональных данных
    <p>
      <input type="checkbox" v-model="processsingAgreed" id="processsingAgreed">
      <label for="processsingAgreed" class="reg-form flo-text">Я даю согласие на обработку моих персональных данных</label>
    </p>
    <div class="input-field">
      <button @click="onContinueClick" class="btn waves-effect waves-light green darken-4" :class="{ 'disabled': ! canContinue }">Продолжить</button>
      <!-- TODO: Error when one of the inputs empty -->
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  data: () => ({
    store: window.store,
    processsingAgreed: false
  }),
  methods: {
    onContinueClick() {
      if (!this.store.test.testUndone) {
        this.store.test.testUndone = true
      }
      this.store.registerDone = true
      setTimeout(() => {
        $('.collapsible').collapsible('open', 1)
      }, 1)
    }
  },
  computed: {
    canContinue() {
      return (
        this.processsingAgreed &&
        Object.values(this.store.registrationForm).every(
          x => x !== null && x !== undefined && x !== '' && x !== []
        )
      )
    }
  }
}
</script>
