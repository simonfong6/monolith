import React, { useState, useEffect } from 'react';
import { useSearchParams } from "react-router-dom";

const timeAgo = (date) => {
  const seconds = Math.floor((new Date() - new Date(date)) / 1000);

  let interval = Math.floor(seconds / 31536000);
  if (interval > 1) {
    return interval + ' years ago';
  }

  interval = Math.floor(seconds / 2592000);
  if (interval > 1) {
    return interval + ' months ago';
  }

  interval = Math.floor(seconds / 86400);
  if (interval > 1) {
    return interval + ' days ago';
  }

  interval = Math.floor(seconds / 3600);
  if (interval > 1) {
    return interval + ' hours ago';
  }

  interval = Math.floor(seconds / 60);
  if (interval > 1) {
    return interval + ' minutes ago';
  }

  if (seconds < 10) return 'just now';

  return Math.floor(seconds) + ' seconds ago';
};

function Post({ post }) {
  return (
    <div>
      <div className="card" style={{ width: "18rem" }}>
        <div className="card-body">
          <h6 className="card-subtitle mb-2 text-body-secondary">
            {post.author}
            &nbsp;|&nbsp;
            <small className=" text-body-secondary float-right">
              {timeAgo(post.date)}
            </small>
          </h6>
          <p className="card-text">{post.text}</p>
          {
            post.tags.map((t) => <span key={t} className="badge rounded-pill text-bg-light">{t}</span>)
          }
        </div>
      </div>
    </div>
  );
}

function Row({ post }) {
  return (
    <tr>
      <th scope="row">{post[0]}</th>
      <td>{post[1]}</td>
      <td>{post[2]}</td>
      <td>{post[3].join(',')}</td>
      <td>{post[4]}</td>
    </tr>
  );
}

function Posts() {

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('/api/posts/').then(res => res.json()).then(data => {
      setPosts(data);
    });
  }, []);

  useEffect(() => {
    searchAuthor();
  }, []);

  const [authorResult, setAuthorResult] = useState(null);

  const [searchParams, setSearchParams] = useSearchParams();

  const author = searchParams.get('author');

  function searchAuthor() {
    fetch('/api/posts/author?' + new URLSearchParams({
      author: author,
    })).then(res => res.json()).then(data => {
      console.log(data);
      setAuthorResult(data);
    });
  }

  function searchOnClick(e) {
    e.preventDefault();
  }


  return (

    <div className='container'>
      <h1>this is the posts</h1>

      <form>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">Author</label>
          <input
            value={author} onChange={e => { setSearchParams({ 'author': e.target.value }); searchAuthor() }}
            type="author" className="form-control" id="exampleInputEmail1"
            aria-describedby="emailHelp" />
          <div id="emailHelp" className="form-text">The author whose posts to search for.</div>
        </div>
        <button onClick={e => { searchOnClick(e); searchAuthor() }} className="btn btn-primary">Search</button>
      </form>

      <div className='container'>
        <h3>Author Results</h3>
        {authorResult === null ? <div> No Result</div> : <Post post={authorResult} />}
      </div>

      <div className='container'>
        <h3>All Posts</h3>
        <table className="table">
          <thead>
            <tr>
              <th scope="col">id</th>
              <th scope="col">author</th>
              <th scope="col">text</th>
              <th scope="col">tags</th>
              <th scope="col">date</th>
            </tr>
          </thead>
          <tbody>
            {posts.map((p) =>  <Row  key={p} post={p}/>)}
          </tbody>
        </table>
      </div>
    </div>

  );
}

export default Posts;
