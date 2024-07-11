/** @type {import('tailwindcss').Config} */
const colors = require('tailwindcss/colors');

module.exports = {
  content: [
    './templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        cyan: colors.cyan,
        teal: colors.teal,
      }
    },
  },
  plugins: [
    require('flowbite/plugin'),
    require('@tailwindcss/forms'),
  ],
}
