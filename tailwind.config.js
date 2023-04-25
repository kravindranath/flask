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
      'beige': '#fcf8e3',
      'beige-dark': '#efead1',
      'purple': '#5a287d',
      'red': '#b21f2d',
      'yellow': '#fbbb21',
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
      'black': '#000',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      gridTemplateColumns: {
        '16': 'repeat(16, minmax(0, 1fr))',
      },
      gridColumn: {
        'span-13': 'span 13 / span 16',
        'span-14': 'span 14 / span 16',
        'span-15': 'span 15 / span 16',
        'span-16': 'span 16 / span 16',
      },
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

