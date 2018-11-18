import RootComponent from '../RootComponent.jsx'

import React from 'react'
import ReactDOM from 'react-dom'
import '../node_modules/semantic-ui-css/semantic.min.css';

import { Message, Container, Divider } from 'semantic-ui-react'

export default class TimeTracker extends RootComponent {
    constructor(props) {
        super(props)
        this.state = {
        }
    }

    render() {
        return (
            <div>

            </div>
        )
    }
}

ReactDOM.render(<TimeTracker />, document.getElementById('app'))
