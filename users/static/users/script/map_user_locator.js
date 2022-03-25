function initMap() {
  const initialPosition = {lat: 15.094328432675029, lng: 121.04979055635714};
  
  const map = new google.maps.Map(document.getElementById('mapuserlocator'), {
      center: initialPosition,
      zoom: 9,
      mapId: 'ba17d8d80d24f5da'
      });
  
    if(!navigator.geolocation){
      console.log("Your browser doesn't support geolocation feature")
    }else{
      navigator.geolocation.getCurrentPosition(getPosition)
    }

  function getPosition(pos){
    let lat = pos.coords.latitude
    let long = pos.coords.longitude
    /* newCoord = [];
    newCoord.push(lat);
    newCoord.push(long);
    return newCoord */

    marker = new google.maps.Marker({
        position: {lat: lat, lng: long},
        map,
        title: "Anahaw",
      });
      
    map.panTo({lat : lat, lng: long}); 
  }
} 