import React, { Component } from 'react';

class EntryDetail extends Component {
    render() {
        const obj = this.props.entryDetail;
        return (
            <div style={{ color: "lightblue", border: "1px solid white"}}>
                <h4>{obj.pilot_name}</h4>
                <h5>
                    Flight Information: {obj.from_dest} {obj.to_dest} {obj.aircraft_reg} {obj.aircraft_icao}
                </h5>
                <h6>Time Information: {obj.flight_date} {obj.flight_duration}</h6>
                <p>Comments: {obj.remarks_and_endorsements}</p>
            </div>
        );
    }
}

export default EntryDetail;
