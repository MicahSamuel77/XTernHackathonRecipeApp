function convertFromTbsp() {
    const tbspInput = document.getElementById("tablespoons");
    const tspInput = document.getElementById("teaspoons");
    const mlInput = document.getElementById("milliliters");

    if (isNaN(tbspInput.value)) {
        tbspInput.value = "";
    } else {
        tspInput.value = tbspInput.value*3;
        mlInput.value = Math.round(10 * tbspInput.value * 14.787) / 10
    }
}

function convertFromTsp() {
    const tbspInput = document.getElementById("tablespoons");
    const tspInput = document.getElementById("teaspoons");
    const mlInput = document.getElementById("milliliters");

    if (isNaN(tspInput.value)) {
        tspInput.value = "";
    } else {
        tbspInput.value = Math.round(10 * tspInput.value / 3) / 10;
        mlInput.value = Math.round(10 * tspInput.value * 4.929) / 10
    }
}

function convertFromMl() {
    const tbspInput = document.getElementById("tablespoons");
    const tspInput = document.getElementById("teaspoons");
    const mlInput = document.getElementById("milliliters");

    if (isNaN(mlInput.value)) {
        mlInput.value = "";
    } else {
        tspInput.value = Math.round(10 * mlInput.value / .203) / 10;
        tbspInput.value = Math.round(10 * mlInput.value / .068) / 10
    }
}