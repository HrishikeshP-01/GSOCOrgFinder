import './Organization.css';

function Organization(props) {
    return (
        <a href={props.org['Ideas Page']} className="org" target="_blank">
            <h3>{props.org['Org']}</h3>
            <div>{props.org['Technologies']}</div>
        </a>
    );
}

export default Organization;