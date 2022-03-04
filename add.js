function sendPost(){
    const data = JSON.stringify({
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        elso: document.getElementById("elso").value,
        masodik:document.getElementById("masodik").value,
        szoveg:document.getElementById("szoveg").value,
        

      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/savedetails/', data);
      console.log(data);
    }