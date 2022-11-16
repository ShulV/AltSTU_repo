const DEFAULT_IMG_URL = "https://thumbs.dreamstime.com/b/%D1%81%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BD%D0%BE%D0%B5-%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D1%83%D0%B4%D0%B8%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%BB%D1%8E%D0%B4%D0%B5%D0%B9-%D0%B2%D1%8B%D0%B4%D0%B5%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D1%85-%D0%BD%D0%B0-%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%86%D0%B2%D0%B5%D1%82%D0%BD%D0%BE%D0%BC-223594982.jpg"
const DEFAULT_HIST_MAX = 3000;
const BUTTON_DISTANCE = 30;

const canvas = document.getElementById("canvas");
const context = canvas.getContext('2d');

function drawBrightnessHistogram(chart, maxValue = DEFAULT_HIST_MAX) {
    // Get image data from canvas
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    // Compute brightness
    var dict = Array(256).fill(0);

    for (let i = 0; i < data.length; i += 4) {
        var brightness = Math.round(
            0.299 * data[i] + 0.5876 * data[i + 1] + 0.114 * data[i + 2]
        );
        
        dict[brightness] += 1;
    }

    // Set max y value
    for (let i = 0; i < dict.length; i += 1) {
        if(dict[i] > maxValue) {
            dict[i] = maxValue;
        }
    }

    // Updating chart
    chart.config.data.datasets[0].data = dict;
    chart.update();
}

function invert() {
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    for (var i = 0; i < data.length; i += 4) {
        data[i] = 255 - data[i];         // red
        data[i + 1] = 255 - data[i + 1]; // green
        data[i + 2] = 255 - data[i + 2]; // blue
    }

    context.putImageData(imageData, 0, 0);
};

function grayscale() {
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    for (var i = 0; i < data.length; i += 4) {
        var avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
        data[i] = avg;      // red
        data[i + 1] = avg;  // green
        data[i + 2] = avg;  // blue
    }

    context.putImageData(imageData, 0, 0);
};

function brightnessAdjustment(coefficent) {
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    for (var i = 0; i < data.length; i += 4) {
        data[i] += coefficent;        // red
        data[i + 1] += coefficent;    // green
        data[i + 2] += coefficent;     // blue

        if (data[i] > 255)
            data[i] = 255;
        else if (data[i] < 0)
            data[i] = 0;
        
        if (data[i + 1] > 255)
            data[i + 1] = 255;
        else if (data[i + 1] < 0)
            data[i + 1] = 0;
        
        if (data[i + 2] > 255)
            data[i + 2] = 255;
        else if (data[i + 2] < 0)
            data[i + 2] = 0;
    }

    context.putImageData(imageData, 0, 0);
}

function contrastAdjustment(coefficent) {
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    
    let averageGray = 0;

    for (var i = 0; i < data.length; i += 4) {
        averageGray += (
            data[i] * 0.2126 + data[i + 1] * 0.7152 + data[i + 2] * 0.0722
        );
    }

    averageGray /= data.length / 4;
    
    for (var i = 0; i < data.length; i += 4) {
        data[i] += Math.round(
            (coefficent * (data[i] - averageGray) + averageGray) / 255
        );    
        data[i + 1] += Math.round(
            (coefficent * (data[i + 1] - averageGray) + averageGray) / 255
        );   
        data[i + 2] += Math.round(
            (coefficent * (data[i + 2] - averageGray) + averageGray) / 255
        ); 

        if (data[i] > 255)
            data[i] = 255;
        else if (data[i] < 0)
            data[i] = 0;
        
        if (data[i + 1] > 255)
            data[i + 1] = 255;
        else if (data[i + 1] < 0)
            data[i + 1] = 0;
        
        if (data[i + 2] > 255)
            data[i + 2] = 255;
        else if (data[i + 2] < 0)
            data[i + 2] = 0;
    }

    context.putImageData(imageData, 0, 0);
}

function binarization(threshold) {
    const imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;

    for (var i = 0; i < data.length; i += 4) {
        let total = data[i] + data[i + 1] + data[i + 2];

        if (total > threshold) {
            data[i] = 255;
            data[i + 1] = 255;
            data[i + 2] = 255;
        }
        else {
            data[i] = 0;
            data[i + 1] = 0;
            data[i + 2] = 0;
        }
    }

    context.putImageData(imageData, 0, 0);
}

function main() {
    // Draw histogram
    var ctx = document.getElementById('chart');
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Array.from(Array(256).keys()),
            datasets: [{
                barPercentage: 0.5,
                barThickness: 6,
                maxBarThickness: 8,
                minBarLength: 2,
                data: Array(256).fill(0),
                backgroundColor: "orange", //rgba(0, 200, 0, 1)",
            }],
        },
        options: {
            responsive: true,
            title: {
                display: true,
                fontSize: 16,
                text: "Гистограмма яркости"
            },
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
        }
    });

    // Adding listener to load button
    const loadButton = document.getElementById("loadButton");
    
    loadButton.addEventListener("click", () => {
        // Loading image when button is clicked
        
        var url = urlInput.value;
        
        let image = document.createElement("img");
        
        image.onload = function() {
            canvas.setAttribute("width", canvas.offsetWidth);
            canvas.setAttribute("height", canvas.offsetHeight);

            context.drawImage(image, 0, 0, image.width, image.height,
                 0, 0, canvas.offsetWidth, canvas.offsetHeight);

            drawBrightnessHistogram(chart);
        }

        image.setAttribute("src", url);
        image.setAttribute("crossOrigin", "");
    })

    // Adding listener to update brightness histogram button
    const histInput = document.getElementById("histInput");
    histInput.setAttribute("value", DEFAULT_HIST_MAX);

    const histButton = document.getElementById("histButton");
    histButton.addEventListener("click", () => {
        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    // Specifying url input
    const urlInput = document.getElementById("urlInput");
    urlInput.setAttribute("value", DEFAULT_IMG_URL);

    //ОБРАБОТЧИКИ СОБЫТИЙ

    // Adding listener to grayscaleButton
    const grayscaleButton = document.getElementById("grayscaleButton");
    grayscaleButton.addEventListener("click", () => {
        grayscale();

        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    // Adding listener to invertButton
    const invertButton = document.getElementById("invertButton");
    invertButton.addEventListener("click", () => {
        invert();
        
        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    // Adding listener to brightnessButton
    const brightnessInput = document.getElementById("brightnessInput");
    const brightnessButton = document.getElementById("brightnessButton");
    
    brightnessButton.addEventListener("click", () => {
        let coefficent =  parseInt(brightnessInput.value);
        brightnessAdjustment(coefficent);
        
        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    // Adding listener to contrastButton
    const contrastInput = document.getElementById("contrastInput");
    const contrastButton = document.getElementById("contrastButton");
    
    contrastButton.addEventListener("click", () => {
        let coefficent =  parseFloat(eval(contrastInput.value));
        contrastAdjustment(coefficent);
        
        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    // Adding listener to binarization
    const binarizationInput = document.getElementById("binarizationInput");
    const binarizationButton = document.getElementById("binarizationButton");
    
    binarizationButton.addEventListener("click", () => {
        let coefficent =  parseInt(binarizationInput.value);
        binarization(coefficent);
        
        let maxValue = parseInt(histInput.value);
        drawBrightnessHistogram(chart, maxValue);
    });

    loadButton.click();
}

main()