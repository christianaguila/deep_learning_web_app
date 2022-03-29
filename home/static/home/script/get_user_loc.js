$(document).ready(function(){
    $("#upload").click(function(){
        if(!navigator.geolocation){
            console.log("Your browser doesn't support geolocation feature")
        }else{
            navigator.geolocation.getCurrentPosition(getPosition)
        }
        
        function getPosition(pos){
            let lat = pos.coords.latitude;
            let long = pos.coords.longitude;

            console.log(lat, long)

            $.ajax({
                url: "/coordinates/",
                data: { latitude: lat, longitude: long },
                type: "POST"
            })
        }
    })
})
                   