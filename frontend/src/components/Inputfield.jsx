import { useState } from 'react';
import '../variables.css';
import './Inputfield.css';

function Inputfield({ onChange, onClick }) {
    const [active, setActive] = useState(false);

    return (
        <div className="inputfield"
            style={ {background: active ? 'var(--color-primary)' : 'var(--color-secondary)'} }
        >
            <input
                style={ {background: active ? 'var(--color-primary)' : 'var(--color-secondary)'} }
                type="text"
                placeholder='write your query'
                onChange={ function (event) {setActive(event.target.value.length > 0); onChange(event.target.value)} }
            />
            <button onClick={onClick}>
                <div className="icon">
                    <svg width="13" height="18" viewBox="0 0 13 18" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M12.2519 8.16795C12.8457 8.56377 12.8457 9.43623 12.2519 9.83205L1.60763 16.9282C0.756192 17.4959 -0.297212 16.5697 0.156696 15.6526L3.2782 9.34559C3.41782 9.06347 3.41646 8.73208 3.27453 8.45111L0.212198 2.38927C-0.251183 1.47202 0.804403 0.536268 1.65947 1.10631L12.2519 8.16795Z"
                            // fill="#E20074"
                            fill={ active ? 'var(--color-primary)' : 'var(--color-secondary)'}
                        />
                    </svg>
                </div>
            </button>
        </div>
    );
}

export default Inputfield