function convertToCups(amount, measurement) {
    switch(measurement) {
        case "ml":
            return amount / 236.59;
        case "tsp":
            return amount / 48;
        case "tbsp":
            return amount / 16;
        case "floz":
            return amount / 8;
        case "pints":
            return amount * 2;
        case "quarts":
            return amount * 4;
        case "gallons":
            return amount * 16;
    }
}

function convertFromCups(amount, measurement) {
    switch(measurement) {
        case "ml":
            return amount * 236.59;
        case "tsp":
            return amount * 48;
        case "tbsp":
            return amount * 16;
        case "floz":
            return amount * 8;
        case "pints":
            return amount / 2;
        case "quarts":
            return amount / 4;
        case "gallons":
            return amount / 16;
    }
}

function updateInputs(amount, measurement) {
    const amountInCups = (measurement == "cups" ? amount : convertToCups(amount, measurement));

    if (measurement != "floz") {
        const flOzInput = document.getElementById("fluidoz");
        flOzInput.value = Math.round(100 * convertFromCups(amountInCups, "floz")) / 100;
    }
    if (measurement != "cups") {
        const cupsInput = document.getElementById("cups");
        cupsInput.value = Math.round(100 * amountInCups) / 100;
    }
    if (measurement != "cups") {
        const pintsInput = document.getElementById("pints");
        pintsInput.value = Math.round(100 * convertFromCups(amountInCups, "pints")) / 100;
    }
    if (measurement != "quarts") {
        const quartsInput = document.getElementById("quarts");
        quartsInput.value = Math.round(100 * convertFromCups(amountInCups, "quarts")) / 100;
    }
    if (measurement != "gallons") {
        const gallonsInput = document.getElementById("gallons");
        gallonsInput.value = Math.round(100 * convertFromCups(amountInCups, "gallons")) / 100;
    }
    if (measurement != "tbsp") {
        const tbspInput = document.getElementById("tablespoons");
        tbspInput.value = Math.round(100 * convertFromCups(amountInCups, "tbsp")) / 100;
    }
    if (measurement != "tsp") {
        const tspInput = document.getElementById("teaspoons");
        tspInput.value = Math.round(100 * convertFromCups(amountInCups, "tsp")) / 100;
    }
    if (measurement != "ml") {
        const mlInput = document.getElementById("milliliters");
        mlInput.value = Math.round(100 * convertFromCups(amountInCups, "ml")) / 100;
    }
}

function updateFromTbsp() {
    const tbspInput = document.getElementById("tablespoons");
    updateInputs(tbspInput.value, "tbsp");
}

function updateFromFlOz() {
    const flOzInput = document.getElementById("fluidoz");
    updateInputs(flOzInput.value, "floz");
}

function updateFromTsp() {
    const tspInput = document.getElementById("teaspoons");
    updateInputs(tspInput.value, "tsp");
}

function updateFromMl() {
    const mlInput = document.getElementById("milliliters");
    updateInputs(mlInput.value, "ml");
}

function updateFromCups() {
    const cupsInput = document.getElementById("cups");
    updateInputs(cupsInput.value, "cups");
}

function updateFromPints() {
    const pintsInput = document.getElementById("pints");
    updateInputs(pintsInput.value, "pints");
}

function updateFromQuarts() {
    const quartsInput = document.getElementById("quarts");
    updateInputs(quartsInput.value, "quarts");
}

function updateFromGallons() {
    const gallonsInput = document.getElementById("gallons");
    updateInputs(gallonsInput.value, "gallons");
}

function updateFromF() {
    const fInput = document.getElementById("fahrenheit");
    const cInput = document.getElementById("celsius");

    cInput.value = Math.round(100 * (fInput.value - 32) / 1.8) / 100
}

function updateFromC() {
    const fInput = document.getElementById("fahrenheit");
    const cInput = document.getElementById("celsius");

    fInput.value = Math.round(100 * (cInput.value * 1.8) + 32) / 100
}