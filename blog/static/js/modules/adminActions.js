import Post from './post.js';
import Block from './block.js';

export default class AdminActions {
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
      this.addButton = block.querySelector('div');
      return new Block(this.slug, this.postLink, this.addButton, '0');
    });
  }

  createLinksFromRoadmapItemToPost() {
    Array.from(this.blocks).map((block) => {
      if (this.posts.map((post) => post.slug).includes(block.slug)) {
        block.postLink.href = '/post/' + block.slug;
        block.postLink.parentElement.classList.value = 'side block linked';
        console.log(this.posts);
        block.postLink.parentElement.classList.add(
          this.posts.filter((post) => post.slug == block.slug)[0].name,
        );
      } else {
        block.addButton.onclick = () =>
          (window.location.href =
            '/admin/blog/post/add?author=1&slug=' + block.slug);
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
