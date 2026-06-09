import React from "react";
// ASSETS
import agendasus from "../assets/agendasus.svg";
// STYLES
import "./Presentation.css"

const Presentation = () => {
  return (
    <section className="presentation-container">
      <div className="presentation">
        <div className="brand-title">
          <img src={agendasus} alt="AgendaSUS logo" />
          <h2>
            <span className="green">Agenda</span>
            <span className="blue">SUS</span>
          </h2>
        </div>
        <div className="text">
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos
            commodi neque reprehenderit aspernatur, deleniti quis asperiores ex
            quasi, dicta exercitationem odit aperiam rem minus! Minima pariatur
            voluptas quisquam fugiat perferendis.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Presentation;
