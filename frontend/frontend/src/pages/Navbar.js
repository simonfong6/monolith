import React from "react"; import { Link } from "react-router-dom";
import './Navbar.css';

function Navbar() {
  return (
    <nav className="Navbar navbar navbar-expand-sm bg-body-tertiary">
      <div className="container-fluid">
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link active" to="/">Index</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" aria-current="page" to="/home">Home</Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/posts">Posts</Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
