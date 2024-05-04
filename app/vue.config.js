const webpack = require('webpack');

const {defineConfig} = require('@vue/cli-service');

module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
      proxy: 'http://localhost:6862'
      // proxy: {
      //   '/api': {
      //     target: 'http://localhost:6862',
      //     logLevel: 'debug'
      //   }
      // }
    },
    configureWebpack: {
        //process: {env: {}},
        plugins: [
            // fix "process is not defined" error:
            // (do "npm install process" before running the build)
            new webpack.ProvidePlugin({
              process: 'process/browser',
            }),
        ],
        resolve: {
            fallback: {
              crypto: require.resolve("crypto-browserify"),
              stream: require.resolve("stream-browserify"),
              process: require.resolve("process/browser"),
              vm: require.resolve("vm-browserify"),
            },
        },
    }
});