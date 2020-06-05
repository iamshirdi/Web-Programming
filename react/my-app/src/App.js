import React from 'react';
import poster  from './poster.mp4';
import './App.css';
import Carousel from './Carousel';
import 'react-responsive-carousel/lib/styles/carousel.min.css';
import "./Carousel.css";



function App() {
  return (
    <div className="App">

      <header className="App-header">

      <div className="video-container">
        <video src={poster} width="100%" height="100%" style={{objectFit:"cover"}} autoplay="true" loop="true">  </video>

        <div className="text-container">
          <div style={{fontSize:"64px", textTransform: 'uppercase'}}>Abbas Live </div>
          <div style={{fontSize:"20px",  textTransform: 'uppercase' }}>streams from around the world</div>
        </div>
        </div>

      </header>


      <div style={{display:"flex",width:"100%",justifyContent:"space-around",padding:"40px"}}>
      <div style={{fontSize:"20px", textTransform: 'uppercase',color:"black"}}>selected streams</div>
      <div  style={{fontSize:"20px", color:'#919597'}}>Scheduled streams thats coming up</div>
      </div>


      <div className="carousel_container">
      <Carousel />

        </div>
        <div style={{display:"flex",width:"100%",justifyContent:"space-around",padding:"40px"}}>
        <div style={{fontSize:"20px", textTransform: 'uppercase',color:"black"}}>live streams</div>
        <div  style={{fontSize:"20px", color:'#919597'}}>The most viewers right now on Twitch & Youtube</div>
        </div>


  </div>

  );
}

export default App;
