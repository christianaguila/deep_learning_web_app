
var gmarkers =[];

function initMap(){
    var map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: parseFloat(12.87), lng: parseFloat(121.77)},
        zoom: 7,
        mapId: "71573f5f2187c47d",
        gestureHandling: "cooperative",
        restriction: {
            latLngBounds: {north: parseFloat(18.5), south: parseFloat(4.5), west: parseFloat(115), east: parseFloat(130)},
            strictBounds: false,
          },
      });

      


    const markers = [
        ["Anahaw (General Luna, Llanera, Nueva Ecija)", 15.631885308825185, 120.99981832037325, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (Pinagrealan, Candelaria, Zambales)", 15.609569373943357, 120.12120123700828, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw" ],
        ["Anahaw (Tubotubo North, Zambales)", 15.767376396402343, 120.00030385151615, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (General Mamerto Natividad, Nueva Ecija)", 15.588680, 120.984558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (Maniniog, Mayantoc, Tarlac)", 15.588680, 120.34558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (Sampaloc, Talavera, Nueva Ecija)", 15.588680, 120.934558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (Esguerra, Talavera, Nueva Ecija)", 15.592680, 120.923558, "/static/home/images/icons/map_anahaw.png", 30, 30], "Anahaw",
        ["Anahaw (Umangan, Aliaga, Nueva Ecija)", 15.523480, 120.923558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        ["Anahaw (Pula, Nueva Ecija)", 15.5889780,120.984558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Timmaguab, Santa Ignacia, Tarlac)", 15.588680, 120.45768, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Pinagrealan, Candelaria, Zambales)", 15.588680, 120.097678, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Maniniog, Mayantoc, Tarlac)", 15.588680, 120.345321, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Maniniog, Mayantoc, Tarlac)", 15.588680, 120.264647, "/static/home/images/icons/map_anahaw.png", 30, 30], "Anahaw",
        // ["Anahaw (General Mamerto Natividad, Nueva Ecija)", 15.588680, 120.984558, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Sacpil, Conner, Apayao)", 17.665516801317917, 121.24096507754436, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Ripang - Old Pob., Conner, Apayao)", 17.765516801317917, 121.25096507754436, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Guinaang, Conner, Apayao)", 17.865516801317917, 121.22096507754436, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],
        // ["Anahaw (Lenneng - Liyyeng, Kabugao, Apayao)", 17.965516801317917, 121.26096507754436, "/static/home/images/icons/map_anahaw.png", 30, 30, "Anahaw"],

        ["Agi (Tuguegarao, Cagayan", 17.61309674, 121.7268746, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Accusilian, Cagayan", 17.74791000, 121.46254000, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Aurora, Cagayan)", 16.99065000, 121.63664000, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Basco, Cagayan)", 20.44865000, 121.97017000, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Matnog, Sorsogon)", 12.6077, 124.0578, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Dupitac, Piddig, Ilocos Norte)", 18.166670, 120.750000, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Santo Niño, Bontoc, Southern Leyte)", 10.350000, 124.966670, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Pan-Philippine Hwy, Mandaluyong, Metro Manila)", 14.577470, 121.050880, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Umangan, Aliaga, Nueva Ecija)", 15.523480, 120.923558, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Pula, Nueva Ecija)", 15.5889780,120.984558, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Gregorio Pimentel, Diffun, Quirino)", 16.588680, 121.45768, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Picaleon, Nueva Ecija)", 15.588680, 121.097678, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (San Teodoro, Batangas)", 13.833330, 121.000000, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Santo Tomas, Calauan, Laguna)", 14.166670, 121.333330, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (General Mamerto Natividad, Nueva Ecija)", 15.588680, 120.984558, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Sacpil, Conner, Apayao)", 17.665516801317917, 121.24096507754436, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Ripang - Old Pob., Conner, Apayao)", 17.765516801317917, 121.25096507754436, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Guinaang, Conner, Apayao)", 17.865516801317917, 121.22096507754436, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],
        ["Agi (Lenneng - Liyyeng, Kabugao, Apayao)", 17.965516801317917, 121.26096507754436, "/static/home/images/icons/map_agi.png", 30, 30, "Agi"],

        ["Bignay (Lupi, Camarines Sur)", 13.882498964639023, 122.8666174870637, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Maguibuay, Quezon)", 14.007284, 122.762966, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Cawayan, Lopez, Quezon)", 13.839526, 122.330939, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_bignay.png", 30, 30], "Bignay",
        ["Bignay (Ligao, Albay)", 13.164658, 123.498773, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (San Pablo, Catanauan, Quezon)", 13.687790, 122.363231, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Villa Aurin, San Narciso, Quezon)",13.535730, 122.528019, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Pawa, Boac, Marinduque)", 13.450028, 121.891819, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Sibuyao, Marinduque)", 13.358519, 122.034520, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (San Antonio Magkupa, Catanauan, Quezon)", 13.667662, 122.355278, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Aslong, Libmanan, Camarines Sur)", 13.683406, 123.029966, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Balantay, Masbate)", 12.173031, 123.822714, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Libas, Masbate)", 12.009228, 123.821623, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Dona Maria - Kangkuirina, Leyte)", 10.956956, 124.763934, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Mag-aso, La Paz, Leyte)", 10.878758, 124.914845, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Kahupian, Southern Leyte)",10.506663, 125.014735, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Canha-ayon, Leyte)", 10.453975, 124.889006, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (GVV5+M6 Asturias, Cebu)", 10.544192, 123.858007, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],
        ["Bignay (Duangan, Balamban, Cebu)", 10.459079, 123.758712, "/static/home/images/icons/map_bignay.png", 30, 30, "Bignay"],

        ["Bagawak Morado (Santa Rosa, Laguna)", 14.2843, 121.0889, "/static/home/images/icons/map_bagawakmorado.png", 30, 30, "Bagawak Morado"],
        ["Bagawak Morado (Calamba, Laguna)", 14.1877, 121.1251, "/static/home/images/icons/map_bagawakmorado.png", 30, 30, "Bagawak Morado"],
        ["Bagawak Morado (Pampanga)", 15.0794, 120.6200, "/static/home/images/icons/map_bagawakmorado.png", 30, 30, "Bagawak Morado"],

        ["Kalingag (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_kalingag.png", 30, 30, "Kalingag"],
        ["Kalingag (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_kalingag.png", 30, 30, "Kalingag"],

        ["Katmon (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_katmon.png", 30, 30, "Katmon"],
        ["Katmon (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_katmon.png", 30, 30, "Katmon"],

        ["Kris Plant (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_krisplant.png", 30, 30, "Kris Plant"],
        ["Kris Plant (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_krisplant.png", 30, 30, "Kris Plant"],

        ["Payau (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_payau.png", 30, 30, "Payau"],
        ["Payau (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_payau.png", 30, 30, "Payau"],

        ["Copeland's Pitcher (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_pitcher.png", 30, 30, "Copeland's Pitcher"],
        ["Copeland's Pitcher (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_pitcher.png", 30, 30, "Copeland's Pitcher"],

        ["Tayabak (Sumalang, Lopez, Quezon)",13.763071870841916, 122.33397311298609, "/static/home/images/icons/map_tayabak.png", 30, 30, "Tayabak"],
        ["Tayabak (Palong, Libmanan, Camarines Sur)", 13.675021, 122.967060, "/static/home/images/icons/map_tayabak.png", 30, 30, "Tayabak"],


        ];


    // ------------------ Marker Loop ---------------------//

    for(let i = 0; i<markers.length; i++){
        const currMarker = markers[i]

        const marker = new google.maps.Marker({
            position: {lat: parseFloat(currMarker[1]), lng: parseFloat(currMarker[2])},
            map,
            title: currMarker[0],
            icon: {
                url:currMarker[3],
                scaledSize: new google.maps.Size(currMarker[4], currMarker[5])
            },
            category: currMarker[6],
            animation: google.maps.Animation.DROP,
            });

            // marker.category = markers[i];
            gmarkers.push(marker);

            

        const infowindow = new google.maps.InfoWindow({
                content: currMarker[0],
        });
        marker.addListener("click", toggleBounce)

    // ------------------ Information Window Loop ---------------------//
        function toggleBounce() {
            if (marker.getAnimation() !== null) {
              marker.setAnimation(null);
            } else {
              marker.setAnimation(google.maps.Animation.BOUNCE);
              setTimeout(function(){ marker.setAnimation(null); }, 1400);
            }
          }
            // marker.addListener("click", () => {
            //     infowindow.open({
            //     anchor: marker,
            //     map,
            //     shouldFocus: true,
            //     });
            //     map.panTo(this.getPosition());
            //     map.setZoom(15);
            // });


            marker.addListener('click', function () {
                if (infowindow) { infowindow.close();}
                console.log('Gmarker 1 gets pushed');
                infowindow.open(map, marker);
                map.panTo(this.getPosition());
                map.setZoom(11);
                window.setTimeout(function() {map.setZoom(map.getZoom());},3000);
            });

        }
    

        filterMarkers = function (category) {
            for (i = 0; i < markers.length; i++) {
                markerval = gmarkers[i];
                // If is same category or category not picked
                if (markerval.category == category || category.length === 0) {
                    markerval.setVisible(true);
                }
                // Categories don't match 
                else {
                    markerval.setVisible(false);
                }
            }
        }
    
    }
