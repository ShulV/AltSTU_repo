// //128 версия выдает ошибки
import * as THREE from 'https://unpkg.com/three@0.127.0/build/three.module.js'
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


  //Сцена ----------------------------------------------------------------------------------------------------
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xD2691E);
  //----------------------------------------------------------------------------------------------------------


  //Элемент управления, позволяет камере вращаться вокруг цели.-----------------------------------------------
  const controls = new OrbitControls(camera, canvas);
  controls.target.set(0, 5, 0);
  controls.update();
  //----------------------------------------------------------------------------------------------------------


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


  //Свет -----------------------------------------------------------------------------------------------------
  const color = 0xFFFFFF;
  const intensity = 0.95;
  const light2 = new THREE.AmbientLight(color, intensity);
  light2.position.set(10, 10, 10)
  scene.add(light2);
  //----------------------------------------------------------------------------------------------------------
  

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
    root.position.set(-2, -2.6, 0);//позиционирование
    root.scale.set(5, 5, 5);//масштабирование
    
    scene.add(root);
  }, function(xhr) {
    console.log(xhr.loaded/xhr.total * 100 + "% loaded");
  }, function(err) {
    console.log("An error occured: " + err)
  });
  //----------------------------------------------------------------------------------------------------------


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
