class Point {
    constructor(x, y, z) {
        this.x = x
        this.y = y
        this.z = z
    }
}

class Line {
    constructor(startPoint, endPoint) {
        this.startPoint = startPoint
        this.endPoint = endPoint
    }
}

let coordsArray = []

//читаем файл из инпута, возвращает содержимое файла (json)
const readFile = (input) => {
    console.log('readFile func')
    let file = input.files[0];
    
    let reader = new FileReader();
      
    reader.readAsText(file);
      
    reader.onload = function() {
        console.log("Файл загружен");
        console.log(reader.result)
        return reader.result
    };
      
    reader.onerror = function() {
        console.log(reader.error);
    };
    
}

const fileInput = document.getElementById("file-input")

const loadFigure = (input) => {
    console.log("load")
    const jsonFigure = readFile(input)
    alert('jsonFigure')
    console.log(jsonFigure)
    alert('reading')
    const parseObj = JSON.parse(jsonFigure)
    console.log("obj")
    console.log(parseObj)
}

loadFigure(fileInput)