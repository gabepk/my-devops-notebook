import debounce from './debounce.js';

export default class ScrollAnima {
    constructor(query) {
        this.sections = document.querySelectorAll(query);
        this.windowMetade = window.innerHeight * 0.8;
    }

    bindEventCallbacks() {
        this.checkDistance = debounce(this.checkDistance.bind(this), 50);
    }
    addEvents() {
        window.addEventListener('scroll', this.checkDistance);
    }

    getDistance() {
        this.distance = [...this.sections].map(section => {
            const offset = section.offsetTop;
            return {
                element: section,
                offset: Math.floor(offset - this.windowMetade),
            };
        });
    }

    checkDistance() {
        this.distance.forEach(item => {
            if (window.pageYOffset > item.offset) {
                item.element.classList.add('active');
            }
        })
    }

    init() {
        if (this.sections.length) {
            this.getDistance();
            this.checkDistance();

            this.bindEventCallbacks();
            this.addEvents();
        }
        return this;
    }
}