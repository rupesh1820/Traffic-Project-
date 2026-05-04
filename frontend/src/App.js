import { useState } from "react";

function App() {
  const [time, setTime] = useState("");
  const [day, setDay] = useState(1);
  const [weather, setWeather] = useState(0);
  const [result, setResult] = useState("");

  const predict = async () => {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ 
        time: Number(time), 
        day, 
        weather 
      }),
    });

    const data = await res.json();
    setResult(data.prediction);
  };

  return (
    <div style={{
      textAlign: "center",
      marginTop: "80px",
      fontFamily: "Arial"
    }}>
      <h1>🚦 Traffic Predictor</h1>

      <input 
        placeholder="Enter Time (0-23)"
        onChange={(e)=>setTime(e.target.value)}
      />
      <br/><br/>

      <select onChange={(e)=>setDay(Number(e.target.value))}>
        <option value={1}>Weekday</option>
        <option value={0}>Weekend</option>
      </select>
      <br/><br/>

      <select onChange={(e)=>setWeather(Number(e.target.value))}>
        <option value={0}>Sunny</option>
        <option value={1}>Cloudy</option>
        <option value={2}>Rainy</option>
      </select>
      <br/><br/>

      <button onClick={predict}>Predict</button>

      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;