import React from "react";
import ReactDOM from "react-dom";

function addLeadingZero(i) {
  if (i < 10) {
    return `0${i}`;
  }
  return i;
}

const displayTime = (date) => {
  const h = date.getHours();
  const m = addLeadingZero(date.getMinutes());
  const s = addLeadingZero(date.getSeconds());

  return `${h}:${m}:${s}`;
}


const Clock = () => {
  const [time, setTime] = React.useState(new Date());

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return displayTime(time);
}

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <Clock />
  </React.StrictMode>,
  rootElement
);
