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
    devtool: 'eval',
}
