
/* ==========================================
   SIGNURE — JAVASCRIPT PRINCIPAL
   Navigation responsive
========================================== */

document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.querySelector(".menu");
    const nav = document.querySelector("#main-navigation");

    // Vérifier que le menu existe
    if (!toggle || !nav) {
        return;
    }

    // Ouvrir et fermer le menu mobile
    toggle.addEventListener("click", function () {

        const isOpen = nav.classList.toggle("open");

        toggle.setAttribute(
            "aria-expanded",
            String(isOpen)
        );

        toggle.setAttribute(
            "aria-label",
            isOpen ? "Fermer le menu" : "Ouvrir le menu"
        );

    });

    // Fermer le menu après un clic sur un lien
    nav.querySelectorAll("a").forEach(function (link) {

        link.addEventListener("click", function () {

            nav.classList.remove("open");

            toggle.setAttribute("aria-expanded", "false");
            toggle.setAttribute("aria-label", "Ouvrir le menu");

        });

    });

    // Fermer le menu avec la touche Échap
    document.addEventListener("keydown", function (event) {

        if (event.key === "Escape") {

            nav.classList.remove("open");

            toggle.setAttribute("aria-expanded", "false");
            toggle.setAttribute("aria-label", "Ouvrir le menu");

        }

    });

});


/* =====================================
   BOUTON RETOUR EN HAUT — SIGNURE
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    const backToTop = document.getElementById("backToTop");

    if (!backToTop) return;

    function toggleBackToTop() {
        if (window.scrollY > 300) {
            backToTop.classList.add("show");
        } else {
            backToTop.classList.remove("show");
        }
    }

    window.addEventListener("scroll", toggleBackToTop, {
        passive: true
    });

    toggleBackToTop();

    backToTop.addEventListener("click", function () {
        const reduceMotion = window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches;

        window.scrollTo({
            top: 0,
            behavior: reduceMotion ? "instant" : "smooth"
        });
    });

});


/* =====================================
   MASQUER LE BOUTON CONTACT AU FOOTER
===================================== */

document.addEventListener("DOMContentLoaded", function () {

    const contactButton = document.querySelector(".floating-contact");
    const footer = document.querySelector(".site-footer");

    if (!contactButton || !footer) return;

    const observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {

                if (entry.isIntersecting) {
                    contactButton.classList.add("contact-hidden");
                } else {
                    contactButton.classList.remove("contact-hidden");
                }

            });
        },
        {
            threshold: 0
        }
    );

    observer.observe(footer);

});
