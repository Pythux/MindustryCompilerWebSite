module.exports = {
    transpileDependencies: [
        'vuetify'
    ],
    chainWebpack: config => {
        config.plugins.delete('fork-ts-checker')
    },
    publicPath: process.env.NODE_ENV === 'production'
        ? '/MindustryCompiler/'
        : '/'
}
