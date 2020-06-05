import React from "react";
import { Carousel } from "react-responsive-carousel";
import "./Carousel.css";
import 'react-responsive-carousel/lib/styles/carousel.min.css';


export default () => (
  <Carousel
  infiniteLoop
   centerMode
   centerSlidePercentage={50}
   selectedItem={1}
   showIndicators={false}
   swipeable={true}
   showThumbs={false}
  >
    <div>
    <a href="https://www.abbas.live/livestreams/yung-lean-live-the-back-of-the-truck">
      <video
        src="https://storage.googleapis.com/abbaslive/videos/Yl/yl-gif1%20(1).mp4"
        width="100%"
        height="100%"
        style={{ objectFit: "cover" }}
        autoplay="true"
        loop="true"      >
      </video>
      <h1 className="legend">YUNG LEAN <br></br>Apr 2 ⁠— 9:00 PM</h1>
      </a>
    </div>

    <div>
    <a href="https://www.abbas.live/livestreams/lorentz-stream">
    <video
         src="https://storage.googleapis.com/abbaslive/videos/Yl/yl-gif5.mp4"
         width="100%"
         height="100%"
         style={{ objectFit: "cover" }}
         autoplay="true"
         loop="true"
       >
       </video>
        <h1 className="legend">Wunna <br></br> June 7 ⁠— 8:00 PM</h1>
{/*
      <div class="overlay">
      <img
        src="https://uploads-ssl.webflow.com/5eb403f88cf2c6351e1455a0/5eba8165db6330597b32eebc_play.svg"
        style={{ verticalAlign: "middle" }}
        width="50px"
        height="50px"
      />
      </div>
*/}
        </a>
    </div>

    <div>
    <a href="https://www.abbas.live/livestreams/post-malone-x-nirvana-tribute">
    <video
      src="https://storage.googleapis.com/abbaslive/videos/Yl/yl-gif3.mp4"
      width="100%"
      height="100%"
      style={{ objectFit: "cover" }}
      autoplay="true"
      loop="true"    >
    </video>
    <h1 className="legend">Post Malone" <br></br> 25 April ⁠— 10:00 AM</h1>
    </a>
    </div>

  </Carousel>

);
