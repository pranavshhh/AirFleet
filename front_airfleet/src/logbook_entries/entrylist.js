import React, { Component } from 'react';
import DummyData from './dummydata.json';

class EntryList extends Component{
    render(){
        return(
            <div>
                {DummyData.map( p =>
                    <h4>{p.pilot_name} : {p.from_dest} - {p.to_dest}</h4>
                    )
                }
            </div>
        )
    }
}

export default EntryList;