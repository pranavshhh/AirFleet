import React, { Component } from "react";
import axios from "axios";

class EntryForm extends Component {
    handleChange(event) {
        this.setState({[event.target.name]:event.target.value})
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log(this.state.entry_name);
        axios
            .post("http://127.0.0.1:8000/create/", {
                entry_name: this.state.entry_name
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
            entry_name: " ",
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    render() {
        const { entry_name } = this.state;
        return (
            <form onSubmit={this.handleSubmit}>
                <div>
                    <input
                        type="text"
                        name="entry_name"
                        value={entry_name}
                        onChange={this.handleChange} 
                    />
                </div>
                <input type="submit" value="Submit" />
            </form>
        );
    }

}

export default EntryForm;