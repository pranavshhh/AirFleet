import React, { Component } from 'react';
import EntryDetail from './entrydetail';
import axios from 'axios';
import EntryForm from './entryform'

class EntryList extends Component{
    constructor(props) {
        super(props);
        this.state = {
            entryData: [],
            entry: " ",
            showComponent: false,
        };
        this.getEntryDetail = this.getEntryDetail.bind(this);
        this.showEntryDetails = this.showEntryDetails.bind(this);  
    }

    getEntryDetail(item) {
        axios
            .get("http://127.0.0.1:8000".concat(item.absolute_url))
            .then((response) => {
                this.setState({ entry: response.data })
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    showEntryDetails(item) {
        this.getEntryDetail(item);
        this.setState({ showComponent: true })
    }

    componentDidMount() {
        axios
            .get("http://127.0.0.1:8000/")
            .then((response) => {
                this.setState({ entryData: response.data})
            })
            .catch(function (error){
                console.log(error)
            })
    }

    render(){
        return(
            <div>
                <EntryForm/>

                {this.state.entryData.map((item) => {
                    return (
                        <h3 key={item.id} onClick={() => this.showEntryDetails(item)}>
                            {item.pilot_name}, {item.from_dest}, {item.to_dest}, {item.flight_date}
                        </h3>
                    );
                })}

                {this.state.showComponent ? (
                    <EntryDetail entryDetail={this.state.entry} />
                ) : null}
            </div>
        );
    }
}

export default EntryList;