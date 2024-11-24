import Header from './components/Header.jsx';
import Inputfield from './components/Inputfield.jsx';
import './App.css';
import {
    VictoryChart,
    VictoryLine,
    VictoryTheme,
    VictoryArea,
    VictoryBar,
    VictoryBoxPlot,
    VictoryPie,
    VictoryScatter,
    VictoryCandlestick,
    VictoryZoomContainer,
    Scale,
    VictoryHistogram,
    // VictoryTheme
} from "victory";
import Footer from './components/Footer.jsx';
import { useState } from 'react';
import Button from './components/Button.jsx';

function App() {
    const [sampleData, setSampleData] = useState([]);
    const [showData, setDataVisibility] = useState(false);
    const [response, setResponse] = useState('');
    const [query, setQuery] = useState('');

    const fetchData = async () => {
        const response = await fetch(`http://localhost:8000/get-analytics?text=${query}`, {
            method: 'POST',
            // headers: {
            //     'Content-Type': 'application/json'
            // },
            // body: JSON.stringify({text: query})
        });
        console.log('Response:', response);
        console.log('query:', query);
        const data = await response.json();
        console.log('Data:', data);
        setResponse(data[0]['output']);
        setSampleData(data[1]);
        setDataVisibility(true);
    }
    
    return (
        <div>
            <Header />
            {
                !showData && 
                <div className="placeholder">
                    Please enter your query
                </div>
            }
            
            {
                showData &&
                <div className="content">
                    <div className="response">
                        <h2 className='response-title'>Response</h2>
                        <p>{response}</p>
                    </div>
                    <div className="graph">
                        <h2 className='graph-title'>Data</h2>
                        <VictoryChart here uncomment
                            domainPadding={{ x: 20 }}
                            theme={VictoryTheme.clean}
                            height={500}
                            width={800}
                            scale={{ x: "time" }}
                            containerComponent={
                                <VictoryZoomContainer
                                    allowZoom={true}
                                    allowPan={true}
                                    // zoomDomain={{
                                    //     // x: [5, 35],
                                    //     y: [0, 100],
                                    // }}
                                    zoomDimension="x"
                                />
                            }
                        >
                            <VictoryBar
                                data={sampleData}
                                style={{data: {fill: "var(--color-primary)"}}}
                            />
                        </VictoryChart>
                    </div>
                </div>
            }
            <div className='centering'>
                <Inputfield onChange={setQuery} onClick={fetchData} />
                <Button />
            </div>
            <Footer />
        </div>
    );
}

export default App
