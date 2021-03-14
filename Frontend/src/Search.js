import React, { useState } from 'react';
import axios from 'axios';
import './Search.css';

function Search(props) {
    const [username, setUsername] = useState();

    const search = () => {
        axios.get(`https://api.github.com/users/${username}/repos`)
            .then(({data}) => {
                if (!data.length) return alert('Invalid username');
                let languages = {}
                data.forEach(repo => {
                    if (!languages[repo.language]) languages[repo.language] = 0;
                    languages[repo.language]++;
                })

                if (!Object.values(languages).length) return alert('This user does not have any repositories');
                props.onSearch(Object.keys(languages));
            })
    }

    return (
        <div className="search">
            <input type="text" placeholder="GitHub username..." value={username} onChange={event => setUsername(event.target.value)}/>

            <button onClick={search}>Search</button>
        </div>
    )
}

export default Search;