import React, { useState, useEffect } from 'react';

function Posts() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch('/api/posts/').then(res => res.json()).then(data => {
      setPosts(data);
    });
  }, []);

  const [author, setAuthor] = useState(''); // Declare a state variable...

  const [authorResult, setAuthorResult] = useState(['no results']);

  function fetchAuthorResults(e) {
    e.preventDefault();
    console.log(author);
    fetch('/api/posts/author?' + new URLSearchParams({
      author: author,
    })).then(res => res.json()).then(data => {
      console.log(data);
      if (data === null) {
        setAuthorResult(['no results returned']);
        return;
      }
      setAuthorResult(data);
    });
  }


  return (

    <div className='container'>
      <h1>this is the posts</h1>

      <form>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">Author</label>
          <input
            value={author} onChange={e => setAuthor(e.target.value)}
            type="author" className="form-control" id="exampleInputEmail1"
            aria-describedby="emailHelp" />
          <div id="emailHelp" className="form-text">The author whose posts to search for.</div>
        </div>
        <button onClick={e => fetchAuthorResults(e)} className="btn btn-primary">Search</button>
      </form>

      <div>
        <h3>Author Results</h3>
        <div>
          {authorResult}
        </div>
      </div>

      <div>
        These are words
        <p>The current time is {currentTime}. (From API server: /time)</p>
      </div>

      <div>
        {posts.map((p) => <li key={p[0]}>{p[0]} = {p[1]} | {p}</li>)}

      </div>
    </div>

  );
}

export default Posts;
