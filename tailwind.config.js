module.exports = {
    content: [
        './templates/**/*.html',
        './**/*.html',
        './theme/static_src/**/*.{js,css}',
    ],
    theme: {
        extend: {
            fontFamily: {
                // Define your custom fonts here
                roboto: ['YourFontName', 'ui-sans-serif', 'system-ui'],
                serif: ['AnotherFontName', 'ui-serif', 'Georgia'],
            },
        },
    },
    plugins: [],
};
