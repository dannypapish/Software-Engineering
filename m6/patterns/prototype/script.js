// Prototypical inheritance allows us to inherit properties from other objects, even if they are not related to each other.
// This is a very powerful, yet often unappreciated and misunderstood feature of JavaScript.
// The prototype property is a property of all objects in JavaScript, and we can use it to establish a unique inheritance chain for each object.
// Here's the main thing to remember:
//    - When a new method is added to the prototype of an object, all instances of that object will have access to that method.

function AnyNumber(real, imaginary) {
    this.real = real;
    this.imaginary = imaginary;
}

AnyNumber.prototype.getNumber = function () {
    return this.real;
}

AnyNumber.prototype.setNumber = function (num) {
    this.real = num;
}

// TODO 11: Add getImaginary(), setImaginary(num), add(c), and magnitude() methods

AnyNumber.prototype.getImaginary = function () {
    return this.imaginary;
}

AnyNumber.prototype.setImaginary = function (num) {
    this.imaginary = num;
}

AnyNumber.prototype.add = function (c) {
    var real = this.real + c.real;
    var imaginary = this.imaginary + c.imaginary;
    return new AnyNumber(real, imaginary);
}

AnyNumber.prototype.magnitude = function () {
    return Math.sqrt(this.real * this.real + this.imaginary * this.imaginary);
}

// Helper functions for drawing the fractal
function makeRandomPalette() {
    var palette = [];
    for (var i = 0; i < 6; i++) {
        // generates a random hex color
        palette.push("#" + ((1 << 24) * Math.random() | 0).toString(16));
    }
    return palette;
}

// Setting some global variables for the fractal drawing

var width = 600,
    height = 600,
    paletteOptions = [
        ["#C9DDDE", "#DDDDDD", "#CCCCCC", "#BBBBBB", "#AAAAAA", "#999999"],
        ["#352A87", "#B2BEB5", "#F2F3F4", "#E9E2AF", "#A67D3D", "#5C3317"],
        ["#000000", "#111111", "#222222", "#333333", "#444444", "#555555"],
        ["#123456", "#234567", "#345678", "#456789", "#56789A", "#6789AB"],
        ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082"],
        ["#352221", "#229872", "#234273", "#200164", "#352095", "#847706"]
    ],
    paletteChoiceIndex = 0,
    palette = paletteOptions[paletteChoiceIndex],
    maxIterations = 100,
    break_point = 2,
    c = new AnyNumber(-0.4, 0.6),
    xMin = -2,
    xMax = 2,
    yMin = -2,
    yMax = 2;


function map(value, start1, stop1, start2, stop2) {
    return (start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1)));
}

function setPixel(imageData, x, y, r, g, b, a) {
    var index = (x + y * width) * 4;
    imageData.data[index] = r;
    imageData.data[index + 1] = g;
    imageData.data[index + 2] = b;
    imageData.data[index + 3] = a;
    return imageData;
}

function draw_julia() {
    var x, y, a, b, i, z, zx, zy;
    imageData = new ImageData(width, height);
    for (x = 0; x < width; x++) {
        for (y = 0; y < height; y++) {
            a = map(x, 0, width, xMin, xMax);
            b = map(y, 0, height, yMin, yMax);
            z = new AnyNumber(a, b);
            i = 0;
            while (i < maxIterations) {
                zx = z.getNumber() * z.getNumber() - z.getImaginary() * z.getImaginary();
                zy = 2 * z.getNumber() * z.getImaginary();
                z = new AnyNumber(zx, zy);
                z = z.add(c);
                if (z.magnitude() > break_point) {
                    break;
                }
                i++;
            }
            if (i == maxIterations) {
                setPixel(imageData, x, y, 0, 0, 0, 255);
            } else {
                var color = palette[i % 6],
                    r = parseInt(color.substring(1, 3), 16),
                    g = parseInt(color.substring(3, 5), 16),
                    b = parseInt(color.substring(5, 7), 16);
                imageData = setPixel(imageData, x, y, r, g, b, 255);
            }
        }
    }
    return imageData;
}

function reload(paletteChoiceIndex) {
    palette = paletteOptions[paletteChoiceIndex];
    var canvas = document.getElementById("canvas");
    var ctx = canvas.getContext("2d");
    canvas.width = width;
    canvas.height = height;
    var imageData = draw_julia();
    ctx.putImageData(imageData, 0, 0);
}

function changePalette() {
    paletteChoiceIndex = (paletteChoiceIndex + 1) % paletteOptions.length;
    reload(paletteChoiceIndex);
}

function reset() {
    xMin = -2;
    xMax = 2;
    yMin = -2;
    yMax = 2;
    break_point = 2;
    maxIterations = 100;
    c = new AnyNumber(-0.4, 0.6);
    reload(paletteChoiceIndex);
}

function reloadColorPalette() {
    paletteChoiceIndex = 0;
    paletteOptions = [
        ["#C9DDDE", "#DDDDDD", "#CCCCCC", "#BBBBBB", "#AAAAAA", "#999999"],
        ["#352A87", "#B2BEB5", "#F2F3F4", "#E9E2AF", "#A67D3D", "#5C3317"],
        ["#000000", "#111111", "#222222", "#333333", "#444444", "#555555"],
        ["#123456", "#234567", "#345678", "#456789", "#56789A", "#6789AB"],
        ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082"],
        ["#352221", "#229872", "#234273", "#200164", "#352095", "#847706"]
    ];
    reload(paletteChoiceIndex);
}

// TODO 12: Add the followingfunctions to your code.
// - increaseC()
// - decreaseC()
// - increaseCI()
// - decreaseCI()
// - changeC()
// - randomizeColorPalette()
// - increaseMaxIterations()
// - decreaseMaxIterations()
// - zoomIn()
// - zoomOut()
// - increaseBreakPoint()
// - decreaseBreakPoint()

function increaseC() {
    c.real += 0.1;
    reload(paletteChoiceIndex);
}

function decreaseC() {
    c.real -= 0.1;
    reload(paletteChoiceIndex);
}

function increaseCI() {
    c.imaginary += 0.1;
    reload(paletteChoiceIndex);
}

function decreaseCI() {
    c.imaginary -= 0.1;
    reload(paletteChoiceIndex);
}

function changeC() {
    var real = Math.random() * 4 - 2;
    var imaginary = Math.random() * 4 - 2;
    c = new AnyNumber(real, imaginary);
    reload(paletteChoiceIndex);
}

function randomizeColorPalette() {
    paletteOptions = [makeRandomPalette()];
    reloadColorPalette();
    reload(paletteChoiceIndex);
}

function increaseMaxIterations() {
    if (maxIterations < 25600) {
        maxIterations *= 2;
        reload(paletteChoiceIndex);
    }
}

function decreaseMaxIterations() {
    if (maxIterations > 25) {
        maxIterations /= 2;
        reload(paletteChoiceIndex);
    }
}

function zoomIn() {
    xMin -= 0.5;
    yMin -= 0.5;
    xMax += 0.5;
    yMax += 0.5;
    reload(paletteChoiceIndex);
}

function zoomOut() {
    xMin += 0.5;
    yMin += 0.5;
    xMax -= 0.5;
    yMax -= 0.5;
    reload(paletteChoiceIndex);
}

function increaseBreakPoint() {
    break_point *= 2;
    reload(paletteChoiceIndex);
}

function decreaseBreakPoint() {
    break_point /= 2;
    reload(paletteChoiceIndex);
}

function eventHandler(event) {
    var key = event.keyCode;
    switch (key) {
        case 82: // r
            reset();
            break;
        case 80: // p
            changePalette();
            break;
        case 67: // c
            changeC();
            break;
        case 73: // i
            increaseMaxIterations();
            break;
        case 68: // d
            decreaseMaxIterations();
            break;
        case 90: // z
            zoomIn();
            break;
        case 88: // x
            zoomOut();
            break;
        case 66: // b
            increaseBreakPoint();
            break;
        case 86: // v
            decreaseBreakPoint();
            break;
        case 71: // g
            randomizeColorPalette();
            break;
        case 85: // u
            increaseC();
            break;
        case 74: // j
            decreaseC();
            break;
        case 72: // h
            increaseCI();
            break;
        case 78: // n
            decreaseCI();
            break;
    }
}

window.onload = function () {
    reload(paletteChoiceIndex);
    document.addEventListener("keydown", eventHandler, false); // Observer for key presses
}

