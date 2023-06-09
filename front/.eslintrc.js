module.exports = {
    root:true,
    parserOptions: {
        parser: '@bable/eslint-parser',
    },
    env:{
        node:true,
        browser:true,
    },
    extends:[
        'eslint-recommended',
        'plugin:vue/vue3-recommended'
    ],
};