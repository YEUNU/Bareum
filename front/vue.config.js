const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    proxy: {
      '/api': {
        target: 'http://django:8000', // 백엔드 서버의 주소와 포트로연결
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
})