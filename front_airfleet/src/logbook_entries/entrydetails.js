import React, { Component } from 'react';

class EntryDetail extends Component{
    render(){
        const p = this.props.p
        return(
            <div>
                <h4>{p.id}</h4>
                <h4>{p.pilot_name}</h4>
                <h4>{p.aircraft_reg}</h4>
            </div>
            )
    }
}

export default EntryDetail