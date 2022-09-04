const canvas = document.getElementById("canvas-plot")
canvas.width = 1200;
canvas.height = 600;
const ctx = canvas.getContext("2d")

ctx.fillStyle = "#003300";
ctx.font = '20px sans-serif';

function drawLine(ctx, startX, startY, endX, endY){
    ctx.beginPath();
    ctx.moveTo(startX,startY);
    ctx.lineTo(endX,endY);
    ctx.stroke();
}

drawLine(ctx, 50, 50, 100, 100)