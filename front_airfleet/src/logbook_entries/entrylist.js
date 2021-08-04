import React, { Component } from 'react';
import EntryDetail from './entrydetails';
import axios from 'axios';

class EntryList extends Component{

    state = {
        entryData:[],
    }


    componentDidMount(){
        axios.get("http://127.0.0.1:8000")
        .then((response) => {
            this.setState({entryData: response.data})
        })
        .catch(function (error){
            console.log(error)
        })
    }

    render(){
        return(
            <div>
                {this.state.entryData.map( item => {
                return <h3>{item.pilot_name}, {item.flight_date}, {item.aircraft_reg}
                </h3>

                        })
                }
            </div>
            )
    }
}

export default EntryList;