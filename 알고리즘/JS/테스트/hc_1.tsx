import React, { useState, useEffect } from "react";
import { createRoot } from "react-dom/client";

const AsyncParagraph = ({ dataVersion, loadData }) => {
  // view data
  const [paragraph, setParagraph] = useState("");

  // i prefer use useCallback to loadData (but it's test)
  useEffect(() => {
    loadData().then(setParagraph);
  }, [dataVersion, loadData]);

  return <p>{paragraph}</p>;
};

document.body.innerHTML = "<div id='root'></div>";
const root = createRoot(document.getElementById("root"));

root.render(
  <AsyncParagraph
    dataVersion="10"
    loadData={() => {
      return new Promise((resolve, reject) => {
        resolve("Data!");
      });
    }}
  />
);

setTimeout(() => console.log(document.getElementById("root").innerHTML), 300);
