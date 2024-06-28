let scene, camera, renderer, rocket; // Define variables for scene, camera, renderer, and rocket

function parentWidth(elem) {
    return elem.parentElement.clientWidth;
}

function parentHeight(elem) {
    return elem.parentElement.clientHeight;
}

function init3D() {
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0xffffff);

    camera = new THREE.PerspectiveCamera(75, parentWidth(document.getElementById("3Drocket")) / parentHeight(document.getElementById("3Drocket")), 0.1, 1000);

    renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(parentWidth(document.getElementById("3Drocket")), parentHeight(document.getElementById("3Drocket")));

    document.getElementById('3Drocket').appendChild(renderer.domElement);

    // Rocket body (cylinder)
    const rocketBodyGeometry = new THREE.CylinderGeometry(
        0.4,   // Radius at the top of the cylinder
        0.4,   // Radius at the bottom of the cylinder (same as top for a straight cylinder)
        3.0,     // Height of the cylinder (made it longer)
        64    // Number of segments
    );

    // Thruster (cylinder)
    const thrusterGeometry = new THREE.CylinderGeometry(
        0.4,   // Radius at the top of the thruster (same as rocket body)
        0.3,   // Radius at the bottom of the thruster (smaller for thruster effect)
        0.4,   // Height of the thruster
        64    // Number of segments
    );

    // Cone on top (nose cone)
    const coneGeometry = new THREE.ConeGeometry(
        0.4,   // Radius of the base of the cone (matches the rocket body)
        0.75,  // Height of the cone (made it slightly longer)
        64    // Number of segments for the circular base
    );

    // Position the cone on top of the rocket body
    coneGeometry.translate(0, 1.875, 0); // Adjusted the translation to fit proportionally
    thrusterGeometry.translate(0, -1.7, 0);
    // Combine the geometries
    rocketBodyGeometry.merge(coneGeometry);
    rocketBodyGeometry.merge(thrusterGeometry);

    const rocketGeometry = rocketBodyGeometry;

   


    // Set the materials for different parts of the rocket
    

    // Create the rocket mesh using the multi-material
    

    
    const rocketMaterial = new THREE.MeshPhongMaterial({
        color: 0x04469A,          // Color of the rocket
        specular: 0xFFFFFF,       // Specular color
        shininess: 100,            // Shininess (adjust as needed)
        side: THREE.DoubleSide   // Ensure the material is visible from both sides
    });
    rocket = new THREE.Mesh(rocketGeometry, rocketMaterial);
    scene.add(rocket);
    const ambientLight = new THREE.AmbientLight(0xFFFFFF, 0.5); // Color, Intensity
    scene.add(ambientLight);
    camera.position.z = 5;
    renderer.render(scene, camera);
}

// Resize the 3D object when the browser window changes size
function onWindowResize() {
    camera.aspect = parentWidth(document.getElementById("3Dcube")) / parentHeight(document.getElementById("3Dcube"));
    camera.updateProjectionMatrix();
    renderer.setSize(parentWidth(document.getElementById("3Dcube")), parentHeight(document.getElementById("3Dcube")));
}

window.addEventListener('resize', onWindowResize, false);

// Create the 3D representation
init3D();

// Create events for the sensor readings
if (!!window.EventSource) {
    var source = new EventSource('/events');

    source.addEventListener('open', function (e) {
        console.log("Events Connected");
    }, false);

    source.addEventListener('error', function (e) {
        if (e.target.readyState != EventSource.OPEN) {
            console.log("Events Disconnected");
        }
    }, false);

    source.addEventListener('gyro_readings', function (e) {
        var obj = JSON.parse(e.data);
        document.getElementById("gyroX").innerHTML = obj.gyroX;
        document.getElementById("gyroY").innerHTML = obj.gyroY;
        document.getElementById("gyroZ").innerHTML = obj.gyroZ;

        // Change rocket rotation after receiving the readings
        rocket.rotation.x = obj.gyroY;
        rocket.rotation.z = obj.gyroX;
        rocket.rotation.y = obj.gyroZ;
        renderer.render(scene, camera);
    }, false);

    source.addEventListener('temperature_reading', function (e) {
        console.log("temperature_reading", e.data);
        document.getElementById("temp").innerHTML = e.data;
    }, false);

    source.addEventListener('accelerometer_readings', function (e) {
        console.log("accelerometer_readings", e.data);
        var obj = JSON.parse(e.data);
        document.getElementById("accX").innerHTML = obj.accX;
        document.getElementById("accY").innerHTML = obj.accY;
        document.getElementById("accZ").innerHTML = obj.accZ;
    }, false);
}

function resetPosition(element) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "/" + element.id, true);
    console.log(element.id);
    xhr.send();
}
