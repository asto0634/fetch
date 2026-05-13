import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import { BASE_URL } from "../App";

function PostDetails() {
  const { id } = useParams();

  const [isLoading, setLoading] = useState(false);
  const [post, setSinglePost] = useState(null);

  async function fetchSinglePost() {
    setLoading(true);

    const response = await fetch(`${BASE_URL}/posts/${id}`);
    const data = await response.json();

    setSinglePost(data);
    setLoading(false);
  }

  useEffect(() => {
    if (id) {
      fetchSinglePost();
    }
  }, [id]);

  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundColor: "#f4f6f9",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <div
        className="post-card"
        style={{
          backgroundColor: "#fff",
          width: "600px",
          padding: "30px",
          borderRadius: "12px",
          boxShadow: "0 4px 15px rgba(0,0,0,0.1)",
        }}
      >
        <h2
          style={{
            fontSize: "28px",
            marginBottom: "20px",
            color: "#222",
            textTransform: "capitalize",
          }}
        >
          {post?.title}
        </h2>

        <p
          style={{
            fontSize: "16px",
            marginBottom: "10px",
            color: "#555",
          }}
        >
          <strong>Post ID:</strong> {post?.id}
        </p>

        <p
          style={{
            fontSize: "16px",
            marginBottom: "10px",
            color: "#555",
          }}
        >
          <strong>User ID:</strong> {post?.userId}
        </p>

        <p
          style={{
            marginTop: "20px",
            lineHeight: "1.8",
            color: "#444",
            whiteSpace: "pre-line",
          }}
        >
          {post?.body}
        </p>
      </div>
    </div>
  );
}

export default PostDetails;