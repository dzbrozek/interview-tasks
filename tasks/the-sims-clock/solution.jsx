import React from "react";
import ReactDOM from "react-dom";

const displayTime = (date) => {
  const h = date.getHours();
  const m = date.getMinutes();
  const s = date.getSeconds();

  return `${h}:${m}:${s}`;
}

const ClockMode = {
  pause: 0,
  speed1x: 1,
  speed2x: 2,
  speed3x: 3
}

const Clock = () => {
  const [time] = React.useState(new Date());
  const [offset, setOffset] = React.useState(0);
  const [mode, setMode] = React.useState(ClockMode.speed1x);

  React.useEffect(() => {
    if(mode === ClockMode.pause) {
      return;
    }

    const intervalId = setInterval(() => {
      setOffset((state) => state +1);
    }, 1000 / mode);

    return () => clearInterval(intervalId);
  }, [mode]);

  const currentTime = new Date();
  currentTime.setSeconds(time.getSeconds() + offset);

  return (
    <div>
      <p>
        {displayTime(currentTime)}
      </p>
      <p>
        <button onClick={() => setMode(ClockMode.pause)}>||</button>
        <button onClick={() => setMode(ClockMode.speed1x)}>1x</button>
        <button onClick={() => setMode(ClockMode.speed2x)}>2x</button>
        <button onClick={() => setMode(ClockMode.speed3x)}>3x</button>
      </p>
    </div>
  )
}

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <Clock />
  </React.StrictMode>,
  rootElement
);
