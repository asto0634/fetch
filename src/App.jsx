
import { useEffect, useState } from "react";
import Posts from "./pages/Posts";
import { Routes, Route, Router } from 'react-router-dom';
import Home from "./pages/Home";
import PostDetails from "./pages/PostDetails";

export const BASE_URL = "https://jsonplaceholder.typicode.com/";

function App () {
  return (
   <Routes>
    <Route path="/" element={<Home/>}/>
    <Route path="/posts" element={<Posts/>}/>
    <Route path="/posts/:id" element={<PostDetails/>}/>
   </Routes>
  )
}

export default App