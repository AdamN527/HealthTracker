import React from 'react';
import Navbar from "./components/Navbar/Navbar";
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import './App.css';
import HeroSection from './components/HeroSection';
import Home from './components/Pages/Home';
import Login from './components/Pages/Login';

function App() {

  return (
    <>
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home}/>
        <Route path='/login' exact component={Login}/>
      </Switch>
    </Router>
    </>
  );
}

export default App;
