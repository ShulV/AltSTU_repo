// // //128 версия выдает ошибки
import * as THREE from 'https://unpkg.com/three@0.127.0/build/three.module.js'
import { OrbitControls } from 'https://unpkg.com/three@0.127/examples/jsm/controls/OrbitControls'
import { OrbitControls } from 'https://unpkg.com/three@0.127/examples/jsm/controls/OrbitControls'
import {GLTFLoader} from 'https://unpkg.com/three@0.127/examples/jsm/loaders/GLTFLoader.js'
import {RGBELoader} from 'https://unpkg.com/three@0.127/examples/jsm/loaders/RGBELoader.js'


function main() {
  //
  const canvas = document.getElementById('c')
  //

  //визуализатор (создает изображение по модели) -------------------------------------------------------------
  const renderer = new THREE.WebGLRenderer({canvas});
  //----------------------------------------------------------------------------------------------------------


  //Камера ---------------------------------------------------------------------------------------------------
  const fov = 45; //Вертикальное поле зрения усеченной камеры.
  const aspect = 2; //Соотношение сторон усеченной пирамиды камеры
  const near = 0.1; //Расстяние до ближайшей границы отображения
  const far = 1000; //Расстяние до дальней границы отображения
  const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
  camera.position.set(0, 10, 20);
  //----------------------------------------------------------------------------------------------------------


// //camera - то, с помощью чего мы видим
// //scene - отображение с объектами
// //render - логика (записывается, где что находится в момент времени)

// //
// const scene = new THREE.Scene();
// //70 - угол обзора, 2й арг - соотношение сторон
// const camera = new THREE.PerspectiveCamera(70, window.innerWidth / window.innerHeight, 0.1, 100);
// //
// const renderer = new THREE.WebGLRenderer();

// camera.position.set(12, 8, 30);


// scene.background = new THREE.Color(0xD2691E);
// renderer.setSize(window.innerWidth, window.innerHeight);
// renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
// renderer.shadowMap.enabled = true;
// renderer.gammaOutut = true;
// document.body.appendChild(renderer.domElement)


// //линия
// const points = [
//     new THREE.Vector2(0, 0),
//     new THREE.Vector2(1, 1),
// ]

// const material = new THREE.LineBasicMaterial({color: 0xffffff});
// const geometryLine = new THREE.BufferGeometry().setFromPoints(points);
// const line = new THREE.Line(geometryLine, material);
// scene.add(line);

// //3D модель

// const loader = new GLTFLoader();
// loader.load('./robot_model/adamHead.gltf', function(gltf) {
//     console.log(gltf);
    
    
//     const root = gltf.scene;
    
//     root.position.set(0, 0, 0);
//     root.scale.set(2.5, 2.5, 2.5);
    
//     scene.add(root);
// }, function(xhr) {
//     console.log(xhr.loaded/xhr.total * 100 + "% lodaded");
// }, function(err) {
//     console.log("An error occured: " + err)
// });

// //куб с тенями

// const material2 = new THREE.MeshPhongMaterial( { color: 0xffffff, flatShading: true } );
// const geometry2 = new THREE.BoxGeometry( 2, 2, 2 );
// const cube2 = new THREE.Mesh( geometry2, material2 );
// cube2.position.set(8, 8, 5);
// scene.add( cube2 );

// //куб с текстурой
// var texture3 = new THREE.TextureLoader().load( './crate.gif' );
// var material3 = new THREE.MeshBasicMaterial( { map: texture3 } );
// const cube3 = new THREE.Mesh( geometry2, material3 );
// cube3.position.set(5, 5, 5);
// scene.add( cube3 );

// //свет
// let ambientLight = new THREE.AmbientLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.75);
// scene.add(ambientLight);

// let directionalLightBack = new THREE.DirectionalLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.25);
// directionalLightBack.position.set(30, 100, 100);
// scene.add(directionalLightBack);

// let directionalLightFront = new THREE.DirectionalLight(new THREE.Color('hsl(0, 0%, 100%)'), 0.25);
// directionalLightFront.position.set(-30, 100, -100);
// scene.add(directionalLightFront);




// var clock = new THREE.Clock();
// var angle = 0; // текущий угол
// var angularSpeed = THREE.Math.degToRad(20); // угловая скорость - градусов в секунду
// var delta = 0;
// var radius = 20;

// //функция, обновляющая сцену
// function animate() {
//     delta = clock.getDelta(); // getDelta() - возвращает интервал в долях секунды
//     requestAnimationFrame(animate);

//     camera.position.x = Math.cos(angle) * radius;
//     camera.position.z = Math.sin(angle) * radius;
//     angle += angularSpeed * delta; // приращение угла

//     camera.lookAt(0, 0, 0);

//     renderer.render(scene, camera);

//     cube2.rotation.x += 0.01;
// 	cube2.rotation.y += 0.01;

// 	cube3.rotation.y += 0.03;

    
// }
// animate();

/* global THREE, dat */

function main() {
  const canvas = document.getElementById('c')
  const renderer = new THREE.WebGLRenderer({canvas});

  const fov = 45;
  const aspect = 2;
  const near = 0.1;
  const far = 100;
  const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);
  camera.position.set(0, 10, 20);

  const controls = new OrbitControls(camera, canvas);
  controls.target.set(0, 5, 0);
  controls.update();

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xD2691E);

  {
    const planeSize = 40;

    const loader = new THREE.TextureLoader();
    const texture = loader.load('https://r105.threejsfundamentals.org/threejs/resources/images/checker.png');
    texture.wrapS = THREE.RepeatWrapping;
    texture.wrapT = THREE.RepeatWrapping;
    texture.magFilter = THREE.NearestFilter;
    const repeats = planeSize / 2;
    texture.repeat.set(repeats, repeats);

  //Сцена ----------------------------------------------------------------------------------------------------
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xD2691E);
  //----------------------------------------------------------------------------------------------------------


  //Элемент управления, позволяет камере вращаться вокруг цели.-----------------------------------------------
  const controls = new OrbitControls(camera, canvas);
  controls.target.set(0, 5, 0);
  controls.update();
  //----------------------------------------------------------------------------------------------------------

    const planeGeo = new THREE.PlaneBufferGeometry(planeSize, planeSize);
    const planeMat = new THREE.MeshPhongMaterial({
      map: texture,
      side: THREE.DoubleSide,
    });
    const mesh = new THREE.Mesh(planeGeo, planeMat);
    mesh.rotation.x = Math.PI * -.5;
    scene.add(mesh);
  }
  {
    const cubeSize = 4;
    const cubeGeo = new THREE.BoxBufferGeometry(cubeSize, cubeSize, cubeSize);

    var texture3 = new THREE.TextureLoader().load( './crate.gif' );
    var material3 = new THREE.MeshBasicMaterial( { map: texture3 } );
    const cubMesh = new THREE.Mesh(cubeGeo, material3);
    cubMesh.position.set(cubeSize + 1, cubeSize / 2, 0);
    scene.add(cubMesh);
  }
  {
    const sphereRadius = 3;
    const sphereWidthDivisions = 32;
    const sphereHeightDivisions = 16;
    const sphereGeo = new THREE.SphereBufferGeometry(sphereRadius, sphereWidthDivisions, sphereHeightDivisions);
    const sphereMat = new THREE.MeshPhongMaterial({color: '#CA8'});
    const mesh = new THREE.Mesh(sphereGeo, sphereMat);
    mesh.position.set(-sphereRadius - 1, sphereRadius + 2, 0);
    scene.add(mesh);
  }
  //Плоская поверхность---------------------------------------------------------------------------------------
  const planeSize = 40;
  const texture = new THREE.TextureLoader().load('./altstu_bg.webp');//шахматная доска 2x2
  texture.wrapS = THREE.RepeatWrapping;
  texture.wrapT = THREE.RepeatWrapping;
  texture.magFilter = THREE.NearestFilter;
  const repeats = planeSize / 10;
  texture.repeat.set(repeats, repeats);//зарептить картинку по 10 в длину и ширину

  const planeGeo = new THREE.PlaneBufferGeometry(planeSize, planeSize);
  const planeMat = new THREE.MeshPhongMaterial({
    map: texture,
    side: THREE.DoubleSide,
  });
  const mesh = new THREE.Mesh(planeGeo, planeMat);
  mesh.rotation.x = Math.PI * -.5; //поворот поверхности на 180 градусов
  scene.add(mesh);
  //----------------------------------------------------------------------------------------------------------


  {
    const color = 0xFFFFFF;
    const intensity = 1;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(0, 10, 0);
    light.target.position.set(-5, 0, 0);
    scene.add(light);
    scene.add(light.target);
  }

  //3D модель

  //3D модель-1-----------------------------------------------------------------------------------------------
  new GLTFLoader().load('./robot_model/adamHead.gltf', function(gltf) {
    console.log(gltf);
    const root = gltf.scene;
    root.position.set(10, 5, 10);//позиционирование
    root.scale.set(2.5, 2.5, 2.5);//масштабирование
    
    scene.add(root);
  }, function(xhr) {
    console.log(xhr.loaded/xhr.total * 100 + "% loaded");
  }, function(err) {
    console.log("An error occured: " + err)
  });
  //----------------------------------------------------------------------------------------------------------


  //3D модель-2-----------------------------------------------------------------------------------------------
  new GLTFLoader().load('./women_model/scene.gltf', function(gltf) {
    console.log(gltf);
    const root = gltf.scene;
    
    root.position.set(10, 5, 10);
    root.scale.set(2.5, 2.5, 2.5);
    
    scene.add(root);
  }, function(xhr) {
    console.log(xhr.loaded/xhr.total * 100 + "% loaded");
  }, function(err) {
    console.log("An error occured: " + err)
  });
  //----------------------------------------------------------------------------------------------------------

  function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
      renderer.setSize(width, height, false);
    }
    return needResize;
  }

  //Куб-------------------------------------------------------------------------------------------------------
  const geometry = new THREE.BoxGeometry( 4, 4, 4 );
	var texture3 = new THREE.TextureLoader().load( './crate.gif' );
  var material3 = new THREE.MeshBasicMaterial( { map: texture3 } );
	const cube = new THREE.Mesh( geometry, material3 );
  cube.position.set(-9, 2, -9)
	scene.add( cube );
  //----------------------------------------------------------------------------------------------------------



  function resizeRendererToDisplaySize(renderer) {
    const canvas = renderer.domElement;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;
    const needResize = canvas.width !== width || canvas.height !== height;
    if (needResize) {
      renderer.setSize(width, height, false);
    }
    return needResize;
  }

  let stateLeft = true;
  function render() {
    console.log(cube.position.x)
    cube.rotation.x += 0.01;
    if (cube.position.x < 3 && cube.position.x > 0) {
      stateLeft = true;
    }
    if (cube.position.x <= 0) {
      stateLeft = false;
    }
    
    if (stateLeft) {
      cube.position.x += 0.1;
    } else {
      cube.position.x -= 0.1;
    }

    if (resizeRendererToDisplaySize(renderer)) {
      const canvas = renderer.domElement;
      camera.aspect = canvas.clientWidth / canvas.clientHeight;
      camera.updateProjectionMatrix();
    }

    renderer.render(scene, camera);

    requestAnimationFrame(render);
  }

  requestAnimationFrame(render);
  animate();


}

main();


main();
