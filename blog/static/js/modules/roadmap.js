export default class Roadmap {
    constructor(query) {
        this.sections = document.querySelectorAll(query);
    }

    bindEventCallbacks() {
        this.showSections = this.showSections.bind(this);
    }
    addEvents() {
        window.addEventListener('scroll', this.showSections);
    }

    showSections() {
        this.sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const isSectionVisible = (sectionTop - (window.innerHeight * 0.8)) < 0;
            if (isSectionVisible) {
                section.classList.add('active');
            }
        });
    }

    init() {
        if (this.sections.length) {
            this.bindEventCallbacks();
            this.addEvents();
            this.showSections();
        }
    }
}