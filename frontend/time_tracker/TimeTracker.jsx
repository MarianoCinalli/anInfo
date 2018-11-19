import RootComponent from '../RootComponent.jsx'

import React from 'react'
import ReactDOM from 'react-dom'
import '../node_modules/semantic-ui-css/semantic.min.css';

import { Header, Label, Container, Divider, Segment, Breadcrumb, Search, Table, Form, Dropdown, Select, Button } from 'semantic-ui-react'

export default class TimeTracker extends RootComponent {
    constructor(props) {
        super(props)
        this.state = {
        }
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
                <Table.Row>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                  <Table.Cell>Cell</Table.Cell>
                </Table.Row>
              </Table.Body>

            </Table>
        )
    }

    addHours = () => {
        return(
            <Form>
                <Form.Group widths='equal'>
                <Dropdown fluid selection placeholder='Seleccionar tarea' />
                <Form.Field inline>
                  <Label basic color='green' pointing='right'>
                    Horas a agregar
                  </Label>
                </Form.Field>
                <Button size='small'> Agregar </Button>
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
            {this.addHours()}
            </Container>
        )
    }
}

ReactDOM.render(<TimeTracker />, document.getElementById('app'))
