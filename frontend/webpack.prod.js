const webpack = require('webpack');

const MinifyPlugin = require("babel-minify-webpack-plugin");

module.exports = {
    entry: {
        TimeTracker: './time_tracker/TimeTracker.jsx',
    },
    output: {
        filename: '[name].js',
        path: __dirname + '/static'
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /(node_modules)/,
                use: {
                    loader: 'babel-loader',
                }
            },
            {
                test: /\.css$/,
                loader: 'style-loader!css-loader'
            },
            {
                test: /\.(png|woff|woff2|eot|ttf|svg)$/,
                loader: 'url-loader?limit=100000'
            }
        ]
    },
    watchOptions: {
        poll: true
    },
    devtool: 'cheap-module-source-map ',
    plugins: [
        new webpack.DefinePlugin({
            'process.env': {
                'NODE_ENV': JSON.stringify('production')
            }
        }),
        new MinifyPlugin()
    ],
}
