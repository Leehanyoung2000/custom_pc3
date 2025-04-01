function updateTotalPrice() {
    let monitorPrice = parseFloat(document.getElementById("monitor-select").value) || 0;
    let mousePrice = parseFloat(document.getElementById("mouse-select").value) || 0;
    let keyboardPrice = parseFloat(document.getElementById("keyboard-select").value) || 0;
    let totalPrice = monitorPrice + mousePrice + keyboardPrice;

    document.getElementById("total-price").innerText = `총 가격: ${totalPrice.toLocaleString()} 원`;
}

function updatePart(type) {
    let selectElement = document.getElementById(`${type}-select`);
    let selectedOption = selectElement.options[selectElement.selectedIndex];
    let image = selectedOption.getAttribute("data-image");

    let partImage = document.getElementById(`${type}-image`);
    partImage.src = image;
    partImage.style.width = "30%";
    partImage.style.maxWidth = "300px";

    updateTotalPrice();
}