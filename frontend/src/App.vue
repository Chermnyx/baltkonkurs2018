<template>
  <div id="app">
    <nav>
      <div class="nav-wrapper navbar-fixed blue">
        <a href="#!" class="brand-logo center">
          NeoNevus
        </a>
      </div>
    </nav>
    <main>
      <router-view/>
    </main>
    <footer class="page-footer blue">
      <div class="footer-copyright">
        <div class="container">
          © 2018
        </div>
      </div>
    </footer>
  </div>

</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

main {
  flex: 1 0 auto;
}

.force-disabled {
  color: gray;
  pointer-events: none;
}

/* label focus color */
.input-field input[type='text']:focus + label {
  color: #1b5e20 !important;
}

/* label underline focus color */
.input-field input[type='text']:focus {
  border-bottom: 1px solid #1b5e20 !important;
  box-shadow: 0 1px 0 0 #1b5e20 !important;
}

[type='radio']:checked + label:after,
[type='radio'].with-gap:checked + label:after {
  background-color: #1b5e20 !important;
}

[type='checkbox']:checked + label:before {
  border-right-color: #1b5e20 !important;
  border-bottom-color: #1b5e20 !important;
}

/* icon prefix focus color */
.input-field .prefix.active {
  color: #1b5e20 !important;
}
</style>
