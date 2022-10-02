/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {},
  },
  plugins: [
    function ({ addVariant }) {
      addVariant('child', '& > *');
      addVariant('child-hover', '& > *:hover');
    },
    require('@tailwindcss/forms'),
  ],
  variants: {
    extend: {
      opacity: ['disabled'],
      backgroundColor: ['odd', 'even'],
    },
  },
  safelist: [
    {
      pattern: /grid-col-*/,
    },
  ],
};
