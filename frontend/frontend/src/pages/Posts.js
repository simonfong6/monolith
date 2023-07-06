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
  function createHandle(author) {
    const kMaxLength = 5;
    return author.slice(0, kMaxLength).toLowerCase();
  }

  return (
    <div>
      <div className="card" style={{ width: "18rem" }}>
        <div className="card-body">
          <h6 className="card-subtitle mb-2 text-body-secondary d-flex justify-content-between">
            {post.author}
            <small>@{createHandle(post.author)}</small>
            <small className=" text-body-secondary float-right">
              {timeAgo(post.date)}
            </small>
          </h6>
          <p className="card-text" style={{ whiteSpace: 'pre-wrap' }}>{post.text}</p>
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

function parseTextPost(text) {
  const kAuthorMarker = 'author=';
  const kTagMarker = 'tags=';
  let post = {
    id: -1,
    author: 'Author Frog',
    text: 'Overweight when it gets on the scale.',
    tags: ['foo', 'bar', 'coo'],
    date: new Date(),
  };
  let author = '';
  let tags = [];

  const lines = text.split('\n');

  let remaining = [];

  for (const line of lines) {
    if (line.startsWith(kAuthorMarker)) {
      author = line.replace(kAuthorMarker, '').trim();
      post.author = author
      continue;
    }
    if (line.startsWith(kTagMarker)) {
      const tagsText = line.replace(kTagMarker, '').trim();
      tags = tagsText.split(',');
      post.tags = tags;
      continue;
    }
    remaining.push(line);
  }

  let content = remaining.join('\n');
  post.text = content;


  return post
}



function Posts() {

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('/api/posts/').then(res => res.json()).then(data => {
      setPosts(data);
    });
  }, []);

  useEffect(() => {
    searchAuthor(author);
  }, []);

  const [authorResult, setAuthorResult] = useState(null);

  const [searchParams, setSearchParams] = useSearchParams();

  const author = searchParams.get('author') || '';

  function searchAuthor(authorArg) {
    fetch('/api/posts/author?' + new URLSearchParams({
      author: authorArg,
    })).then(res => res.json()).then(data => {
      setAuthorResult(data);
    });
  }

  function searchOnClick(e) {
    e.preventDefault();
  }

  function createPost(post) {
    console.log('Creating post...');
    console.log(post);
    let authorArg = post.author;
    fetch('/api/posts/new', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(post)
    }).then(res => res.json()).then(data => {
      console.log(data);
      // setAuthorResult(data);
    });
  }

  const draftPost = searchParams.get('draftPost') || '';


  return (

    <div className='container'>
      <h1>this is the posts</h1>

      <div className='container border rounded m-3 p-1'>
        <div className="input-group">
          <textarea className="form-control" aria-label="With textarea"
            value={draftPost}
            onChange={e => {
              setSearchParams(searchParams => {
                searchParams.set('draftPost', e.target.value);
                return searchParams;
              })
            }}
            rows="8"></textarea>
        </div>
        <button type="button" className="btn btn-primary"
          onClick={e => { e.preventDefault(); createPost(parseTextPost(draftPost)) }}
        >
          Post
        </button>
        <div>
          <h5>Preview</h5>
          <Post post={parseTextPost(draftPost)} />
        </div>
      </div>

      <div className='container border rounded m-3 p-1'>
        <form className='container'>
          <div className="mb-3">
            <label htmlFor="exampleInputEmail1" className="form-label">Author</label>
            <input
              value={author} onChange={e => {
                setSearchParams(searchParams => {
                  searchParams.set('author', e.target.value);
                  return searchParams;
                })
                searchAuthor(e.target.value)
              }}
              type="author" className="form-control" id="exampleInputEmail1"
              aria-describedby="emailHelp" />
            <div id="emailHelp" className="form-text">The author whose posts to search for.</div>
          </div>
          <button onClick={e => { searchOnClick(e); searchAuthor(author) }} className="btn btn-primary">Search</button>
        </form>

        <div className='container'>
          <h3>Author Results</h3>
          {authorResult === null ? <div> No Result</div> : <Post post={authorResult} />}
        </div>
      </div>
      <div className='container border rounded m-3'>
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
            {posts.map((p) => <Row key={p} post={p} />)}
          </tbody>
        </table>
      </div>
    </div>

  );
}

export default Posts;
