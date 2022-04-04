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

  async function getPosition(pos){
    let lat = pos.coords.latitude
    let long = pos.coords.longitude
    
    const response = await fetch(
      "https://geocode.arcgis.com/arcgis/rest/services/World/GeocodeServer/reverseGeocode?f=pjson&featureTypes=&location=" + `${long},${lat}`
    );

    const data = await response.json();
    let userAddress = data.address.Match_addr;

    $.ajax({
      url: "/coordinates/",
      data: { latitude: lat, longitude: long , address: userAddress},
      type: "POST"
  })

    marker = new google.maps.Marker({
        position: {lat: lat, lng: long},
        map,
        title: userAddress,
      });
      
    map.panTo({lat : lat, lng: long}); 
  }
} 
