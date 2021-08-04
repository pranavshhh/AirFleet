import logo from './plane.svg';
import './App.css';
import EntryList from './logbook_entries/entrylist';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Web App for Pilots of all kinds.
        </p>
        <h1
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Create an AirFleet Account
        </h1>
        <EntryList/>
      </header>
    </div>
  );
}

export default App;
