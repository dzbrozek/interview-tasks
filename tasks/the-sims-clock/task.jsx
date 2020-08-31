import React from "react";
import ReactDOM from "react-dom";

const displayTime = (date) => {
  const h = date.getHours();
  const m = date.getMinutes();
  const s = date.getSeconds();

  return `${h}:${m}:${s}`;
}

const Clock = () => {
  return (
    <div>
      <p>
        {displayTime(new Date())}
      </p>
      <p>
        <button>||</button>
        <button>1x</button>
        <button>2x</button>
        <button>3x</button>
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
