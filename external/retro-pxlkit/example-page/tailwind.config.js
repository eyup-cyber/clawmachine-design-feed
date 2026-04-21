/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'retro-bg': '#F2F0EB',
        'retro-text': '#1D1D20',
        'retro-border': '#1D1D20',
        'retro-primary': '#4F46E5', // Indigo
        'retro-secondary': '#FBBF24', // Amber
        'retro-accent': '#10B981', // Emerald
        'retro-muted': '#6B7280',
      },
      boxShadow: {
        'retro': '4px 4px 0px 0px rgba(29, 29, 32, 1)',
        'retro-hover': '2px 2px 0px 0px rgba(29, 29, 32, 1)',
      },
      fontFamily: {
        pixel: ['"Press Start 2P"', 'monospace'],
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
