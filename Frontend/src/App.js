import logo from './assets/logo.png';
import './App.css';
import Organization from './Organization';
import Search from "./Search";
import axios from 'axios';
import qs from 'qs';

function App() {
    const onSearch = (technologies) => {
        console.log(technologies)
        var qs=require('qs')
        axios.post('http://127.0.0.1:8000/find/',qs.stringify({'technologies':technologies}))
        axios.get('http://127.0.0.1:8000/find/').then(function(response){
          console.log(response)
        })
    }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>

        <main className="body">
            <div>
                <h2>Organizations</h2>
                <div className="organizations">
                    <Organization />
                </div>
            </div>

            <div>
                <h2>Search</h2>
                <Search onSearch={onSearch} />
            </div>
        </main>
    </div>
  );
}

export default App;
