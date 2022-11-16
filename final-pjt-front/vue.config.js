const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: [
    'vuetify'
  ],
  // css: {
  //   loaderOptions: {
  //       sass: {
  //         additionalData: `@import "@/assets/_variables.sass";`
  //       },
  //       scss: {
  //         additionalData: `@import "@/assets/_variables.scss";`
  //       },
  //   }
  // }
})

const globalSassFiles = [
  './src/assets/_variables.scss',
]

module.exports = {
  chainWebpack: config => {
      const oneOfsMap = config.module.rule('scss').oneOfs.store
      oneOfsMap.forEach(item => {
          item
              .use('sass-resources-loader')
              .loader('sass-resources-loader')
              .options({
                  resources: globalSassFiles
              })
              .end()
      })
  }
}