import Post from './post.js';
import Block from './block.js';

export default class Actions {
  constructor(query) {
    // Initialize list of posts
    this.posts = document.querySelector('#posts').children;
    this.posts = Array.from(this.posts).map((post) => {
      this.slug = post.querySelector('#slug').textContent;
      this.name = post.querySelector('#name').textContent;
      return new Post(this.slug, this.name);
    });

    // Get all blocks from the roadmap
    this.blocks = document.querySelectorAll(query);
    this.blocks = Array.from(this.blocks).map((block) => {
      this.slug = block.id;
      this.postLink = block.querySelector('a');
      return new Block(this.slug, this.postLink);
    });
  }

  createLinksFromRoadmapItemToPost() {
    Array.from(this.blocks).map((block) => {
      if (this.posts.map((post) => post.slug).includes(block.slug)) {
        block.postLink.href = '/post/' + block.slug;
        block.postLink.parentElement.classList.add('linked');
        block.postLink.parentElement.classList.add(
          this.posts.filter((post) => post.slug == block.slug)[0].name,
        );
      }
    });
  }

  init() {
    if (this.blocks && this.blocks.length) {
      this.createLinksFromRoadmapItemToPost();
    }
    return this;
  }
}
