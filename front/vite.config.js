import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VitePWA({ 
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true
      },
      includeAssets: ['/icons/*'],
      manifest: {
        name: '바름',
        short_name: '바름',
        description: '건강의 시작 - 바름',
        theme_color: '#ffffff',
        icons: [
          {
            src: '/icons/android-chrome-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/icons/android-chrome-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      } 
    
    }),
  ],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      // 이미지 디렉토리에 대한 별칭 설정
      '@assets': path.resolve(__dirname, 'src/assets')
    }
  },
  server: {
    watch: {
      usePolling: true,
    },
    host:'0.0.0.0',
    proxy: {
      '/api': { 
        target: 'http://django:8000/api', 
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
        secure: false,
        ws: true
      }
    }
  },
})
