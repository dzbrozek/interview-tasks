import React from "react";
import ReactDOM from "react-dom";

const Clock = () => {
  // return current time
  return '12:25:33'
}

const rootElement = document.getElementById("root");
ReactDOM.render(
  <React.StrictMode>
    <Clock />
  </React.StrictMode>,
  rootElement
);
