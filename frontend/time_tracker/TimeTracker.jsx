import RootComponent from '../RootComponent.jsx'

import React from 'react'
import ReactDOM from 'react-dom'
import '../node_modules/semantic-ui-css/semantic.min.css';

import { Header, Label, Container, Divider, Segment, Breadcrumb, Search, Table, Form, Dropdown, Select, Button } from 'semantic-ui-react'

export default class TimeTracker extends RootComponent {
    constructor(props) {
        super(props)
        this.state = {
            tasks: [],
            tasksAsOptions: [],
            selectedTask: null,
            selectedHours: null
        }
        this.ajaxCall('/tasks/jorge.bolco/crm', null, this.tasksOnSuccess)
    }

    tasksOnSuccess = (r, params) => {
        this.setState({tasks: r})
        this.setState({tasksAsOptions: this.tasksAsOptions(r)})
    }

    tasksAsOptions = (tasks) => {
        var tasks_as_options = []
        for (var i = 0; i < tasks.length; i++) {
            var option = {}
            option.text = tasks[i].description
            option.value = tasks[i].id
            tasks_as_options.push(option)
        }
        return tasks_as_options
    }

    tableContents = () => {
        var tasks = this.state.tasks
        var rows = []
        var i
        for (i = 0; i < tasks.length; i++) {
            var next_row = (
                  <Table.Row key={i}>
                    <Table.Cell>{tasks[i]["description"]}</Table.Cell>
                    <Table.Cell>{tasks[i]["timeEstimated"]}</Table.Cell>
                    <Table.Cell>{tasks[i]["timeElapsed"]}</Table.Cell>
                    <Table.Cell>{tasks[i]["status"]}</Table.Cell>
                  </Table.Row>
              );
            rows.push(next_row)
        }
        return rows
    }

    taskTable = () => {
        return (
            <Table celled>
              <Table.Header>
                <Table.Row>
                  <Table.HeaderCell>Nombre</Table.HeaderCell>
                  <Table.HeaderCell>Estimado (horas)</Table.HeaderCell>
                  <Table.HeaderCell>Transcurrido (horas)</Table.HeaderCell>
                  <Table.HeaderCell>Estado</Table.HeaderCell>
                </Table.Row>
              </Table.Header>
              <Table.Body>
              {this.tableContents()}
              </Table.Body>
            </Table>
        )
    }

    handleSelectedTaskChange = (event, {value, name}) => {
        this.setState({selectedTask: value })
    }

    handleSelectedHoursChange = (event) => {
        this.setState({selectedHours: event.target.value})
    }

    taskOnSuccess = (r, params) => {
        this.ajaxCall('/tasks/jorge.bolco/crm', null, this.tasksOnSuccess)
    }

    handleClick = (event) => {
        var endpoint = '/task/' + this.state.selectedTask
        var body = {hours: this.state.selectedHours}
        this.ajaxCall(endpoint, body, this.taskOnSuccess)
    }

    addHoursSelector = () => {
        var options = this.state.tasksAsOptions
        console.log(options)
        return(
            <Form>
                <Form.Group widths='equal'>
                <Dropdown options={options}
                    onChange={this.handleSelectedTaskChange}
                    fluid selection placeholder='Seleccionar tarea' />
                <Form.Field inline>
                  <Label basic color='green' pointing='right'>
                    Horas a agregar
                  </Label>
                  <input type='number'
                    onChange={this.handleSelectedHoursChange} />
                </Form.Field>
                <Button size='small' onClick={this.handleClick}>
                    Agregar
                </Button>
                </Form.Group>
            </Form>
        )
    }

    render() {
        return (
            <Container>
            <Header size='huge'>PSA Spring CRM</Header>
            <Divider />
            <Breadcrumb>
              <Breadcrumb.Section link>Proyectos</Breadcrumb.Section>
              <Breadcrumb.Divider />
              <Breadcrumb.Section link>Spring CRM</Breadcrumb.Section>
            </Breadcrumb>
            <Header size='medium'>PSA - Time Tracker</Header>
            <Search />
            {this.taskTable()}
            {this.addHoursSelector()}
            </Container>
        )
    }
}

ReactDOM.render(<TimeTracker />, document.getElementById('app'))
