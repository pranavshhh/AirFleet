import React, { Component } from "react";
import axios from "axios";

class EntryForm extends React.Component {
    handleChange(event) {
        this.setState({[event.target.name]:event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.state.pilot_name);
        axios
            .post("http://127.0.0.1:8000/create/", {
                pilot_name: this.state.pilot_name
            })
            .then((response) => {
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
            })
    }

    constructor(props) {
        super(props);
        this.state = {
            pilot_name: " ",
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    render() {
        const { pilot_name } = this.state;
        return (
            <form onSubmit={this.handleSubmit}>
                <div>
                    <input
                        type="text"
                        name="pilot_name"
                        value={pilot_name}
                        onChange={this.handleChange} 
                    />
                </div>
                <input type="submit" value="Submit" />
            </form>
        );
    }

}

export default EntryForm;