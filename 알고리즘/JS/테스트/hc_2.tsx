import React, { useState, useContext, createContext } from "react";
import { createRoot } from "react-dom/client";

let ThemeContext = createContext();

const Content = () => {
  // Dependacy Insection context to ThemeContext
  const context = useContext(ThemeContext);

  return (
    <section className={`theme-${context.theme}`}>
      <span>Current theme: {context.theme}</span>
      <button onClick={context.switchTheme}>Switch Theme</button>
    </section>
  );
};

function App() {
  const [theme, setTheme] = useState("dark");
  const switchTheme = () => {
    theme === "dark" ? setTheme("light") : setTheme("dark");
  };
  return (
    <ThemeContext.Provider value={{ theme, switchTheme }}>
      <Content />
    </ThemeContext.Provider>
  );
}

document.body.innerHTML = "<div id='root'></div>";
const root = createRoot(document.getElementById("root"));
root.render(<App />);
