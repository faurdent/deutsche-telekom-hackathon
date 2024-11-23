import '../variables.css';
import './Inputfield.css';

function Inputfield() {
    return (
        <div className="inputfield">
            <input type="text" placeholder='Write your query here...'/>
            <button>Submit</button>
        </div>
    );
}

export default Inputfield