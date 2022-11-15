//128 версия выдает ошибки
import * as THREE from 'https://unpkg.com/three@0.127.0/build/three.module.js'
import {GLTFLoader} from 'https://unpkg.com/three@0.127/examples/jsm/loaders/GLTFLoader.js'
import {RGBELoader} from 'https://unpkg.com/three@0.127/examples/jsm/loaders/RGBELoader.js'


//camera - то, с помощью чего мы видим
//scene - отображение с объектами
//render - логика (записывается, где что находится в момент времени)

//
const scene = new THREE.Scene();
//70 - угол обзора, 2й арг - соотношение сторон
const camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.1, 100);
//
const renderer = new THREE.WebGLRenderer();

camera.position.set(12, 8, 30);


scene.background = new THREE.Color(0xD2691E);
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.gammaOutut = true;
document.body.appendChild(renderer.domElement)


//линия
const points = [
    new THREE.Vector2(0, 0),
    new THREE.Vector2(1, 1),
]

const material = new THREE.LineBasicMaterial({color: 0xffffff});
const geometryLine = new THREE.BufferGeometry().setFromPoints(points);
const line = new THREE.Line(geometryLine, material);
scene.add(line);

//3D модель

const loader = new GLTFLoader();
loader.load('./robot_model/adamHead.gltf', function(gltf) {
    console.log(gltf);
    
    
    const root = gltf.scene;
    
    root.position.set(0, 0, 0);
    root.scale.set(2.5, 2.5, 2.5);
    
    scene.add(root);
}, function(xhr) {
    console.log(xhr.loaded/xhr.total * 100 + "% lodaded");
}, function(err) {
    console.log("An error occured: " + err)
});

//куб с тенями

const material2 = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
const geometry2 = new THREE.BoxGeometry( 2, 2, 2 );
const cube2 = new THREE.Mesh( geometry2, material2 );
cube2.position.set(8, 8, 5);
scene.add( cube2 );

//куб с текстурой
var texture3 = new THREE.TextureLoader().load( './crate.gif' );
var material3 = new THREE.MeshBasicMaterial( { map: texture3 } );
const cube3 = new THREE.Mesh( geometry2, material3 );
cube3.position.set(5, 5, 5);
scene.add( cube3 );

//свет
let ambientLight = new THREE.AmbientLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.75);
scene.add(ambientLight);

let directionalLightBack = new THREE.DirectionalLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.25);
directionalLightBack.position.set(30, 100, 100);
scene.add(directionalLightBack);

let directionalLightFront = new THREE.DirectionalLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.25);
directionalLightFront.position.set(-30, 100, -100);
scene.add(directionalLightFront);




var clock = new THREE.Clock();
var angle = 0; // текущий угол
var angularSpeed = THREE.Math.degToRad(20); // угловая скорость - градусов в секунду
var delta = 0;
var radius = 20;

//функция, обновляющая сцену
function animate() {
    delta = clock.getDelta(); // getDelta() - возвращает интервал в долях секунды
    requestAnimationFrame(animate);

    camera.position.x = Math.cos(angle) * radius;
    camera.position.z = Math.sin(angle) * radius;
    angle += angularSpeed * delta; // приращение угла

    camera.lookAt(0, 0, 0);

    renderer.render(scene, camera);

    cube2.rotation.x += 0.01;
	cube2.rotation.y += 0.01;

	cube3.rotation.y += 0.03;

    
}
animate();