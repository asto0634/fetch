import { useEffect, useState } from "react";
import { BASE_URL } from "../App";
import { Link } from "react-router-dom";

function Posts() {
  const [posts, setPosts] = useState([]);
  const [isLoading, setLoading] = useState(false);
  
  useEffect(()=> {
    async function fetchPosts() {
      setLoading(true);
      const response = await fetch(`${BASE_URL}/posts`);
      const data = await response.json();
      setPosts(data)
      setLoading(false);
    }
    
    fetchPosts();
  },[]);

  console.log(posts)
  
  return (
    <>
      <h2>Posts</h2>
      <div>
        {isLoading && <h3>Loading...</h3>}
        <div style={styles.container}>
          {posts.map((post)=> (
            <Link to={`/posts/${post.id}`} key={post.id} style={styles.card}>
              <h3 style={styles.title}>{post.title}</h3>
              <p style={styles.body}>{post.body}</p>
              <span style={styles.user}>User ID: {post.userId}</span>
            </Link>
          ))}
        </div>
      </div>
    </>
  )
}

const styles = { 
  container: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))",
    gap: "20px",
    padding: "20px",
    backgroundColor: "#f4f6f8",
  },
  card: {
    backgroundColor: "#fff",
    padding: "15px",
    borderRadius: "10px",
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
    transition: "0.3s",
  },
  title: {
    fontSize: "18px",
    marginBottom: "10px",
    color: "#333",
    textTransform: "capitalize",
  },
  body: {
    fontSize: "14px",
    color: "#555",
    marginBottom: "10px",
    lineHeight: "1.5",
  },
  user: {
    fontSize: "12px",
    color: "#888",
  },
};

export default Posts;
