import Post from './post.js';
import Block from './block.js';

export default class AdminActions {
  constructor(query) {
    // Initialize list of posts
    this.posts = document.querySelector("#posts").children;
    this.posts = Array.from(this.posts).map(post => {
      this.slug = post.querySelector("#slug").textContent;
      this.color = post.querySelector("#color").textContent;
      return new Post(this.slug, this.color);
    });


    // Get all blocks from the roadmap
    this.blocks = document.querySelectorAll(query);
    this.blocks = Array.from(this.blocks).map(block => {
        this.slug = block.id;
        this.postLink = block.querySelector("a");
        this.addButton = block.querySelector("div");
        return new Block(this.slug, this.postLink, this.addButton);
    });
  }

  createLinksFromRoadmapItemToPost() {
    Array.from(this.blocks).map(block => {
      if(this.posts.map(post => post.slug).includes(block.slug)) {
        block.postLink.href = "/post/" + block.slug;
        block.addButton.parentElement.classList.add("linked");
        block.addButton.parentElement.style.backgroundColor = 
          this.posts.filter(post => post.slug == block.slug)[0].color;
      } else {
        block.addButton.onclick = () => 
          window.location.href = "/admin/blog/post/add?author=1&slug=" + block.slug;
          block.addButton.parentElement.style.backgroundColor = "#ea9999";
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