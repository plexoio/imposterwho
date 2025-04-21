function sendMail(){
    let parms = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        subject: document.getElementById("subject").value,
        message: document.getElementById("message").value,
    }

    emailjs.send("service_4n1zxbt", template_1gspcga, parms).then(alert("Email sent successfully!"))
}

document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();
  sendMail();
});