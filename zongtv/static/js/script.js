
function moveNewsRight() {

    const row = document.getElementById("channelRow");
    const card = row.querySelector(".channel-card");

    if(!card) return;

    const cardWidth = card.offsetWidth + 35;

    row.scrollBy({
        left: cardWidth,
        behavior: "smooth"
    });
}

function moveNewsLeft() {

    const row = document.getElementById("channelRow");
    const card = row.querySelector(".channel-card");

    if(!card) return;

    const cardWidth = card.offsetWidth + 35;

    row.scrollBy({
        left: -cardWidth,
        behavior: "smooth"
    });
}
function moveZongRight() {

    const row = document.getElementById("zongRow");
    const card = row.querySelector(".show-card");

    if(!card) return;

    const width = card.offsetWidth + 20;

    row.scrollBy({
        left: width,
        behavior: "smooth"
    });
}

function moveZongLeft() {

    const row = document.getElementById("zongRow");
    const card = row.querySelector(".show-card");

    if(!card) return;

    const width = card.offsetWidth + 20;

    row.scrollBy({
        left: -width,
        behavior: "smooth"
    });
}

function entLeft() {

    const row = document.getElementById("entRow");
    const card = row.querySelector(".channel-card");

    const move = card.offsetWidth + 35;

    row.scrollBy({
        left: -move,
        behavior: "smooth"
    });
}
function moveRight(categoryId){

    const row =
    document.getElementById(
        "showRow" + categoryId
    );

    const card =
    row.querySelector(".show-card");

    if(!card) return;

    const width =
    card.offsetWidth + 20;

    row.scrollBy({
        left: width,
        behavior: "smooth"
    });
}

function moveLeft(categoryId){

    const row =
    document.getElementById(
        "showRow" + categoryId
    );

    const card =
    row.querySelector(".show-card");

    if(!card) return;

    const width =
    card.offsetWidth + 20;

    row.scrollBy({
        left: -width,
        behavior: "smooth"
    });
}

function moveRightEntertainment() {

    const row = document.getElementById("entRow");
    const card = row.querySelector(".channel-card");

    if (!card) return;

    const cardWidth = card.offsetWidth + 35;

    row.scrollBy({
        left: cardWidth,
        behavior: "smooth"
    });
}

function moveLeftEntertainment() {

    const row = document.getElementById("entRow");
    const card = row.querySelector(".channel-card");

    if (!card) return;

    const cardWidth = card.offsetWidth + 35;

    row.scrollBy({
        left: -cardWidth,
        behavior: "smooth"
    });
}
window.addEventListener("load", function () {

    document.body.classList.add("loaded");

    const loader = document.getElementById("loader");

    setTimeout(() => {
        if(loader){
            loader.remove();
        }
    }, 200);

});