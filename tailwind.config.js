/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.{html,js}'], // add your preferred file extensions here,
  theme: {
    screens: {
      sm: '480px',
      md: '768px',
      lg: '976px',
      xl: '1440px',
    },
    colors: {
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'pink': '#ff49db',
      'orange': '#ff7849',
      'green': '#13ce66',
      'yellow': '#ffc82c',
      'gray-dark': '#273444',
      'gray': {
        '100': '#F8F8F8',
        '200': '#E0E0E0',
        '300': '#C8C8C8',
        '400': '#888888',
        '500': '#707070',
        '600': '#505050',
        '700': '#383838',
        '800': '#282828',
        '900': '#101010',
      },
      'white': '#fff',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        '128': '32rem',
        '144': '36rem',
      },
      borderRadius: {
        '4xl': '2rem',
      }
    }
  },
  plugins: [],
}

