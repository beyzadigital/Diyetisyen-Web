console.log("BB Nutrition hazır!");

const whatsapp = document.querySelector(".whatsapp");

whatsapp.addEventListener("click", () => {

    console.log("WhatsApp butonuna tıklandı.");

});

AOS.init({
    duration:1000,
    once:true
});
